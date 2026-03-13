import os
import json
import time
import PIL.Image
import tenacity
from google import genai
from google.genai import errors
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class MathMentorSystem:
    def __init__(self, model="gemini-3.1-flash-lite-preview"):
        self.model = model

    @tenacity.retry(
        retry=tenacity.retry_if_exception_type(errors.ClientError),
        wait=tenacity.wait_exponential(multiplier=1, min=2, max=10),
        stop=tenacity.stop_after_attempt(5),
        reraise=True
    )
    def _call(self, system, user, image=None):
        contents = [system, user]
        if image:
            contents.append(image)
        
        config = None
        if "JSON" in system.upper():
            config = {"response_mime_type": "application/json"}
            
        try:
            res = client.models.generate_content(
                model=self.model,
                contents=contents,
                config=config
            )
            return res.text if res.text else ""
        except errors.ClientError as e:
            # Re-raise so tenacity can retry or reraise=True propagates it
            raise e
        except Exception as e:
            raise e

    def _stream_call(self, system, user):
        max_retries = 3
        retry_count = 0
        while retry_count < max_retries:
            try:
                res = client.models.generate_content_stream(
                    model=self.model,
                    contents=[system, user]
                )
                for chunk in res:
                    if chunk.text:
                        yield chunk.text
                return # Success
            except errors.ClientError as e:
                if "429" in str(e) and retry_count < max_retries - 1:
                    retry_count += 1
                    time.sleep(2 ** retry_count)
                    continue
                yield f"\n[STREAM ERROR]: {str(e)}"
                break
            except Exception as e:
                yield f"\n[STREAM ERROR]: {str(e)}"
                break

    def vision_parser_agent(self, image):
        system = """You are a Math Vision Agent. Analyze the provided image of a mathematical problem and extract all details into JSON format:
        {
          "problem_text": "Cleaned mathematical question using plain text and standard symbols (no LaTeX)",
          "topic": "Algebra|Calculus|Linear Algebra|Probability",
          "variables": ["v1", "v2"],
          "constraints": ["c1", "c2"],
          "needs_clarification": boolean
        }
        Do NOT use LaTeX. Use standard text representation for math (e.g., ^ for power, * for multiplication, sqrt() for roots)."""
        
        try:
            raw_response = self._call(system, "Extract the math problem from this image.", image=image)
            if "```json" in raw_response:
                raw_response = raw_response.split("```json")[1].split("```")[0].strip()
            elif "```" in raw_response:
                raw_response = raw_response.split("```")[1].strip()
                
            return json.loads(raw_response)
        except Exception as e:
            return {
                "problem_text": "Vision extraction failed",
                "topic": "Algebra",
                "variables": [],
                "constraints": [],
                "needs_clarification": True,
                "error": f"Vision parsing failed: {str(e)}"
            }

    def parser_agent(self, raw_input):
        system = """You are a Math Extraction Agent. Extract details into JSON format:
        {
          "problem_text": "Cleaned mathematical question in plain text (no LaTeX)",
          "topic": "Algebra|Calculus|Linear Algebra|Probability",
          "variables": ["v1", "v2"],
          "constraints": ["c1", "c2"],
          "needs_clarification": boolean
        }
        Do NOT use LaTeX. Use plain text formatting."""
        
        try:
            raw_response = self._call(system, raw_input)
            # Remove any markdown code block artifacts if they exist
            if raw_response.startswith("```json"):
                raw_response = raw_response.split("```json")[1].split("```")[0].strip()
            elif "```" in raw_response:
                raw_response = raw_response.split("```")[1].strip()
                
            parsed = json.loads(raw_response)
            
            # Ensure mandatory keys exist
            if "problem_text" not in parsed:
                parsed["problem_text"] = raw_input
            if "needs_clarification" not in parsed:
                parsed["needs_clarification"] = False
            
            return parsed
        except Exception as e:
            # Absolute fallback if parsing fails
            return {
                "problem_text": raw_input,
                "topic": "Algebra",
                "variables": [],
                "constraints": [],
                "needs_clarification": False,
                "error": f"Parsing failed: {str(e)}"
            }

    def router_agent(self, problem_json):
        system = "Route this problem to the correct sub-topic (Algebra, Calculus, Linear Algebra, or Probability). Output ONLY the topic name."
        return self._call(system, str(problem_json)).strip()

    def solver_agent(self, problem, context, memory_context=""):
        system = f"""You are a Master JEE Math Solver. Your goal is to provide a logically flawless and beautifully structured solution.
        
        STRICT FORMATTING RULES:
        1. DO NOT use LaTeX (no $, $$, \\(, \\[, etc.).
        2. Use plain text and standard mathematical notation (e.g., ^ for power, / for division, * for multiplication, sqrt for square root).
        3. Keep the output clean and highly structured.
        4. Reference context: {context}. Reference past cases: {memory_context}.
        
        STRUCTURE:
        ### Objective
        (Problem goal)
        
        ### Key Concepts
        (Formulas/principles used in plain text)
        
        ### Step-by-Step Solution
        (Detailed numbered steps)
        
        ### Final Answer
        (Result clearly highlighted)"""
        return self._call(system, problem)

    def solver_agent_stream(self, problem, context, memory_context=""):
        system = f"""You are a Master JEE Math Solver. Your goal is to provide a logically flawless and beautifully structured solution.
        
        STRICT FORMATTING RULES:
        1. DO NOT use LaTeX (no $, $$, \\(, \\[, etc.).
        2. Use plain text and standard mathematical notation.
        3. Keep the output clean and highly structured.
        4. Reference context: {context}. Reference past cases: {memory_context}.
        
        STRUCTURE:
        ### Objective
        (Problem goal)
        
        ### Key Concepts
        (Formulas/principles used in plain text)
        
        ### Step-by-Step Solution
        (Detailed numbered steps)
        
        ### Final Answer
        (Result clearly highlighted)"""
        return self._stream_call(system, problem)

    def verifier_agent(self, solution):
        system = """Verify the math solution. Ensure it is logically correct and follows the plain text requirement:
        - NO LaTeX delimiters.
        - Structured and clear.
        Return JSON: {"is_confident": bool, "errors": [], "final_verdict": ""}"""
        
        try:
            raw_response = self._call(system, solution)
            if raw_response.startswith("```json"):
                raw_response = raw_response.split("```json")[1].split("```")[0].strip()
            elif "```" in raw_response:
                raw_response = raw_response.split("```")[1].strip()
            
            return json.loads(raw_response)
        except Exception:
            return {
                "is_confident": False,
                "errors": ["Failed to parse verification result from model."],
                "final_verdict": "ERROR"
            }

    def explainer_agent(self, solution):
        system = """You are a JEE Physics & Math Mentor. Your task is to transform technical solutions into conceptual masterclasses.
        
        STRICT FORMATTING RULES:
        1. DO NOT use LaTeX.
        2. Use clean, plain text and structured formatting.
        
        STRUCTURE:
        ---
        ###  The Core Logic
        (Explain the 'why' behind the chosen approach in plain text)
        
        ###  Avoid These Pitfalls
        (Mention common mistakes students make in this specific topic)
        
        ###  Pro-Tip
        (Provide a shortcut or a mental model for this type of problem)
        ---"""
        return self._call(system, solution)


    def explainer_agent_stream(self, solution):
        system = """You are a JEE Physics & Math Mentor. Your task is to transform technical solutions into conceptual masterclasses.
        
        STRICT FORMATTING RULES:
        1. DO NOT use LaTeX.
        2. Use clean, plain text and structured formatting.
        
        STRUCTURE:
        ---
        ###  The Core Logic
        (Explain the 'why' behind the chosen approach in plain text)
        
        ###  Avoid These Pitfalls
        (Mention common mistakes students make in this specific topic)
        
        ###  Pro-Tip
        (Provide a shortcut or a mental model for this type of problem)
        ---"""
        return self._stream_call(system, solution)

    def refine_transcript(self, transcript):
        system = r"""You are a Math Transcript Refiner. 
        Convert verbal math descriptions into technical mathematical notation (PLAIN TEXT ONLY, NO LATEX).
        
        STRICT RULES:
        - DO NOT use LaTeX delimiters like $, $$, etc.
        - Use ^ for power, sqrt() for roots, etc.
        
        Example: 
        - "square root of x plus 5" -> "sqrt(x + 5)"
        - "x raised to the power of 2" -> "x^2"
        - "integral of sine x" -> "integral(sin(x) dx)"
        
        If unclear, prefix with '[UNCLEAR]: '."""
        return self._call(system, transcript)