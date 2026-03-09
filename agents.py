import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY"))

class MathMentorSystem:
    def __init__(self, model="stepfun/step-3.5-flash:free"):
        self.model = model

    def _call(self, system, user):
        response_format = { "type": "json_object" } if "JSON" in system.upper() else None
        res = client.chat.completions.create(
            model=self.model,
            messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
            response_format=response_format
        )
        if res.choices and len(res.choices) > 0:
            return res.choices[0].message.content
        return ""

    def _stream_call(self, system, user):
        try:
            res = client.chat.completions.create(
                model=self.model,
                messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
                stream=True
            )
            for chunk in res:
                if chunk.choices and len(chunk.choices) > 0:
                    delta = chunk.choices[0].delta
                    if hasattr(delta, 'content') and delta.content:
                        yield delta.content
        except Exception as e:
            yield f"\n[STREAM ERROR]: {str(e)}"

    def parser_agent(self, raw_input):
        system = """You are a Math Extraction Agent. Extract details into JSON format:
        {
          "problem_text": "Cleaned mathematical question",
          "topic": "Algebra|Calculus|Linear Algebra|Probability",
          "variables": ["v1", "v2"],
          "constraints": ["c1", "c2"],
          "needs_clarification": boolean
        }
        Ensure all LaTeX formulas are escaped properly with $ or $$."""
        
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
        system = f"""You are a Master JEE Math Solver. Your goal is to provide a logically flawless and beautifully formatted solution.
        
        STRICT FORMATTING RULES:
        1. USE ONLY '...' for inline math. NEVER use '(...)'.
        2. USE ONLY '...' for block equations on THEIR OWN LINE. NEVER use '[...]'.
        3. DO NOT use markdown code blocks (```) for mathematical equations.
        4. Reference context: {context}. Reference past cases: {memory_context}.
        
        STRUCTURE:
        ### Objective
        (Problem goal)
        
        ### Key Concepts
        (Formula used)
        
        ### Step-by-Step Solution
        (Detailed steps)
        
        ### Final Answer
        (Result clearly highlighted)"""
        return self._call(system, problem)

    def solver_agent_stream(self, problem, context, memory_context=""):
        system = f"""You are a Master JEE Math Solver. Your goal is to provide a logically flawless and beautifully formatted solution.
        
        STRICT FORMATTING RULES:
        1. USE ONLY '...' for inline math. NEVER use '(...)'.
        2. USE ONLY '...' for block equations on THEIR OWN LINE. NEVER use '[...]'.
        3. DO NOT use markdown code blocks (```) for mathematical equations.
        4. Reference context: {context}. Reference past cases: {memory_context}.
        
        STRUCTURE:
        ### Objective
        (Problem goal)
        
        ### Key Concepts
        (Formulas used)
        
        ### Step-by-Step Solution
        (Detailed steps)
        
        ###  Final Answer
        (Result clearly highlighted)"""
        return self._stream_call(system, problem)

    def verifier_agent(self, solution):
        system = """Verify the math solution. Ensure it follows the STRICT LaTeX delimiters:
        - Inline: ...
        - Block: ...
        Reject if it uses (...) or [...]. 
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
        
        STRUCTURE:
        ---
        ###  The Core Logic
        (Explain the 'why' behind the chosen approach)
        
        ###  Avoid These Pitfalls
        (Mention common mistakes students make in this specific topic)
        
        ###  Pro-Tip
        (Provide a shortcut or a mental model for this type of problem)
        ---
        Use LaTeX for all math."""
        return self._call(system, solution)


    def explainer_agent_stream(self, solution):
        system = """You are a JEE Physics & Math Mentor. Your task is to transform technical solutions into conceptual masterclasses.
        
        STRUCTURE:
        ---
        ###  The Core Logic
        (Explain the 'why' behind the chosen approach)
        
        ###  Avoid These Pitfalls
        (Mention common mistakes students make in this specific topic)
        
        ###  Pro-Tip
        (Provide a shortcut or a mental model for this type of problem)
        ---
        Use LaTeX for math."""
        return self._stream_call(system, solution)

    def refine_transcript(self, transcript):
        system = r"""You are a Math Transcript Refiner. 
        Convert verbal math descriptions into technical mathematical notation.
        
        STRICT DELIMITER RULES:
        - Use '...' for inline math.
        - Use '...' for block math.
        - NEVER use '(...)', '[...]', or custom delimiters.
        
        Example: 
        - "square root of x plus 5" -> "\sqrt{x + 5}"
        - "x raised to the power of 2" -> "x^2"
        - "integral of sine x" -> "\int \sin(x) dx"
        
        If unclear, prefix with '[UNCLEAR]: '."""
        return self._call(system, transcript)