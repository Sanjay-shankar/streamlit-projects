import streamlit as st
from langchain.llms import OpenAI  # Use this if ChatOpenAI is unavailable

st.title('Sample Apps')

# Sidebar input for API key
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

def generate_response(input_text):
    if openai_api_key.startswith('sk-'):
        llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
        response = llm(input_text)
        st.info(response)
    else:
        st.error("Invalid OpenAI API Key")

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are ----')
    submitted = st.form_submit_button('Submit')

    if not openai_api_key:
        st.warning('Please enter your OpenAI API key', icon='⚠️')
    elif submitted:
        generate_response(text)
