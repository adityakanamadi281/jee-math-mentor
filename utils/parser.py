import torch
from faster_whisper import WhisperModel
import easyocr
import tempfile
import os
import numpy as np
from PIL import Image
import io
import streamlit as st

# OPTIMIZATION: Set torch threads at the module level for CPU performance
torch.set_num_threads(os.cpu_count() or 4)
torch.set_num_interop_threads(1)

@st.cache_resource
def get_ocr_reader():
    # Only load English and use gpu=False explicitly for CPU environments
    return easyocr.Reader(['en'], gpu=False)

@st.cache_resource
def get_whisper_model():
    # 'tiny.en' is fastest for English. compute_type="int8" is most efficient for CPU.
    return WhisperModel("tiny.en", device="cpu", compute_type="int8")

def ocr_process(file):
    """Processes image file using EasyOCR (Optimized for CPU)"""
    try:
        image = Image.open(file).convert('RGB')
        
        # SPEED OPTIMIZATION: Resize huge images to speed up detection/recognition
        # Maximum width of 1200px is usually enough for math recognition
        max_size = 1200
        if image.width > max_size or image.height > max_size:
            ratio = min(max_size / image.width, max_size / image.height)
            new_size = (int(image.width * ratio), int(image.height * ratio))
            image = image.resize(new_size, Image.Resampling.LANCZOS)
            
        image_np = np.array(image)
        
        ocr_reader = get_ocr_reader()
        # detail=0: Returns only text strings (FASTER)
        # decoder='greedy': Faster than beam search (FASTER)
        results = ocr_reader.readtext(image_np, detail=0, decoder='greedy')
        return " ".join(results)
    except Exception as e:
        return f"OCR Error: {str(e)}"

def speech_to_text(audio_file):
    """Processes audio file using faster-whisper (tiny model)"""
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
            tmp_file.write(audio_file.read())
            tmp_path = tmp_file.name
        
        model = get_whisper_model()
        # beam_size=1: Fastest transcription (Greedy search)
        # vad_filter=True: Skips silence, reducing compute load
        segments, info = model.transcribe(
            tmp_path, 
            beam_size=1, 
            vad_filter=True, 
            vad_parameters=dict(min_silence_duration_ms=500)
        )
        
        transcript = []
        for segment in segments:
            transcript.append(segment.text)
        
        full_text = " ".join(transcript).strip()
        
        # Cleanup
        os.remove(tmp_path)
        return full_text
    except Exception as e:
        return f"ASR Error: {str(e)}"
