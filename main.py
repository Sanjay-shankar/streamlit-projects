import streamlit as st
from langchain.chat_models import ChatOpenAI

st.title("🦜🔗 Quickstart App")

# Retrieve the OpenAI API key from Streamlit secrets
openai_api_key = st.secrets.get("openai", {}).get("api_key", None)

if not openai_api_key:
    st.error("OpenAI API key is missing! Please set it in Streamlit secrets.")
else:
    def generate_response(input_text):
        try:
            # Initialize the ChatOpenAI model with the API key
            model = ChatOpenAI(temperature=0.7, openai_api_key=openai_api_key)
            response = model.invoke(input_text)
            st.info(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")

    with st.form("my_form"):
        text = st.text_area(
            "Enter text:",
            "What are the three key pieces of advice for learning how to code?",
        )
        submitted = st.form_submit_button("Submit")
        if submitted:
            generate_response(text)
