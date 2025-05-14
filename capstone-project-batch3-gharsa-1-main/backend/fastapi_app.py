from fastapi import FastAPI, UploadFile, File, Query
from fastapi.middleware.cors import CORSMiddleware
from tensorflow.keras.models import load_model
import tensorflow as tf
from fastapi.responses import StreamingResponse, JSONResponse
import joblib
import cv2
import numpy as np
import base64
import os
import torch
from PIL import Image
from torchvision import transforms




app = FastAPI()

# CORS for Streamlit access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load trained soil classification Keras model 
model_soil = load_model("backend\models\efficientnet_model_soils2.keras")

# MLP disease detection model
model_mlp = joblib.load('backend\models\81_R01235mlp_model.pkl')
scaler = joblib.load('backend\models\scaler.pkl')

img_size = (224, 224)

# Your class names manually listed or loaded
class_names_soil = ['Alluvial soil', 'Black Soil', 'Clay soil', 'Red soil', 'loam', 'sandy']


class_names_mlp = {
    4: "Gall Midge",
    6: "Powdery Mildew",
    7: "Sooty Mould",
    8: "rot",
    9: "burn"
}

# Function to convert RGB to hue
def rgb_to_hue(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB).astype(np.float32) / 255.0
    r, g, b = cv2.split(image)
    num = 0.5 * ((r - g) + (r - b))
    den = np.sqrt((r - g)**2 + (r - b)*(g - b)) + 1e-6
    theta = np.arccos(num / den)
    h = np.where(b > g, 2 * np.pi - theta, theta) / (2 * np.pi)
    return h

# Function to mask green pixels in the hue image
def mask_green_pixels(hue_image):
    green_mask = (hue_image > 0.25) & (hue_image < 0.45)
    return np.where(green_mask, 0, hue_image)

# Function to extract features from an image
def extract_features(image):
    hue = rgb_to_hue(image)
    masked = mask_green_pixels(hue)
    binary = np.where(masked > 0, 1, 0).astype(np.uint8)

    infected_ratio = binary.sum() / binary.size
    infected_hues = hue[binary == 1]
    mean_hue = infected_hues.mean() if infected_hues.size > 0 else 0
    std_hue = infected_hues.std() if infected_hues.size > 0 else 0

    edges = cv2.Canny((binary * 255).astype(np.uint8), 100, 200)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    perimeter = sum(cv2.arcLength(cnt, True) for cnt in contours)
    num_contours = len(contours)

    return [infected_ratio, perimeter, mean_hue, std_hue, num_contours]






dinov2 = torch.hub.load('facebookresearch/dinov2', 'dinov2_vits14').eval()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
dinov2 = dinov2.to(device)

clf_plant = joblib.load("backend\models\plant_identifier_SVM_model.pkl")
le_plant = joblib.load("backend\models\plant_label_encoder.pkl")


transform_dino = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])


def extract_dino_embedding(image_np: np.ndarray) -> np.ndarray:
    """
    Takes a NumPy image (BGR - OpenCV format),
    converts to PIL, transforms it, feeds to DINOv2, and returns embedding.
    """
    image_rgb = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)
    image_pil = Image.fromarray(image_rgb)

    tensor = transform_dino(image_pil).unsqueeze(0).to(device)

    with torch.no_grad():
        embedding = dinov2(tensor).squeeze().cpu().numpy().reshape(1, -1)

    return embedding



@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    img = tf.image.decode_image(contents, channels=3)
    img = tf.image.resize(img, img_size)
    img = tf.keras.applications.efficientnet.preprocess_input(img)
    img = tf.expand_dims(img, 0)

    preds = model_soil.predict(img)
    class_index = int(np.argmax(preds))
    class_name = class_names_soil[class_index]
    confidence = float(np.max(preds))

    return {"class": class_name, "confidence": confidence}



@app.post("/detect")
async def detect(file: UploadFile = File(...)):

    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    photo = cv2.imdecode(nparr, cv2.IMREAD_COLOR)


    features = extract_features(photo)
    if features is not None:
        features_scaled = scaler.transform([features])
        prediction = model_mlp.predict(features_scaled)[0]
        predicted_class = class_names_mlp.get(prediction, "Unknown")

    
        return JSONResponse({
            "class": predicted_class
        })
    else:
        return JSONResponse({"error": "Failed to process image"}, status_code=400)

@app.post("/recognize")
async def recognize(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        embedding = extract_dino_embedding(image)

        pred = clf_plant.predict(embedding)[0]
        class_name = le_plant.inverse_transform([pred])[0]

        return JSONResponse({
            "class": class_name
        })
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)