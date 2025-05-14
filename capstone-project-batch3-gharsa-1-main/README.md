# Gharsa: AI-Powered Plant Advisor for Home Growers


<p align="center">
  <img src="assets/Logo.png" alt="Gharsa Logo" width="500"/>
</p>



**Gharsa (غرسة)** Is a capstone AI project developed to assist users who are interested in planting at home but lack the experience or knowledge to get started. Through a simple interface and powerful models, Gharsa helps users identify soil types, recognize plants, and detect plant diseases using computer vision techniques.

---

## 📋 Table of Contents

1. [About the Project](#-about-the-project)
2. [Features](#-features)
3. [How It Works](#-how-it-works)
4. [Project Structure](#-project-structure)
5. [Getting Started](#-getting-started)
6. [Technologies Used](#-technologies-used)
7. [Team Members](#-team-members)

---

## 📖 About the Project

Gharsa offers an accessible solution to beginners and home growers who want to:

1. **Know what to plant and how to improve their soil** — by uploading a soil photo, users receive:

   * The soil type.
   * Tips to improve its fertility ("خصوبة").
   * Recommended plants/crops suitable for that soil.

2. **Identify an unknown plant** — by uploading a picture (of a plant found in the street, received as a gift, etc.), the system:

   * Uses **DinoV2** embeddings & **SVM** model to match against a labeled dataset.
   * Returns the plant’s full name, nickname, common uses, possible allergies (if any), and care tips.

3. **Check if their plant is diseased** — by uploading a picture of a single leaf, Gharsa:

   * Detects disease types such as **Midge, Powdery Mildew, Sooty Mould, Rot, and Burns** using advanced CNN-based models.
   * Provides the user with an Arabic diagnosis and helpful care instructions.

---

## ✨ Features

### 🌱 1. Soil Classification & Crop Recommendation

* **Input**: Photo of the soil.
* **Output**: Soil type, tips to improve its fertility, and suitable plants/crops.
* **Model**: CNN (EfficientNet-based) for classification.

### 🌿 2. Plant Identification by Image

* **Input**: Photo of a full plant.
* **Output**: Plant name, nickname, uses, allergies, and care instructions.
* **Model**: DinoV2 to generate image embeddings, then classify.

### 🍂 3. Leaf Disease Detection

* **Input**: Photo of a leaf.
* **Output**: Diagnosis of disease (e.g., rot, burn) with recommendations.
* **Model**: YOLOv8 for detection + post-processing.

---

## 🛠 How It Works

1. **Soil Classification**:

   * User uploads soil image
   * CNN model classifies into one of 6 soil types
   * App returns Arabic label, improvement tips, and crop suggestions

2. **Plant Identification**:

   * User uploads plant image
   * DinoV2 generates an embedding
   * System compares to database to classify plant and return detailed info

3. **Disease Detection**:

   * User uploads a leaf photo
   * YOLOv8 detects diseases
   * If found, app marks location and explains the issue in Arabic

---

## 📂 Project Structure

text
Gharsa/
├── backend/                        # FastAPI backend
│   ├── fastapi_app.py             # Main app with /predict and /detect endpoints
│   ├── models/                    # Trained ML models
│   │   ├── efficientnet_model_soils2.keras
│   │   
│
├── frontend/                      # Streamlit frontend
│   ├── Gharsa.py                  # Landing & navigation
│   ├── Pages/
│   │   ├── أزرع نبتتك.py          # Soil classifier
│   │   ├── أفحص نبتتك.py         # Disease detection
│   │   └── الأعضاء.py            # Team page
│   ├── images/                    # Assets
│   ├── fonts/                     # Arabic font used in UI
│
├── notebooks/                     # Jupyter notebooks for model training/testing
│   └── soil_mAP 85_EfficientNetB0.ipynb

├── README.md                      # Project documentation
├── requirements.txt               # Python packages


---

## 🚀 Getting Started

### Prerequisites

* Python 3.10+
* pip

### Installation

bash
git clone https://github.com/your-repo/gharsa.git
cd gharsa
pip install -r requirements.txt


### Run Backend (FastAPI):

bash
uvicorn backend.fastapi_app:app --reload --port 8000


### Run Frontend (Streamlit):

bash
streamlit run frontend/Gharsa.py


---

## 💻 Technologies Used

* **FastAPI**: Lightweight Python API framework
* **Streamlit**: Interactive UI in Python
* **TensorFlow/Keras**: For CNN-based soil classification
* **PyTorch**: 
* **DinoV2**: For image embedding and plant recognition
* **YOLOv8**: For plant disease detection
* **OpenCV**: Image processing and annotations

---

## 👨‍👩‍👧‍👦 Team Members

* Abdulaziz Alfrayan
* Rahaf Masmali
* Majd Alotaibi
* Abdullah Alzahrani
* Najla Almarshde
