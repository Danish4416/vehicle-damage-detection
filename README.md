# 🚗 Vehicle Damage Detection App

A deep learning-based web application that detects and classifies vehicle damage from an uploaded image.

The application uses **ResNet50 with Transfer Learning** and classifies vehicles into six categories based on front and rear views.

### 🚀 Live Demo

👉 **[Try the Vehicle Damage Detection App](https://vehicle-damage-detection-1-g3s2.onrender.com)**
---

## 🎯 Project Objective

The objective of this project is to build an end-to-end **Computer Vision and Deep Learning application** that can identify the damage condition of a vehicle from an image.

The model is trained primarily on **third-quarter front and rear views** of vehicles. For better predictions, the uploaded image should capture a similar view of the vehicle.

---

## 🧠 Model Details

* **Architecture:** ResNet50
* **Approach:** Transfer Learning
* **Framework:** PyTorch
* **Input Image Size:** 224 × 224
* **Number of Classes:** 6
* **Dataset Size:** ~1,700 images
* **Validation Accuracy:** ~80%

### Classes

1. Front Normal
2. Front Crushed
3. Front Breakage
4. Rear Normal
5. Rear Crushed
6. Rear Breakage

---

## 🔄 Application Workflow

```text
Upload Vehicle Image
        ↓
Streamlit Frontend
        ↓
FastAPI Backend
        ↓
ResNet50 Model
        ↓
Damage Classification
        ↓
Prediction Result
```

---

## 🛠️ Tech Stack

### Machine Learning / Deep Learning

* Python
* PyTorch
* Torchvision
* ResNet50
* Transfer Learning
* Computer Vision

### Backend

* FastAPI
* Uvicorn

### Frontend

* Streamlit

### Deployment & Version Control

* Render
* Git
* GitHub

---

## 📁 Project Structure

```text
vehicle-damage-detection/
│
├── api/
│   └── server.py
│
├── streamlit_ui/
│   ├── app.py
│   └── requirements.txt
│
├── saved_model.pth
├── source_code.ipynb
├── requirements.txt
├── app_screenshot.jpg
└── README.md
```

---

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/Danish4416/vehicle-damage-detection.git
cd vehicle-damage-detection
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the FastAPI backend

```bash
uvicorn api.server:app --host 0.0.0.0 --port 8000
```

The API will be available at:

```text
http://localhost:8000
```

### 4. Start the Streamlit application

Open another terminal and run:

```bash
cd streamlit_ui
streamlit run app.py
```

The Streamlit application will open in your browser.

---

## 🌐 API

The prediction endpoint is:

```text
POST /predict
```

It accepts a vehicle image and returns the predicted damage category.

Example response:

```json
{
    "prediction": "Front Crushed"
}
```

---

## 📊 Model Performance

The model achieved approximately **80% validation accuracy** across the six target classes.

The project focuses not only on model training but also on building a complete pipeline from:

**Image → Model → API → Web Interface → Deployment**

---

## ⚠️ Important Note

For better prediction accuracy, use images that clearly show the **third-quarter front or rear view** of the vehicle.

Images with unusual angles, heavy cropping, poor lighting, or views significantly different from the training data may result in incorrect predictions.

---

## 🚀 Deployment

The application is deployed on **Render** and consists of:

* **FastAPI** → Model inference API
* **Streamlit** → User interface
* **ResNet50** → Vehicle damage classification model

### 🔗 Live Application

**https://vehicle-damage-detection-1-g3s2.onrender.com**

---

## 📌 Future Improvements

* Increase the size and diversity of the training dataset
* Improve classification accuracy
* Add confidence scores
* Add Grad-CAM visual explanations
* Experiment with lightweight architectures for faster inference
* Improve performance for different vehicle angles and lighting conditions

---

## 👨‍💻 Author

**Danish Ansari**

Machine Learning & Deep Learning enthusiast focused on building practical, end-to-end AI applications.
