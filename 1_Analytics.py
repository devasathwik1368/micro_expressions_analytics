import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Behavioral Analytics")

if not st.session_state.data:
    st.warning("Go to the main page and capture some expressions first!")
else:
    df = pd.DataFrame(st.session_state.data)
    
    # Chart 1: Emotion Trends
    st.subheader("Emotion Timeline")
    st.line_chart(df.set_index('Timestamp')['Confidence'])
    
    # Chart 2: Distribution
    st.subheader("Sentiment Breakout")
    fig, ax = plt.subplots()
    df['Emotion'].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax)
    st.pyplot(fig)
