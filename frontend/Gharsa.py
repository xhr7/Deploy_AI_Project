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

# عرض الشعار
st.markdown(f"""
    <div style="text-align:right; margin-bottom:-30px">
        <img src="data:image/png;base64,{logo_base64}" style="height: 100px;">
    </div>
""", unsafe_allow_html=True)

# التنقل في الشريط الجانبي
st.sidebar.markdown("## 🚀 قائمة الصفحات")
st.sidebar.page_link("Gharsa.py", label="🏠 الرئيسية")
st.sidebar.page_link("pages/what_is_the_plant.py", label="🔍 ماهي نبتتي؟")
st.sidebar.page_link("pages/check_your_plant.py", label="🪴 افحص نبتتك")
st.sidebar.page_link("pages/plant_your_plant.py", label="🌱 ازرع نبتتك")

# محتوى ترحيبي
st.markdown("<h1 style='text-align:center; color:#4d0d0d;'>🌿 أهلاً بك في غرسة</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:22px;'>منصة زراعية تساعدك على التعرف على نباتاتك، والعناية بها بكل سهولة</p>", unsafe_allow_html=True)