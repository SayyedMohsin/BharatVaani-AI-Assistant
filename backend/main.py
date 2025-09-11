from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY", "AIzaSyD4x0YOurGeminiKey"))
model = genai.GenerativeModel("gemini-1.5-flash")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class AskRequest(BaseModel):
    text: str
    language: str = "hindi"

@app.post("/api/ask")
def ask_ai(req: AskRequest):
    prompt = f"भारतीय संदर्भ में {req.language} में छोटा जवाब दो: {req.text}"
    try:
        response = model.generate_content(prompt)
        return {"answer": response.text.strip()}
    except Exception as e:
        return {"answer": f"AI Error: {str(e)}"}