import os
import base64
import streamlit as st


script_dir = os.path.dirname(os.path.abspath(__file__))


st.set_page_config(page_title="غرسة", layout="wide", initial_sidebar_state="collapsed")


# st.markdown("""
#     <style>
#     MainMenu, footer, header {visibility: hidden;}
#     section[data-testid="stSidebar"], div[data-testid="collapsedControl"] {display: none !important;}
#     </style>
# """, unsafe_allow_html=True)


st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Marhey:wght@300;400;500;600;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Scheherazade+New&display=swap');
    

    </style>
""", unsafe_allow_html=True)


logo_path = os.path.join(script_dir, "images", "Logo.png")
with open(logo_path, "rb") as f:
    logo_base64 = base64.b64encode(f.read()).decode()
st.markdown(f"""
    <div style="text-align: right;">
        <img src="data:image/png;base64,{logo_base64}" style="height: 120px;">
    </div>
""", unsafe_allow_html=True)

welcome_icon_path = os.path.join(script_dir, "images", "welcome_icon.png")
with open(welcome_icon_path, "rb") as f:
    welcome_icon_base64 = base64.b64encode(f.read()).decode()

st.markdown("""
    <style>
    .navbar {
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
    }
    .navbar a {
        text-decoration: none;
        color: #333;
        padding: 8px 15px;
        border-radius: 6px;
    }
    .navbar a:hover {
        background-color: rgba(139,94,60,0.1);
        color: #8b5e3c;
    }
    .active-nav {
        color: #8b5e3c !important;
        border-bottom: 2px solid #8b5e3c;
    }
    </style>
    <div class="navbar">
        <a href="/Gharsa" target="_self" class="active-nav">الرئيسية</a>
        <a href="/Plants_info" target="_self">تعرف على النباتات</a>
        <a href="/what_is_the_plant" target="_self">ماهي نبتتي؟</a>
        <a href="/Plant_your_plant" target="_self">ازرع نبتتك</a>
        <a href="/Check_your_plant" target="_self">افحص نبتتك</a>
        <a href="/Team_members" target="_self">الأعضاء</a>
    </div>
""", unsafe_allow_html=True)

icons = {
    "detect": "detect_plant.png",
    "plant": "plant_guide.png",
    "identify": "identify_plant.png",
    "explore": "explore_plants.png"
}
icon_base64 = {}
for key, file in icons.items():
    with open(os.path.join(script_dir,"images", file), "rb") as f:
        icon_base64[key] = base64.b64encode(f.read()).decode()
        
bg_path = os.path.join(script_dir, "images", "background.png")
with open(bg_path, "rb") as f:
    bg_base64 = base64.b64encode(f.read()).decode()

st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bg_base64}");
        background-size: cover;
        background-attachment: fixed;
        font-family: 'Cairo', sans-serif;
        color: #222;
    }}
    </style>
""", unsafe_allow_html=True)


video_path = os.path.join(script_dir, "videos", "pre_final_video.mp4")
if os.path.exists(video_path):
    with open(video_path, "rb") as f:
        video_bytes = f.read()
    video_base64 = base64.b64encode(video_bytes).decode()

    st.markdown(f"""
        <style>
        .hero-box {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: rgba(255, 255, 255, 0.85);
            border-radius: 20px;
            padding: 30px;
            margin: 30px 40px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            gap: 30px;
            direction: rtl;
        }}
        .hero-text {{
            flex: 1.2;
            font-family: 'Marhey', sans-serif;
            font-size: 24px;
            color: #333;
            text-align: center;
            line-height: 1.8;
        }}
        .hero-title {{
            font-size: 45px;
            color: #8b5e3c;
            margin-bottom: 20px;
            text-align: center;
            margin-right: 90px;
        }}
        .hero-video {{
            flex: 1;
        }}
        video {{
            width: 100%;
            border-radius: 15px;
            box-shadow: 0 6px 20px rgba(0,0,0,0.1);
        }}
        </style>
        <div class="hero-box">
            <div class="hero-video">
                <video controls>
                    <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
                    متصفحك لا يدعم عرض الفيديو.
                </video>
            </div>
            <div class="hero-text">
                  <div class="hero-title" style="display: flex; align-items: center; direction: rtl;">
                    مرحبًا بك في غرسة
                  <img src="data:image/png;base64,{welcome_icon_base64}" style="height: 150px;">
                  </div>
                منصة متكاملة لعشاق النباتات والزراعة<br>
                <span style="text-align:center;">تعلّم، اكتشف، وازرع وابدأ رحلتك نحو عالم أخضر مليء بالإلهام والمعرفة </span>
            </div>


        </div>
    """, unsafe_allow_html=True)
else:
    st.warning("لم يتم العثور على الفيديو.", icon="⚠️")


st.markdown('<div class="custom-subtitle">:قال رسول الله ﷺ</div>', unsafe_allow_html=True)
st.markdown('<div class="custom-text">(ما من مسلمٍ يغرسُ غرساً أو يزرعُ زرعاً فيأكلُ منه طيرٌ أو إنسانٌ أو بهيمةٌ إلاَّ كان له به صدقة)</div>', unsafe_allow_html=True)

st.markdown('<div class="custom-subsubtitle">:أبرز خدمات غرسة</div>', unsafe_allow_html=True)

st.markdown("""
    <style>
    .feature-section {
        display: flex;
        justify-content: space-around;
        margin: 40px 10%;
        gap: 20px;
        # flex-wrap: wrap;
    }
    .feature-card {
        background-color: rgba(255,255,255,0.9);
        border-radius: 15px;
        padding: 25px;
        width: 250px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
        text-align: center;
    }
    .feature-card:hover {
        transform: translateY(-10px);
    }
    .feature-icon {
        font-size: 50px;
        color: #8b5e3c;
        margin-bottom: 10px;
    }
    .feature-title {
        font-family: 'Marhey', sans-serif;
        font-size: 22px;
        color: #8b5e3c;
        font-weight: bold;
    }
    .feature-description {
        font-size: 16px;
        color: #444;
        font-family: 'Scheherazade New', sans-serif;
    }
    .custom-subtitle {
        font-family: 'Marhey', sans-serif;
        font-size: 36px;
        color: #8b5e3c;
        margin: 10px 20px 3px 10px;
        text-align: right;
        font-weight: bold;
    }
    .custom-subsubtitle {
        font-family: 'Marhey', sans-serif;
        font-size: 36px;
        color: #8b5e3c;
        margin: 10px 20px 3px 10px;
        text-align: right;
        font-weight: bold;
        text-position: center;
        text-align: center;
    }
    .custom-text {
        font-family: 'Scheherazade New', sans-serif;
        font-size: 32px;
        text-align: right;
        margin: 20px;
        line-height: 2;
        position: center;
    }
    </style>
""", unsafe_allow_html=True)


st.markdown(f"""
<div class="feature-section">
<a href="/Check_your_plant" target="_self" style="text-decoration: none;">
    <div class="feature-card">
        <div class="feature-icon">
            <img src="data:image/png;base64,{icon_base64['detect']}" style="height: 100px;">
        </div>
        <div class="feature-title">افحص نبتتك</div>
        <div class="feature-description">شخّص حالة نباتك واكتشف الآفات والأمراض بدقة</div>
    </div>
</a>
<a href="/Plant_your_plant" target="_self" style="text-decoration: none;">
    <div class="feature-card">
        <div class="feature-icon">
            <img src="data:image/png;base64,{icon_base64['plant']}" style="height: 100px;">
        </div>
        <div class="feature-title">ازرع نبتتك</div>
        <div class="feature-description">احصل على إرشادات خطوة بخطوة لزراعة نباتاتك المفضلة</div>
    </div>
</a>
<a href="/what_is_the_plant" target="_self" style="text-decoration: none;">
    <div class="feature-card">
        <div class="feature-icon">
            <img src="data:image/png;base64,{icon_base64['identify']}" style="height: 100px;">
        </div>
        <div class="feature-title">ماهي نبتتي؟ </div>
        <div class="feature-description">صوّر نبتتك وتعرّف على اسمها، نوعها، وطريقة العناية بها     </div>
    </div>
</a>
<a href="/Plants_info" target="_self" style="text-decoration: none;">
    <div class="feature-card">
        <div class="feature-icon">
            <img src="data:image/png;base64,{icon_base64['explore']}" style="height: 100px;">
        </div>
        <div class="feature-title">تعرف على النباتات</div>
        <div class="feature-description">استكشف مجموعة واسعة من النباتات</div>
    </div>
</a>
</div>
""", unsafe_allow_html=True)




