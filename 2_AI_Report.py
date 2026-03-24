import streamlit as st
import pandas as pd
from groq import Groq

st.title("🤖 Groq AI Negotiation Insights")

# Setup Groq Client
api_key = st.sidebar.text_input("Enter Groq API Key", type="password")

if st.button("Generate Professional Report"):
    if not st.session_state.data:
        st.error("No data found.")
    elif not api_key:
        st.error("Please add your Groq API Key in the sidebar.")
    else:
        client = Groq(api_key=api_key)
        df = pd.DataFrame(st.session_state.data)
        summary = df['Emotion'].value_counts().to_string()

        prompt = f"Analyze these micro-expressions for a negotiation session: {summary}. Provide mental health status and 3 negotiation tips."
        
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}]
        )
        st.markdown(completion.choices[0].message.content)
