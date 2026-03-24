import streamlit as st
import cv2
import pandas as pd
from deepface import DeepFace
from datetime import datetime

st.set_page_config(page_title="Micro-AI Detector", layout="wide")

# This keeps data alive as you switch between pages
if "data" not in st.session_state:
    st.session_state.data = []

st.title("📹 Live Micro-Expression Analysis")

# UI Layout
col1, col2 = st.columns([2, 1])

with col1:
    img_file = st.camera_input("Take a snapshot to analyze expression")
    if img_file:
        file_bytes = img_file.getvalue()
        # Analyze using DeepFace
        res = DeepFace.analyze(img_path=file_bytes, actions=['emotion'], enforce_detection=False)
        
        emo = res[0]['dominant_emotion']
        conf = res[0]['emotion'][emo]
        
        # Save to history
        st.session_state.data.append({
            "Timestamp": datetime.now().strftime("%H:%M:%S"),
            "Emotion": emo,
            "Confidence": conf
        })
        st.success(f"Detected: {emo.upper()} ({conf:.2f}%)")

with col2:
    st.subheader("Session History")
    if st.session_state.data:
        st.table(pd.DataFrame(st.session_state.data).tail(5))
