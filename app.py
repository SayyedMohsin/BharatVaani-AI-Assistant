# app.py
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# 🔐 Gemini
load_dotenv()
api_key = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# 🎨 Same gradient + glass UI (your React colours)
st.set_page_config(page_title="BharatVaani AI", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@400;700&display=swap');
  .main {background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%);}
  .hindi {font-family: 'Noto Sans Devanagari', sans-serif;}
  .glass {
    background: rgba(255,255,255,0.25);
    border-radius: 20px;
    padding: 2rem;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
  }
  .stButton > button {
    width: 100%;
    border-radius: 12px;
    border: none;
    padding: 0.75rem 1.5rem;
    background: linear-gradient(45deg, #FF416C, #FF4B2B);
    color: white;
    font-weight: 700;
    transition: 0.3s;
  }
  .stButton > button:hover {transform: scale(1.05);}
</style>
""", unsafe_allow_html=True)

# -------------------- HEADER (same as React) --------------------
st.markdown("<h1 class='hindi' style='text-align:center;color:white;'>🇮🇳 BharatVaani AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='hindi' style='text-align:center;color:white;'>२२ भारतीय भाषाओं में तुरंत जवाब</p>", unsafe_allow_html=True)

# -------------------- SIDEBAR (same languages) --------------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3612/3612134.png", width=120)
    st.markdown("### ⚙️ Settings")
    languages = {
        "hi": "हिन्दी", "bn": "বাংলা", "te": "తెలుగు", "ta": "தமிழ்",
        "mr": "मराठी", "ur": "اردو", "gu": "ગુજરાતી", "kn": "ಕನ್ನಡ",
        "ml": "മലയാളം", "or": "ଓଡ଼ିଆ", "pa": "ਪੰਜਾਬੀ", "as": "অসমীয়া",
        "sa": "संस्कृत", "bh": "भोजपुरी", "kok": "कोंकणी", "mai": "मैथिली",
        "en": "English", "ne": "नेपाली", "sd": "सिंधी", "sat": "संताली"
    }
    lang = st.selectbox("🌍 Language", list(languages.keys()), format_func=lambda x: f"{x.upper()} - {languages[x]}")

# -------------------- MAIN AREA (same card) --------------------
with st.container():
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    query = st.text_area("✍️ Ask something / सवाल लिखें", placeholder="जैसे: आज मौसम कैसा है?", label_visibility="collapsed")
    col1, col2 = st.columns([3, 1])
    with col2:
        ask = st.button("▶️ पूछें / Ask")

    if ask and query.strip():
        with st.spinner("सोच रहा है..."):
            prompt = f"भारतीय संदर्भ में {languages[lang]} में छोटा जवाब दो: {query}"
            try:
                response = model.generate_content(prompt)
                answer = response.text.strip()
                if answer:
                    st.success(answer)
                else:
                    st.info("AI ने खाली जवाब दिया, फिर से कोशिश करें।")
            except Exception as e:
                st.error(f"AI Error: {e}")
    elif ask:
        st.warning("कृपया कोई सवाल लिखें")
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------- FOOTER (same) --------------------
st.markdown("---")
st.markdown("<p style='text-align:center;color:grey;'>Made with ❤️ by Sayyed Mohsin Ali</p>", unsafe_allow_html=True)
