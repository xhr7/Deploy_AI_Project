import os
import streamlit as st
import base64

script_dir = os.path.dirname(os.path.abspath(__file__))

st.set_page_config(page_title="تعرف على النباتات", layout="wide")

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

hide_sidebar_style = """
    <style>
    section[data-testid="stSidebar"] {display: none !important;}
    div[data-testid="collapsedControl"] {display: none !important;}
    </style>
"""
st.markdown(hide_sidebar_style, unsafe_allow_html=True)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Marhey:wght@300;400;500;600;700&display=swap');
    </style>
""", unsafe_allow_html=True)
logo_path = os.path.join(script_dir, "..","images", "Logo.png")
with open(logo_path, "rb") as image_file:
    logo_base64 = base64.b64encode(image_file.read()).decode()

st.markdown(f"""
    <div style="text-align: right; padding: 10px 10px 0 0;">
        <img src="data:image/png+xml;base64,{logo_base64}" alt="Logo" style="height: 120px;">
    </div>
""", unsafe_allow_html=True)


# Navigation bar 
st.markdown("""
    <style>
    .navbar {
        display: flex;
        justify-content: center;
        align-items: center;
        position: sticky;
        top: -20px;
        gap: 40px;
        z-index: 1000;
        padding: 15px 10%;
        font-family: 'Marhey', sans-serif;
        font-size: 22px;
        direction: rtl;
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .navbar a {
        text-decoration: none;
        font-weight: light;
        color: #333;
        transition: 0.3s ease;
        padding: 8px 15px;
        border-radius: 6px;
    }
    .navbar a:hover {
        color: #8b5e3c;
        background-color: rgba(139, 94, 60, 0.1);
    }
    .active-nav {
        color: #8b5e3c !important;
        border-bottom: 2px solid #8b5e3c;
    }
    </style>
    
    <div class="navbar">
        <a href="/Gharsa" target="_self" >الرئيسية</a>
        <a href="/Plants_info" target="_self" class="active-nav">تعرف على النباتات</a>
        <a href="/what_is_the_plant" target="_self">ماهي نبتتي؟</a>
        <a href="/Plant_your_plant" target="_self">ازرع نبتتك</a>
        <a href="/Check_your_plant" target="_self">افحص نبتتك</a>
        <a href="/Team_members" target="_self">الأعضاء</a>
    </div>
""", unsafe_allow_html=True)


background_image_path = os.path.join(script_dir, "..","images", "Background.png")


with open(background_image_path, "rb") as f:
    bg_base64 = base64.b64encode(f.read()).decode()


style = f"""
    <style>

    .stApp {{
        background-image: url("data:image/png;base64,{bg_base64}");
        background-size: cover;
        background-repeat: repeat;
        background-position: center;
        background-attachment: fixed;
        font-family: 'Marhey', sans-serif;
        color: #222;
    }}
    .section-title {{
        font-size: 42px;
        margin: 60px 0 20px;
        text-align: right;
        padding-right: 60px;
        font-family: 'Marhey', sans-serif;
    }}
    .plant-box {{
        background-color: rgba(255,255,255,0.8);
        padding: 20px;
        border-radius: 12px;
        margin: 20px;
        font-family: 'Marhey', sans-serif;
    }}
    </style>
"""
st.markdown(style, unsafe_allow_html=True)

plant_icon_path = os.path.join(script_dir, "..","images", "explore_plants.png")
with open(plant_icon_path, "rb") as f:
    plant_icon_base64 = base64.b64encode(f.read()).decode()

st.markdown(f"""
    <div style="display: flex; align-items: center; gap: 15px; justify-content: center; direction: rtl; ">
        <div style="font-family: 'Marhey', sans-serif; font-size: 60px; color: #4d0d0d; ">
تعرف على النباتات
                    </div>
        <img src="data:image/png;base64,{plant_icon_base64}" style="height: 100px;">
    </div>
""", unsafe_allow_html=True)
st.markdown("<div class='section-title'>اشهر النباتات الداخلية</div>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown("""<div class='plant-box'>
     <b>سانسيفيريا</b><br>نبتة تتحمل قلة الإضاءة والماء، ممتازة للمبتدئين.
    </div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""<div class='plant-box'>
     <b>بوتس</b><br>نموها سريع وتناسب الأماكن الداخلية ذات الإضاءة المتوسطة.
    </div>""", unsafe_allow_html=True)

st.markdown("<div class='section-title'>اشهر النباتات الخارجية</div>", unsafe_allow_html=True)
col3, col4 = st.columns(2)
with col3:
    st.markdown("""<div class='plant-box'>
     <b>الجهنمية</b><br>مزهره وتتحمل حرارة الشمس، ممتازة للأسوار والبلكونات.
    </div>""", unsafe_allow_html=True)
with col4:
    st.markdown("""<div class='plant-box'>
     <b>الفيكس نيتدا</b><br>شجرة ظل دائمة الخضرة وتتحمل القص والتشكيل.
    </div>""", unsafe_allow_html=True)


