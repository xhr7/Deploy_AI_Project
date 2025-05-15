import streamlit as st
import base64
import os

st.set_page_config(page_title="اعضاء غرسة", layout="wide")

# Hide Streamlit elements
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    section[data-testid="stSidebar"], div[data-testid="collapsedControl"] {display: none !important;}
    </style>
""", unsafe_allow_html=True)

# Load Logo
script_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(script_dir, "..", "images", "Logo.png")
with open(logo_path, "rb") as image_file:
    logo_base64 = base64.b64encode(image_file.read()).decode()

st.markdown(f"""
    <div style="text-align: right;">
        <img src="data:image/png;base64,{logo_base64}" alt="Logo" style="height: 120px;">
    </div>
""", unsafe_allow_html=True)


with open("frontend/images/Background.png", "rb") as f:
    bg_bytes = f.read()
bg_base64 = base64.b64encode(bg_bytes).decode()

style = f"""
<style>

.stApp {{
    background-image: url("data:image/png;base64,{bg_base64}");
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    font-family: 'Marhey', sans-serif;
    color: #222;
}}
.custom-text {{
    font-family: 'Marhey', sans-serif;
    font-size: 32px;
    text-align: center;
    margin: 40px 60px;
    line-height: 2;
}}
.custom-subtitle {{
    font-family: 'Marhey', sans-serif;
    font-size: 50px;
    text-align: center;
    margin-top: 40px;
}}
</style>
"""
st.markdown(style, unsafe_allow_html=True)


# Navbar
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Marhey:wght@300;400;500;600;700&display=swap');
    .navbar {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 40px;
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
        color: #333;
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
        <a href="/Plants_info" target="_self">تعرف على النباتات</a>
        <a href="/what_is_the_plant" target="_self">ماهي نبتتي؟</a>
        <a href="/Plant_your_plant" target="_self">ازرع نبتتك</a>
        <a href="/Check_your_plant" target="_self">افحص نبتتك</a>
        <a href="/Team_members" target="_self" class="active-nav">الأعضاء</a>
    </div>
""", unsafe_allow_html=True)


st.markdown('<h1 style="text-align:center; font-family:Marhey; color:#8b5e3c;"> فريق غرسة</h1>', unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center; font-family:Marhey; font-size:20px; color:#333; margin-bottom:20px;">
    كانت بذرة فنمَت بنقاشنا، وسُقيت بعملنا، وأثمرت بتعاوننا
</div>
<div style="text-align:center; font-family:Marhey; font-size:20px; color:#333;">
    :وهؤلاء من كانوا جزءًا من رحلتها
</div>
""", unsafe_allow_html=True)


st.markdown("""
<style>
.profile-card {
    background-color: white;
    border-radius: 15px;
    padding: 20px;
    text-align: center;
    font-family: 'Marhey', sans-serif;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    direction: rtl;
}
.profile-image {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    object-fit: cover;
    margin-bottom: 15px;
    border: 2px solid #8b5e3c;
}
.member-name {
    color: #8b5e3c;
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 5px;
}
.linkedin-button {
    background-color: #f5f5f5;
    color: #0077b5;
    padding: 8px 15px;
    border-radius: 30px;
    text-decoration: none !important;
    font-size: 14px;
    display: inline-block;
    margin-top: 10px;
    transition: background-color 0.3s;
}
.linkedin-button:hover {
    background-color: #e5e5e5;
    text-decoration: none !important;

}
</style>
""", unsafe_allow_html=True)

import base64

def load_image_as_base64(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()



# Team data 
team_members = [
    {
    "name": "رهف مسملي",
    "linkedin": "https://www.linkedin.com/in/rahaf-masmali/",
    "photo_base64": load_image_as_base64("frontend/images/girl.png")
},
    {"name": "مجد العتيبي", "linkedin": "https://www.linkedin.com/in/majd-abdullah-/" , "photo_base64": load_image_as_base64("frontend/images/girl.png")},
    {"name": "نجلاء المرشدي", "linkedin": "https://www.linkedin.com/in/najlayasm/" , "photo_base64": load_image_as_base64("frontend/images/girl.png")},
    {"name": "عبدالعزيز آل فريان", "linkedin": "https://www.linkedin.com/in/aziizdev/", "photo_base64": load_image_as_base64("frontend/images/boy.png")},
    {"name": "عبدالله الزهراني", "linkedin": "http://www.linkedin.com/in/a-a-alzahrani", "photo_base64": load_image_as_base64("frontend/images/boy.png")}
]


cols = st.columns(len(team_members))
for i, member in enumerate(team_members):
    with cols[i]:
        st.markdown(f"""
            <div class="profile-card">
                <img src="data:image/png;base64,{member['photo_base64']}" class="profile-image" alt="{member['name']}">
                <div class="member-name">{member['name']}</div>
                <a href="{member['linkedin']}" target="_blank " class="linkedin-button" style="text-decoration: none !important;">
                    LinkedIn
                    <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" width="16" height="16">
                </a>
            </div>
        """, unsafe_allow_html=True)
