import streamlit as st
import os
import base64

# إعدادات الصفحة
st.set_page_config(page_title="غرسة - الرئيسية", layout="wide")

# إخفاء أشياء ستريملت
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    section[data-testid="stSidebar"], div[data-testid="collapsedControl"] {display: none !important;}
    </style>
""", unsafe_allow_html=True)

# تحميل الشعار
script_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(script_dir, "images", "Logo.png")
with open(logo_path, "rb") as f:
    logo_base64 = base64.b64encode(f.read()).decode()

# شريط التنقل البسيط
st.markdown(f"""
    <style>
    .navbar {{
        display: flex;
        justify-content: center;
        gap: 40px;
        background-color: #ffffffcc;
        padding: 15px;
        font-family: 'Marhey', sans-serif;
        font-size: 22px;
        direction: rtl;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 30px;
    }}
    .navbar a {{
        text-decoration: none;
        color: #333;
        padding: 8px 15px;
        border-radius: 6px;
    }}
    .navbar a:hover {{
        background-color: rgba(139,94,60,0.1);
        color: #8b5e3c;
    }}
    </style>
    <div style="text-align:right; margin-bottom:-30px">
        <img src="data:image/png;base64,{logo_base64}" style="height: 100px;">
    </div>
    <div class="navbar">
        <a href="/">الرئيسية</a>
        <a href="#">ماهي نبتتي؟</a>
        <a href="#">افحص نبتتك</a>
        <a href="#">ازرع نبتتك</a>
    </div>
""", unsafe_allow_html=True)

# خلفية الصفحة
bg_path = os.path.join(script_dir, "images", "Background.png")
with open(bg_path, "rb") as f:
    bg_base64 = base64.b64encode(f.read()).decode()

st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bg_base64}");
        background-size: cover;
        background-attachment: fixed;
        font-family: 'Cairo', sans-serif;
    }}
    </style>
""", unsafe_allow_html=True)

# محتوى ترحيبي
st.markdown("<h1 style='text-align:center; color:#4d0d0d;'>🌿 أهلاً بك في غرسة</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:22px;'>منصة زراعية تساعدك على التعرف على نباتاتك، والعناية بها بكل سهولة</p>", unsafe_allow_html=True)