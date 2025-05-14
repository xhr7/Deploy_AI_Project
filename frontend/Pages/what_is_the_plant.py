import requests
import streamlit as st
import base64
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
st.set_page_config(page_title="ماهي نبتتي؟", layout="wide")



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
    @import url('https://fonts.googleapis.com/css2?family=Scheherazade+New&display=swap');

    </style>
""", unsafe_allow_html=True) 

logo_path = os.path.join(script_dir, "..","images", "Logo.png")
with open(logo_path, "rb") as image_file:
    logo_base64 = base64.b64encode(image_file.read()).decode()

st.markdown(f"""
    <div style="text-align: right; padding: 0px 0px 0 0;">
        <img src="data:image/png+xml;base64,{logo_base64}" alt="Logo" style="height: 120px; margin-left: auto;">
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
        <a href="/Plants_info" target="_self">تعرف على النباتات</a>
        <a href="/what_is_the_plant" target="_self" class="active-nav">ماهي نبتتي؟</a>
        <a href="/Plant_your_plant" target="_self">ازرع نبتتك</a>
        <a href="/Check_your_plant" target="_self">افحص نبتتك</a>
        <a href="/Team_members" target="_self">الأعضاء</a>
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
        background-attachment: fixed;
        font-family: 'Marhey', sans-serif;
        color: #222;
    }}
    
    .custom-text {{
        font-family: 'Scheherazade New', sans-serif;
        font-size: 22px;
        text-align: center;
        margin: 30px 60px;
        line-height: 2;
        direction: rtl;
        color: #333;
        background-color: rgba(255,255,255,0.7);
        padding: 20px;
        border-radius: 15px;
    }}
    .custom-subtitle {{
        font-family: 'Marhey', sans-serif;
        font-size: 35px;
        text-align: center;
        margin-top: 50px;
        mergin-bottom: 20px;
        color: #4d0d0d;
    }}
    .custom-title {{
        font-family: 'Marhey', sans-serif;
        font-size: 100px;
        text-align: right;
        margin-top: 40px;
        direction: rtl;
        color: #4d0d0d;
    }}
    .soil-type-card {{
        font-family: 'Marhey', sans-serif;
        background-color: rgba(255,255,255,0.8);
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 40px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }}
    </style>
    """
st.markdown(style, unsafe_allow_html=True)





plant_icon_path = os.path.join(script_dir, "..","images", "identify_plant.png")
with open(plant_icon_path, "rb") as f:
    plant_icon_base64 = base64.b64encode(f.read()).decode()

st.markdown(f"""
    <div style="display: flex; align-items: center; gap: 15px; justify-content: center; direction: rtl; ">
        <div style="font-family: 'Marhey', sans-serif; font-size: 60px; color: #4d0d0d; ">
        ماهي نبتتي؟ 
        </div>
        <img src="data:image/png;base64,{plant_icon_base64}" style="height: 100px;">
    </div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='custom-text'>
    <div style="text-align: center; font-size: 22px; font-family: 'Marhey', sans-serif; color: #4d0d0d; font-weight: bold;">
        تعرف على نبتتك من خلال صورة فقط!
    </div>
    <div style="text-align: center; font-size: 18px; font-family: 'Scheherazade New', sans-serif; color: #333; font-weight: bold;">
        ما عليك إلا ترفع صورة واضحة لنبتتك، ونساعدك نحدد اسمها ونوعها وطريقة العناية المناسبة لها. <br>
    </div>
</div>

""", unsafe_allow_html=True)

check_icon_path = os.path.join(script_dir, "..", "images", "what_is_the_plant.png")
with open(check_icon_path, "rb") as f:
    check_icon_base64 = base64.b64encode(f.read()).decode()

st.markdown(f"""
    <div style="display: flex; align-items: center; gap: 15px; justify-content: center; direction: rtl; margin-top: 50px;">
        <div style="font-family: 'Marhey', sans-serif; font-size: 35px; color: #4d0d0d;">
            تعرف على نبتتك
        </div>
        <img src="data:image/png;base64,{check_icon_base64}" style="height: 100px;">
    </div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='custom-text'>
لمساعدتك في التعرف على نبتتك  يمكنك اتباع الخطوات التالية:   
                   
1- ا         بإمكانك تصوير نبتتك كاملة أو جزء منها    2-التقط صورة واضحة         3- ارفع الصورة أدناه للتحليل
</div>
""", unsafe_allow_html=True)



st.markdown("""
<style>
/* نخلي محتوى summary عمودي وبالنص */
summary.st-emotion-cache-4rp1ik {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 6px !important;
}

/* تنسيق النص */
div.st-emotion-cache-wq5ihp.e1icttdg0 > p {
    font-family: 'Scheherazade New', sans-serif !important;
    font-size: 20px !important;
    color: #4d0d0d !important;
    text-align: center !important;
    margin: 0 !important;
}
/* السهم يكون بمحاذاة النص */
summary.st-emotion-cache-4rp1ik svg {
    order: 2 !important;
    margin: 0 !important;
}
</style>
""", unsafe_allow_html=True)



rejected_image_path = os.path.join(script_dir, "..", "images", "rejected_sample_what.jpg")  
with open(rejected_image_path, "rb") as f:
    rejected_image_base64 = base64.b64encode(f.read()).decode()
accepted_image_path = os.path.join(script_dir, "..", "images", "accepted_sample_what.jpg")
with open(accepted_image_path, "rb") as f:
    accepted_image_base64 = base64.b64encode(f.read()).decode()

with st.expander("إرشادات رفع الصورة", expanded=False):
    st.markdown(f"""
    <div style='
        direction: rtl;
        text-align: center;
        font-family: "Scheherazade New", sans-serif;
        background-color: rgba(255, 255, 255, 0.7);
        padding: 20px;
        border-radius: 15px;
        margin-top: 10px;
    '>
        <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 30px;'>
            <!-- ✅ الصور المقبولة -->
            <div>
                <h4 style="color: green;">✅ الصور المقبولة:</h4>
                <ul style="line-height: 2;">
                    <li>صور واضحة للنبتة أو الورقة بدون تشويش</li>
                    <li>الإضاءة طبيعية وموزعة بدون ظل</li>
                    <li>الصورة ملوّنة وعالية الدقة</li>
                </ul>
                <img src="data:image/jpeg;base64,{accepted_image_base64}" style="width: 50%; border-radius: 10px; margin-top: 10px;">
            </div>
            <div>
                <h4 style="color: crimson;">❌ الصور غير المقبولة:</h4>
                <ul style="line-height: 2;">
                    <li>صور فيها ظل يغطي جزء من النبتة</li>
                    <li>صور النباتات من بعيد أو بدون أوراق ظاهرة</li>
                    <li>صور مقصوصة أو مشوهة أو ضبابية</li>
                </ul>
                <img src="data:image/jpeg;base64,{rejected_image_base64}" style="width: 50%; border-radius: 10px; margin-top: 10px;">
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)



# رفع الصورة
uploaded_file = st.file_uploader("اختر صورة للنبتة", type=["jpg", "jpeg", "png"], label_visibility="collapsed",  key="custom_uploader")
st.markdown("""
    <style>
    [data-testid="stFileUploader"] {
        display: flex;
        justify-content: center;
        font-family: 'Scheherazade New', sans-serif;
    }

    [data-testid="stFileUploader"] > div {
        max-width: 500px;
        width: 95%;
    }

    button[kind="primary"] {
        background-color: #8b5e3c !important;
        color: white !important;
        font-size: 20px !important;
        padding: 12px 26px !important;
        border-radius: 10px !important;
        font-family: 'Marhey', sans-serif !important;
    }
    </style>
""", unsafe_allow_html=True)

if uploaded_file:
    file_bytes = uploaded_file.getvalue()
    img_base64 = base64.b64encode(file_bytes).decode()

    st.markdown(f"""
        <div style="text-align: center;">
          <img src="data:image/jpeg;base64,{img_base64}"
            style="width: 250px; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.2);" />
        <p style="font-family: 'Scheherazade New'; font-size: 16px;">🖼️ الصورة المرفوعة</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <style>
        div.stButton > button {
            background-color: #8b5e3c !important;
            color: white !important;
            font-size: 22px !important;
            font-weight: bold !important;
            padding: 16px 36px !important;
            border-radius: 12px !important;
            font-family: 'Marhey', sans-serif !important;
            border-color: #FFFF !important;
            border-width: 2px !important;
            border-style: solid !important;
            display: block;
            margin: 30px auto;
        }
        </style>
    """, unsafe_allow_html=True)

    analyze_clicked = st.button("🔍 تعرف على النبتة ", key="analyze_btn")

    if analyze_clicked:
        with st.spinner("جاري التعرف..."):
            try:
                file_bytes = uploaded_file.getvalue()

                response = requests.post(
                    "https://multimedia-armed-initiatives-yorkshire.trycloudflare.com/recognize",
                    files={"file": file_bytes}
                )
                response.raise_for_status()
                data = response.json()
                class_name = data.get("class", "غير معروفة")

        
                class_translation = {
                    "fiddle_leaf": "نبتة التين الورقي",
                    "mint": "النعناع",
                    "Chamaedorea elegans": "شاميدوريا إليغانس",
                    "aloe_vera": "الألوفيرا",
                    "Dracaena": "الدراسينا",
                    "snake_plant": "نبتة الثعبان",
                    "schismatoglottis": "شيزماتوجلوتس",
                    "Parsley": "البقدونس",
                    "Cilantro": "الكزبرة",
                    "pothos": "نبتة البوتس",
                    "Sansevieria trifasciata ‘Golden Hahnii’": "سانسيفيريا الذهبية القصيرة"
                }

                class_name_ar = class_translation.get(class_name, "غير معروفة")


                st.markdown(f"""
                    <div style = 'text-align:center;'>
                        <h3> اسم النبتة: <b>{class_name_ar}</b></h3>
                    </div>
                """, unsafe_allow_html=True)

            except Exception as e:
                st.error("❌ لم يتم الاتصال بـ FastAPI أو حدث خطأ.")
                st.exception(e)