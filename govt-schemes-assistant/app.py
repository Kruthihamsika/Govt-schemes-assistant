import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Streamlit UI
st.set_page_config(page_title="Govt Schemes Assistant", page_icon="🇮🇳")
st.title("🇮🇳 Indian Government Schemes Assistant")

user_query = st.text_input("🔍 Enter a scheme name or ask about a government scheme:")

if st.button("Get Explanation"):
    if user_query.strip():
        with st.spinner("Fetching details..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert assistant explaining Indian government schemes. Answer in both Telugu and English."
                    },
                    {"role": "user", "content": user_query}
                ]
            )
            st.write(response.choices[0].message.content)
    else:
        st.warning("⚠️ Please enter a scheme name or query.")
