import streamlit as st
import requests
import json

st.set_page_config(page_title="OlympicCoder-7B UI", layout="wide")

st.title("OlympicCoder-7B")
st.markdown("A simple interface for interacting with the OlympicCoder-7B model")

with st.form("input_form"):
    prompt = st.text_area("Enter your prompt:", height=150, 
                         placeholder="Write a Python function to...")
    
    col1, col2 = st.columns(2)
    with col1:
        max_tokens = st.slider("Max tokens", min_value=50, max_value=2000, value=500, step=50)
    with col2:
        temperature = st.slider("Temperature", min_value=0.1, max_value=1.0, value=0.7, step=0.1)
    
    submit_button = st.form_submit_button("Generate Code")

if submit_button and prompt:
    with st.spinner("Generating code..."):
        try:
            response = requests.post(
                "http://localhost:8000/generate",
                json={
                    "prompt": prompt,
                    "max_tokens": max_tokens,
                    "temperature": temperature
                },
                timeout=60
            )
            
            if response.status_code == 200:
                result = response.json()
                st.subheader("Generated Code:")
                st.code(result["text"][0], language="python")
                
                with st.expander("Raw API Response"):
                    st.json(result)
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"Error connecting to the model API: {str(e)}")
