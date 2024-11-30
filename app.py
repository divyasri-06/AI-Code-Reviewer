import streamlit as st
import google.generativeai as ai
from dotenv import load_dotenv
import os


load_dotenv()
# config your Gemini API key

ai.configure(api_key=os.getenv("GEMINI_API_KEY"))

st.title("AI Code Review Application")
st.subheader("Issue with your Python code? Review your code now!")

sys_prompt = """You are a helpful and experienced AI tutor for Python Language.
                You are given a python code to review and anlayse the submitted code.
                You are expected to identify the bugs or errors and provide the fixed code along with explanation for code corrections.
                If the code is not in python, politely remind the user that you are a python code review assistant."""

model = ai.GenerativeModel(model_name = "gemini-1.5-flash", system_instruction=sys_prompt)

user_prompt = st.text_area("Enter your code:", placeholder="Type your code here...")


btn_click = st.button("Submit")

if btn_click == True:
    if user_prompt:
        responses = model.generate_content(user_prompt)
        st.write(responses.text)