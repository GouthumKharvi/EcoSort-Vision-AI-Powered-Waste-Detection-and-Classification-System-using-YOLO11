# ♻️ EcoSort-Vision

## AI-Powered Waste Detection and Classification System using YOLO11, Flask, Docker, AWS, GitHub Actions CI/CD and MLOps

![Python](https://img.shields.io/badge/Python-3.11-blue)
![YOLO11](https://img.shields.io/badge/YOLO11-Ultralytics-green)
![Flask](https://img.shields.io/badge/Flask-Web%20App-black)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![AWS](https://img.shields.io/badge/AWS-Cloud-orange)
![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-success)
![Computer Vision](https://img.shields.io/badge/Computer-Vision-red)

---

# 📌 Project Overview

EcoSort-Vision is an End-to-End Computer Vision and MLOps project developed for intelligent waste detection and classification using YOLO11.

The system automatically identifies and classifies different categories of waste from uploaded images and returns a visual prediction with bounding boxes and class labels.

The project includes:

- Data Ingestion Pipeline
- Data Validation Pipeline
- YOLO11 Training Pipeline
- Flask Web Application
- Docker Containerization
- AWS Deployment
- GitHub Actions CI/CD
- Amazon ECR Integration
- EC2 Deployment
- Real-Time Prediction Interface

The objective of this project is to demonstrate how modern Computer Vision systems can be built, trained, deployed, and maintained using industry-standard MLOps practices.

---

# 🚀 Problem Statement

Manual waste sorting is:

- Time-consuming
- Labor intensive
- Error-prone
- Expensive

Improper waste segregation leads to:

- Increased landfill waste
- Recycling inefficiencies
- Environmental pollution

An intelligent AI system capable of identifying waste categories can improve waste management and automate sorting processes.

---

# 🎯 Solution

EcoSort-Vision leverages:

- YOLO11 Object Detection
- OpenCV
- PyTorch
- Flask
- Docker
- AWS Cloud

to build a complete waste detection platform capable of:

1. Uploading an image
2. Detecting waste objects
3. Classifying waste category
4. Returning annotated output image
5. Deploying automatically through CI/CD pipelines

---

# 📊 Dataset Information

Dataset Source:

Roboflow

Dataset Name:

Garbage Dataset

Total Images:

```text
6075 Images
```

Annotation Format:

```text
YOLO11 Format
```

Number of Classes:

```text
10 Classes
```

Classes:

```text
Battery
Cardboard
Clothes
Glass
Metal
Miscellaneous Trash
Organic
Paper
Plastic
Shoes
```

Dataset Structure:

```text
train/
valid/
test/
data.yaml
```

---

# 🏗️ Project Architecture

```text
                ┌────────────────────┐
                │   Google Drive     │
                └──────────┬─────────┘
                           │
                           ▼
                ┌────────────────────┐
                │ Data Ingestion     │
                └──────────┬─────────┘
                           │
                           ▼
                ┌────────────────────┐
                │ Data Validation    │
                └──────────┬─────────┘
                           │
                           ▼
                ┌────────────────────┐
                │ YOLO11 Training    │
                └──────────┬─────────┘
                           │
                           ▼
                ┌────────────────────┐
                │ best.pt Model      │
                └──────────┬─────────┘
                           │
                           ▼
                ┌────────────────────┐
                │ Flask Application  │
                └──────────┬─────────┘
                           │
                           ▼
                ┌────────────────────┐
                │ Docker Container   │
                └──────────┬─────────┘
                           │
                           ▼
                ┌────────────────────┐
                │ Amazon ECR         │
                └──────────┬─────────┘
                           │
                           ▼
                ┌────────────────────┐
                │ AWS EC2            │
                └────────────────────┘
```

---

# ⚙️ Project Workflow

## 1️⃣ Data Ingestion

The Data Ingestion module:

- Downloads dataset from Google Drive
- Creates artifact directories
- Stores dataset zip file
- Extracts dataset

File:

```text
ecosortvision/components/data_ingestion.py
```

Functions:

```python
download_data()
extract_zip_file()
initiate_data_ingestion()
```

---

## 2️⃣ Data Validation

The Data Validation module validates:

### Directory Validation

Checks existence of:

```text
train/images
train/labels

valid/images
valid/labels

test/images
test/labels
```

### File Validation

Checks:

```text
data.yaml exists
```

### Dataset Consistency Validation

Checks:

```text
Image count == Label count
```

for:

```text
train
valid
test
```

File:

```text
ecosortvision/components/data_validation.py
```

---

## 3️⃣ Model Training

Model training uses:

```text
YOLO11n
```

Pretrained Weights:

```text
yolo11n.pt
```

Training Steps:

1. Unzip dataset
2. Read data.yaml
3. Update class count
4. Create custom YOLO11 configuration
5. Train model
6. Save best.pt
7. Store trained model in artifacts

File:

```text
ecosortvision/components/model_trainer.py
```

---

# 🧠 Model Details

Framework:

```text
Ultralytics YOLO11
```

Backend:

```text
PyTorch
```

Image Size:

```text
640 x 640
```

Training Parameters:

```python
epochs=1
batch=16
```

Pretrained Weights:

```text
yolo11n.pt
```

Output Model:

```text
artifacts/model_trainer/best.pt
```

---

# 📂 Project Structure

```text
EcoSort-Vision
│
├── .github
│   └── workflows
│       └── main.yaml
│
├── artifacts
│   ├── data_ingestion
│   ├── data_validation
│   └── model_trainer
│
├── config
│   └── config.yaml
│
├── data
│   └── inputImage.jpg
│
├── ecosortvision
│
│   ├── components
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── model_trainer.py
│   │   ├── prediction.py
│   │   └── classifier_trainer.py
│
│   ├── constants
│   ├── entity
│   ├── exception
│   ├── logger
│   ├── pipeline
│   └── utils
│
├── flowcharts
│
├── research
│
├── static
│
├── templates
│   └── index.html
│
├── ultralytics
│
├── app.py
├── Dockerfile
├── requirements.txt
├── setup.py
└── README.md
```

---

# 🖥️ Flask Web Application

Routes:

## Home Route

```python
/
```

Returns:

```text
index.html
```

---

## Train Route

```python
/train
```

Triggers:

```text
Complete Training Pipeline
```

---

## Predict Route

```python
/ predict
```

Accepts:

```json
{
  "image":"base64_string"
}
```

Returns:

```json
{
   "image":"prediction_image"
}
```

---

## Live Route

```python
/live
```

Starts webcam inference.

---

# 🎨 Frontend Features

Modern futuristic UI includes:

- Animated Particle Background
- Live Statistics Dashboard
- Upload Interface
- Prediction Interface
- Loading Animation
- Responsive Design
- Real-Time Detection Visualization

Technologies:

```text
HTML
CSS
JavaScript
jQuery
Bootstrap
```

---

# 🐳 Dockerization

Dockerfile:

```dockerfile
FROM python:3.11-slim-bullseye

WORKDIR /app

COPY . /app

RUN apt update -y && apt install awscli -y

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 unzip -y

RUN pip install -r requirements.txt

CMD ["python3", "app.py"]
```

Build Docker Image:

```bash
docker build -t ecosortvision .
```

Run Docker Container:

```bash
docker run -p 8080:8080 ecosortvision
```

---

# ☁️ AWS Deployment Architecture

```text
GitHub Repository
        │
        ▼
GitHub Actions
        │
        ▼
Docker Build
        │
        ▼
Amazon ECR
        │
        ▼
AWS EC2
        │
        ▼
Docker Container
        │
        ▼
Flask Application
```

---

# 🔄 CI/CD Pipeline

GitHub Actions Workflow:

```text
.github/workflows/main.yaml
```

Stages:

### Continuous Integration

- Checkout Code
- Linting
- Unit Testing

### Continuous Delivery

- Configure AWS
- Login ECR
- Build Docker Image
- Push Docker Image

### Continuous Deployment

- Pull Latest Image
- Run Docker Container
- Deploy on EC2

---

# 🔐 GitHub Secrets Required

```text
AWS_ACCESS_KEY_ID

AWS_SECRET_ACCESS_KEY

AWS_REGION

AWS_ECR_LOGIN_URI

ECR_REPOSITORY_NAME
```

---

# 📦 AWS Setup

## Step 1

Create IAM User

Permissions:

```text
AmazonEC2FullAccess

AmazonEC2ContainerRegistryFullAccess
```

---

## Step 2

Create ECR Repository

Example:

```text
ecosortvision
```

Save:

```text
Repository URI
```

---

## Step 3

Launch EC2 Instance

Recommended:

```text
Ubuntu
t2.medium or above
```

---

## Step 4

Install Docker

```bash
sudo apt update

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

---

## Step 5

Configure Self Hosted Runner

GitHub:

```text
Settings
→ Actions
→ Runners
→ New Self Hosted Runner
```

Run commands provided by GitHub on EC2.

---

# 💻 Local Setup

## Clone Repository

```bash
git clone https://github.com/yourusername/EcoSort-Vision.git
```

```bash
cd EcoSort-Vision
```

---

## Create Environment

```bash
conda create -n ecosort python=3.11 -y
```

```bash
conda activate ecosort
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Project

```bash
pip install -e .
```

---

# 🏃 Run Application

```bash
python app.py
```

Open:

```text
http://localhost:8080
```

---

# 🏋️ Train Model

Open browser:

```text
http://localhost:8080/train
```

Training Pipeline will execute:

```text
Data Ingestion
↓
Data Validation
↓
YOLO11 Training
↓
best.pt Generation
```

---

# 🔍 Prediction Workflow

```text
Upload Image
      │
      ▼
Convert to Base64
      │
      ▼
Flask API
      │
      ▼
YOLO11 Prediction
      │
      ▼
Bounding Boxes
      │
      ▼
Encoded Output
      │
      ▼
Browser Display
```

---

# 📚 Libraries Used

### Core

```text
Python
Flask
Flask-CORS
```

### Computer Vision

```text
OpenCV
Pillow
Ultralytics
PyTorch
TorchVision
```

### Data Handling

```text
NumPy
Pandas
PyYAML
```

### Machine Learning

```text
Scikit-Learn
```

### Utilities

```text
gdown
dill
from-root
```

### Visualization

```text
Matplotlib
Seaborn
```

### Deployment

```text
Docker
AWS CLI
GitHub Actions
```

---

# 🔮 Future Improvements

- Streamlit Deployment
- FastAPI Backend
- Video Inference
- Real-Time Camera Detection
- Multi-Object Tracking
- AWS ECS Deployment
- Kubernetes Deployment
- Model Monitoring
- MLflow Integration
- Data Drift Detection

---

# 👨‍💻 Author

### Gouthum Kharvi

AI / ML Engineer

GitHub:
https://github.com/GouthumKharvi

LinkedIn:
https://www.linkedin.com/in/gouthum-kharvi-2366a6219/

Portfolio:
https://gouthumkharvi.github.io/Datascience_Portfolio/

---

# 🙏 Acknowledgements

- Ultralytics YOLO11
- Roboflow
- Flask
- PyTorch
- AWS
- GitHub Actions

---

# 📜 License

This project is licensed under the MIT License.

---

## ⭐ If you found this project useful, please consider giving it a star.