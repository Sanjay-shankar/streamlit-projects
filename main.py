import streamlit as st
from langchain.llms import OpenAI  # Or ChatOpenAI, based on your version

st.title("Sample App")

# Retrieve the OpenAI API key from Streamlit secrets
openai_api_key = st.secrets["openai"]["api_key"]

def generate_response(input_text):
    if openai_api_key.startswith('sk-'):
        llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
        response = llm(input_text)
        st.info(response)
    else:
        st.error("Invalid OpenAI API Key")

with st.form("my_form"):
    text = st.text_area("Enter text:", "What are ----")
    submitted = st.form_submit_button("Submit")

    if submitted:
        generate_response(text)
