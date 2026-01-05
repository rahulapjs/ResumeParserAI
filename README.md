# ResumeParserAI

A Streamlit-based application that parses resumes (PDF) using Google Gemini AI to generate professional summaries and extract structured data.

## Features
- **PDF Upload**: Upload your resume in PDF format.
- **AI Analysis**: Uses Google Gemini Pro/Flash to analyze the content.
- **Structured Extraction**: Extracts Name, Email, Location, Work Experience, Projects, Skills, and Education.
- **Professional Summary**: Generates an engaging first-person summary.

## Prerequisites
- Docker and Docker Compose installed on your machine.
- A Google Gemini API Key.

## Getting Started

### 1. Clone the repository
```bash
git clone <repository-url>
cd ResumeParserAI
```

### 2. Environment Setup
Create a `.env` file from the example:
```bash
cp .env.example .env
```
Open `.env` and add your Gemini API key:
```
GEMINI_API_KEY=your_actual_api_key_here
```

### 3. Run with Docker Compose
Start the application:
```bash
docker-compose up --build
```
Access the application at `http://localhost:8501`.

### 4. Run Locally (Optional)
If you prefer running without Docker:
```bash
pip install -r requirements.txt
streamlit run main.py
```

## Project Structure
- `main.py`: Main application logic.
- `requirements.txt`: Python dependencies.
- `Dockerfile`: Docker construction instructions.
- `docker-compose.yml`: Container orchestration.
