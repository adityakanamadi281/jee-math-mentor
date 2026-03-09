import streamlit as st
from agents import MathMentorSystem
from utils.rag import MathRAG
from utils.memory import save_memory, search_memory
from utils.parser import ocr_process, speech_to_text

st.set_page_config(page_title="Multimodal Math Mentor", layout="wide", page_icon="🎓")
rag = MathRAG()
system = MathMentorSystem()

# Custom CSS for Premium Look
st.markdown("""
    <style>
    .main { background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); }
    .stButton>button { width: 100%; border-radius: 20px; border: none; background: #4e73df; color: white; font-weight: bold; }
    .stTextArea>div>div>textarea { border-radius: 10px; border: 1px solid #4e73df; }
    .stAlert { border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎓 JEE Math Mentor")
st.caption("AI-Powered Multi-Agent System for Math Problem Solving")

# --- 1. Input Section ---
with st.sidebar:
    st.header("⚙️ Configuration")
    mode = st.selectbox("Input Mode", ["Text", "Image (OCR)", "Audio (ASR)"])
    st.divider()
    st.info(".")

raw_text = ""

if mode == "Text":
    raw_text = st.text_area("Enter Math Problem:", placeholder="e.g., Solve for x: 2x + 5 = 15")
elif mode == "Image (OCR)":
    uploaded_file = st.file_uploader("Upload Image", type=['png', 'jpg', 'jpeg'])
    if uploaded_file:
        with st.status("🔍 Processing Math OCR...") as status:
            extracted = ocr_process(uploaded_file)
            status.update(label="OCR Complete. Please verify below.", state="complete")
        raw_text = st.text_area("Verify & Correct OCR Output:", value=extracted, height=150)
        st.info("💡 You can edit the text above if the OCR missed any symbols.")
elif mode == "Audio (ASR)":
    audio_tab1, audio_tab2 = st.tabs(["🎤 Record", "📁 Upload"])
    audio_file = None
    with audio_tab1:
        recorded_audio = st.audio_input("Record your question")
        if recorded_audio:
            audio_file = recorded_audio
    with audio_tab2:
        uploaded_audio = st.file_uploader("Upload Audio File", type=['wav', 'mp3', 'm4a'])
        if uploaded_audio:
            audio_file = uploaded_audio
    
    if audio_file:
        with st.status("🎙️ Transcribing and Math-Refining...") as status:
            transcript = speech_to_text(audio_file)
            status.update(label="Transcribed. Refining math phrases...", state="running")
            # Refine verbal math to symbolic math
            refined = system.refine_transcript(transcript)
            status.update(label="Transcription Finished", state="complete")
        
        if "[UNCLEAR]" in refined:
            st.warning("⚠️ The transcription seems unclear. Please verify and correct the text below.")
            refined = refined.replace("[UNCLEAR]: ", "")
            
        raw_text = st.text_area("Verify & Correct Transcript:", value=refined, height=150)
        st.caption(f"Original Transcript: *{transcript}*")

# --- 2. Solve Workflow ---
if st.button("🚀 Solve Problem") and raw_text:
    # Set this to identify that we are currently solving for this specific text
    st.session_state.raw_text_for_sol = raw_text
    
    # A. Memory Check (Self-Learning)
    similar_past_cases = search_memory(raw_text)
    
    st.divider()
    col1, col2 = st.columns([3, 2])

    # RUN AGENTS IN SEQUENCE - Optimized and Streamed
    with st.status("🧠 Agents collaborating...") as status:
        # 1. Parser
        parsed = system.parser_agent(raw_text)
        st.session_state.parsed = parsed
        
        # HITL Trigger: Ambiguity
        if parsed.get("needs_clarification"):
            st.warning("⚠️ Parser detected ambiguity. Please clarify the problem.")
            st.stop()

        # 2. Router & RAG (Parallel-like feel)
        topic = system.router_agent(parsed)
        problem_text = parsed.get('problem_text', raw_text)
        context = rag.retrieve(problem_text)
        
        st.write(f"**Router:** `{topic}` | **Context:** Found formulas.")
        
        # 3. Solver (Streamed directly to UI)
        status.update(label="✍️ Expert solving...", state="running")
        with col1:
            with st.container(border=True):
                st.header("📝 Expert Solution")
                full_solution = st.write_stream(system.solver_agent_stream(problem_text, context, similar_past_cases))
                st.session_state.full_solution = full_solution
        
        # 4. Verifier
        status.update(label="🔎 Verifying logic...", state="running")
        verification = system.verifier_agent(full_solution)
        with col1:
            if not verification.get('is_confident', False):
                st.error(f"⚠️ **Verifier:** {verification.get('final_verdict', 'Needs review.')}")
            else:
                st.success(f"✅ **Verifier:** Verified logic.")

        # 5. Explainer
        status.update(label="💡 Finalizing tutor notes...", state="running")
        with col2:
            with st.container(border=True):
                st.header("💡 Tutor's Corner")
                st.write_stream(system.explainer_agent_stream(full_solution))
        
        status.update(label="✅ All agents complete", state="complete")

# --- 3. Feedback Loop ---
# Check if we have a solution that matches the Current text
if 'full_solution' in st.session_state and raw_text == st.session_state.get('raw_text_for_sol', ''):
    st.divider()
    st.write("### 🛠️ Continuous Learning")
    f_col1, f_col2 = st.columns(2)
    with f_col1:
        if st.button("✅ Mark as Correct"):
            save_memory(raw_text, st.session_state.full_solution, "Correct")
            st.success("Learned from this solution!")
    with f_col2:
        comment = st.text_input("Feedback/Correction:", placeholder="Optional comment...")
        if st.button("❌ Submit Feedback"):
            save_memory(raw_text, st.session_state.full_solution, f"Incorrect: {comment}")
            st.info("Feedback stored for future improvement.")

# Cleanup session state if the input text changes without solving
if raw_text != st.session_state.get('raw_text_for_sol', ''):
    for key in ['full_solution', 'parsed']:
        if key in st.session_state:
            del st.session_state[key]