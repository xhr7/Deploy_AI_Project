import os
import base64
import streamlit as st

script_dir = os.path.dirname(os.path.abspath(__file__))

st.set_page_config(page_title="غرسة", layout="wide", initial_sidebar_state="collapsed")

# إخفاء عناصر Streamlit
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    section[data-testid="stSidebar"], div[data-testid="collapsedControl"] {display: none !important;}
    </style>
""", unsafe_allow_html=True)

# استيراد الخطوط
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Marhey:wght@300;400;500;600;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Scheherazade+New&display=swap');
    </style>
""", unsafe_allow_html=True)

# شعار غرسة
logo_path = os.path.join(script_dir,"images",  "Logo.png")
with open(logo_path, "rb") as f:
    logo_base64 = base64.b64encode(f.read()).decode()
st.markdown(f"""
    <div style="text-align: right;">
        <img src="data:image/png;base64,{logo_base64}" style="height: 120px;">
    </div>
""", unsafe_allow_html=True)

# شريط تنقل بتصميمك الجميل، لكن باستخدام st.page_link()
st.markdown("""
    <style>
    .custom-navbar {
        display: flex;
        justify-content: center;
        gap: 40px;
        background-color: rgba(255,255,255,0.8);
        padding: 15px;
        font-family: 'Marhey', sans-serif;
        font-size: 22px;
        direction: rtl;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="custom-navbar">', unsafe_allow_html=True)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.page_link("Pages/Plants_info.py", label="تعرف على النباتات")
    with col2:
        st.page_link("Pages/what_is_the_plant.py", label="ماهي نبتتي؟")
    with col3:
        st.page_link("Pages/Plant_your_plant.py", label="ازرع نبتتك")
    with col4:
        st.page_link("Pages/Check_your_plant.py", label="افحص نبتتك")
    with col5:
        st.page_link("Pages/Team_members.py", label="الأعضاء")
    st.markdown('</div>', unsafe_allow_html=True)