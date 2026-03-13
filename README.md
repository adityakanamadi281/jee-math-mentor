# 🎓 JEE Math Mentor: AI-Powered Multi-Agent Math Solver

A premium, multimodal math tutoring system designed to solve complex JEE-level mathematical problems using a multi-agent orchestration pattern. This system supports **Text**, **Image (OCR)**, and **Voice (ASR)** inputs, providing step-by-step solutions with detailed conceptual guidance.

---

## 🚀 Key Features

- **Multimodal Input Support**:
  - **Text**: Direct input of mathematical expressions.
  - **Image (OCR)**: Extracts math from photos/handwriting using **Gemini Vision**.
  - **Audio (ASR)**: Voice-to-math transcription using `faster-whisper` (Tiny model) with automated math-refinement.
- **Multi-Agent Orchestration**:
  - **Parser Agent**: Extracts mathematical entities and classifies the topic.
  - **Router & RAG**: Fetches relevant formulas from the integrated knowledge base.
  - **Solver Agent**: Generates detailed, step-by-step solutions using **Gemini 3.1 Flash**.
  - **Verifier Agent**: Performs logical and formatting checks on the solution.
  - **Explainer Agent**: Provides conceptual "Pro-Tips" and warns against common pitfalls.
- **Resilient & Robust**:
  - **Exponential Backoff**: Integrated retry logic to handle API rate limits gracefully.
  - **Global Error Handling**: Custom boundaries to manage quota issues and provide feedback.
- **CPU-Optimized Performance**:
  - Smart thread management for PyTorch on CPU.
  - Efficient image prep and quantized `int8` audio processing for speed.
- **Continuous Learning**: Users can provide feedback (Correct/Incorrect) which the system stores to improve future reasoning via local memory.

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit (Premium UI)
- **OCR**: Gemini 3.1 Vision
- **ASR**: Faster-Whisper
- **LLM**: Google Gemini API (3.1 Flash / 3.1 Flash Lite)
- **Vector DB**: ChromaDB with FastEmbed
- **Core Ops**: PyTorch, LangChain, and Tenacity

---

## 📂 Project Structure

```text
├── agents.py           # Core agent logic and system prompts
├── app.py              # Streamlit UI and workflow management
├── utils/
│   ├── parser.py       # ASR processing (CPU Optimized)
│   ├── rag.py          # Vector database and formula retrieval
│   └── memory.py       # Local feedback and learning system
├── knowledge_base/     # Markdown files with JEE Math formulas
└── requirements.txt    # Project dependencies
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/adityakanamadi281/jee-math-mentor.git
   cd jee-math-mentor
   ```

2. **Create a virtual environment**:
   ```bash
   uv venv
   ```

3. **Install dependencies**:
   ```bash
   uv pip install -r requirements.txt
   ```

4. **Environment Variables**:
   Create a `.env` file in the root directory:
   ```text
   GEMINI_API_KEY=your_google_ai_studio_key
   ```

5. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

---

## 🧠 Optimization Notes (CPU)

If you are running on a machine without a dedicated GPU:
- The system automatically suppresses unnecessary GPU memory warnings.
- Torch is configured to use optimal CPU threading (`torch.set_num_threads`).
- Whisper uses the `int8` compute type for highly efficient audio processing.
- Multi-agent bursts are managed with exponential retries to stay within free-tier quotas.

---

## 🤝 Feedback

<<<<<<< HEAD
This project is a work in progress. If you encounter any "unclear" transcriptions or OCR misses, use the **Continuous Learning** panel in the app to mark the problem as incorrect and provide feedback. The agent will learn from your corrections!

## Deployment 
### [click here](https://jee-math-mentor.streamlit.app/)
=======
The system learns from you! If you encounter any "unclear" transcriptions or logical errors, use the **Continuous Learning** panel in the app to mark the problem as incorrect and provide feedback. The agent will learn from your corrections!


