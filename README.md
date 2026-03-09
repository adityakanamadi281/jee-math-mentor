# 🎓 JEE Math Mentor: AI-Powered Multi-Agent Math Solver

A premium, multimodal math tutoring system designed to solve complex JEE-level mathematical problems using a multi-agent orchestration pattern. This system supports **Text**, **Image (OCR)**, and **Voice (ASR)** inputs, providing step-by-step solutions with high-fidelity LaTeX formatting.

---

## 🚀 Key Features

- **Multimodal Input Support**:
  - **Text**: Direct input of mathematical expressions.
  - **Image (OCR)**: Extracts math from photos/handwriting using optimized `EasyOCR`.
  - **Audio (ASR)**: Voice-to-math transcription using `faster-whisper` (Tiny model).
- **Multi-Agent Orchestration**:
  - **Parser Agent**: Extracts mathematical entities and constraints.
  - **Router & RAG**: Fetches relevant formulas from the integrated knowledge base.
  - **Solver Agent**: Generates detailed, step-by-step solutions.
  - **Verifier Agent**: Performs logical and formatting checks on the solution.
  - **Explainer Agent**: Provides conceptual "Pro-Tips" and warns against common pitfalls.
- **CPU-Optimized Performance**:
  - Leverages 8-bit quantization for models.
  - Smart image resizing to speed up OCR on standard hardware.
  - Efficient thread management for PyTorch on CPU.
- **Continuous Learning**: Users can provide feedback (Correct/Incorrect) which the system stores to improve future reasoning via local memory.

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit (Premium UI)
- **OCR**: EasyOCR
- **ASR**: Faster-Whisper
- **LLM Orchestration**: OpenRouter (GPT/Flash models)
- **Vector DB**: ChromaDB with FastEmbed
- **Core Ops**: PyTorch & LangChain

---

## 📂 Project Structure

```text
├── agents.py           # Core agent logic and system prompts
├── app.py              # Streamlit UI and workflow management
├── utils/
│   ├── parser.py       # OCR and ASR processing (CPU Optimized)
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
   Create a `.env` file or set up Streamlit secrets:
   ```text
   OPENROUTER_API_KEY=your_key_here
   ```

5. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

---

## 🧠 Optimization Notes (CPU)

If you are running on a machine without a dedicated GPU:
- The system automatically suppresses unnecessary GPU memory warnings.
- Images are scaled to 1200px width before OCR processing to maintain speed.
- Torch is configured to use optimal CPU threading (`torch.set_num_threads`).
- Whisper uses the `int8` compute type for highly efficient audio processing.

---

## 🤝 Feedback

This project is a work in progress. If you encounter any "unclear" transcriptions or OCR misses, use the **Continuous Learning** panel in the app to mark the problem as incorrect and provide feedback. The agent will learn from your corrections!
