# app.py
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# 🔐 .env or Streamlit Secrets
load_dotenv()
api_key = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# 🎨 Page Config
st.set_page_config(page_title="BharatVaani AI", layout="centered")
st.title("🇮🇳 BharatVaani AI Assistant")
st.markdown("22 भारतीय भाषाओं में तुरंत जवाब")

# 🌐 Language Selector
languages = {
    "hi": "हिन्दी", "bn": "বাংলা", "te": "తెలుగు", "ta": "தமிழ்",
    "mr": "मराठी", "ur": "اردو", "gu": "ગુજરાતી", "kn": "ಕನ್ನಡ",
    "ml": "മലയാളം", "or": "ଓଡ଼ିଆ", "pa": "ਪੰਜਾਬੀ", "as": "অসমীয়া"
}
lang = st.selectbox("भाषा चुनें / Choose Language", list(languages.keys()), format_func=lambda x: f"{x.upper()} - {languages[x]}")

# 💬 Input
query = st.text_area("सवाल लिखें / Ask something", placeholder="जैसे: आज मौसम कैसा है?")
if st.button("पूछें / Ask"):
    if query.strip():
        with st.spinner("सोच रहा है..."):
            prompt = f"भारतीय संदर्भ में {languages[lang]} में छोटा जवाब दो: {query}"
            try:
                response = model.generate_content(prompt)
                st.success(response.text.strip())
            except Exception as e:
                st.error(f"AI Error: {e}")
    else:
        st.warning("कृपया कोई सवाल लिखें")
