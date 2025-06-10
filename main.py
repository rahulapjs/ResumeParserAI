import os
from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader
import google.generativeai as genai
from google.generativeai import GenerativeModel
import json

# UI Title
st.title("📄 Gemini PDF Analyzer")

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

st.sidebar.title("🔑 API Configuration")
api_key = st.sidebar.text_input("Enter your API Key", value=gemini_api_key if gemini_api_key else "")
model_options = ["gemini-1.5-flash", "gemini-1.5-pro"]
selected_model = st.sidebar.selectbox("🧠 Select a Gemini Model", model_options, index=0)


def display_parsed_resume(data: dict):
    with st.spinner("🧠 Generating professional summary..."):
        summary_prompt = f"""
         Act as a professional resume writer.

        Using the following resume data in JSON format, write a short and engaging first-person self-introduction. 
        The tone should be confident, natural, and suitable for situations like interviews or personal bios. 
        Include key skills, work experiences, notable projects, and education in a smooth, storytelling format. 
        Avoid listing — instead, focus on creating a personal narrative.

        Resume JSON:
        {json.dumps(data, indent=2)}
        """

        summary_response = model.generate_content(summary_prompt)
        summary_text = summary_response.text

    st.subheader("🧑‍💼 Professional Summary")
    st.write(summary_text)


if api_key:
    # Configure Gemini API
    genai.configure(api_key=api_key)
    model = GenerativeModel(selected_model)
    uploaded_file = st.file_uploader("📤 Upload your CV (PDF only)", type=["pdf"])

    if uploaded_file:
        st.success("✅ Upload complete. Extracting content...")

        # Extract text from PDF
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        if text.strip():
            prompt = f"""
                            You are a professional resume parser. From the following resume text, extract the following details and return them in a structured JSON format:
                            - Name
                            - Email
                            - Location (city, state, country, or any address details)
                            - Work Experience (list of entries with job title, company, duration, and description)
                            - Projects (list of project names and brief descriptions)
                            - Skills (list of skills)
                            - Education (list of degrees, institutions, and years)
                            - Any other relevant details (e.g., phone number, certifications, etc.)

                            If any information is missing, indicate it as "Not found" or an empty list/array for that category. Be precise and avoid fabricating information.

                            Resume text:
                            {text}

                            Only return the summary. Do not include any formatting like JSON blocks or code fences..
                            """
            # Generate response using Gemini
            with st.spinner("🔍 Analyzing PDF content with Gemini..."):
                response = model.generate_content(prompt)
                extracted_data = response.text

                json_data = json.loads(extracted_data)
                display_parsed_resume(json_data)


else:
    st.error("❌ Please enter a valid Gemini API key to enable PDF upload.")

