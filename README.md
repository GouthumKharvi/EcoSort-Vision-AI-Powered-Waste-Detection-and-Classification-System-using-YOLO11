<div align="center">

<!-- ANIMATED HEADER -->
<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Orbitron&size=38&duration=3000&pause=1000&color=00FFB3&center=true&vCenter=true&width=1000&lines=♻️+EcoSort-Vision;Smart+Waste+Detection+%26+Classification;Powered+by+YOLO11+and+Computer+Vision;Building+a+Cleaner+Future+with+AI" />
</p>

<!-- BADGES -->
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/YOLO11-Ultralytics-00FFAA?style=for-the-badge&logo=github&logoColor=black"/>
  <img src="https://img.shields.io/badge/Flask-Web%20App-000000?style=for-the-badge&logo=flask&logoColor=white"/>
  <img src="https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/AWS-EC2%20%7C%20ECR-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white"/>
  <img src="https://img.shields.io/badge/GitHub-Actions%20CI%2FCD-2088FF?style=for-the-badge&logo=github-actions&logoColor=white"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/PyTorch-Deep%20Learning-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white"/>
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white"/>
  <img src="https://img.shields.io/badge/Roboflow-Dataset-purple?style=for-the-badge&logo=roboflow&logoColor=white"/>
  <img src="https://img.shields.io/badge/MLOps-Production%20Grade-FF6B6B?style=for-the-badge&logo=mlflow&logoColor=white"/>
</p>

<br/>

> **♻️ An end-to-end Computer Vision & MLOps project that detects and classifies 10 categories of waste using YOLO11 — from data ingestion to AWS cloud deployment with CI/CD automation.**

<br/>

<!-- QUICK LINKS -->
<p align="center">
  <a href="#-project-overview"><kbd>📌 Overview</kbd></a> &nbsp;•&nbsp;
  <a href="#-dataset"><kbd>📊 Dataset</kbd></a> &nbsp;•&nbsp;
  <a href="#%EF%B8%8F-project-architecture"><kbd>🏗️ Architecture</kbd></a> &nbsp;•&nbsp;
  <a href="#-project-structure"><kbd>📂 Structure</kbd></a> &nbsp;•&nbsp;
  <a href="#-local-setup--installation"><kbd>💻 Setup</kbd></a> &nbsp;•&nbsp;
  <a href="#-aws-deployment"><kbd>☁️ AWS</kbd></a> &nbsp;•&nbsp;
  <a href="#-cicd-pipeline"><kbd>🔄 CI/CD</kbd></a>
</p>

</div>

---

## 📌 Project Overview

**EcoSort-Vision** is a production-grade, end-to-end Computer Vision system that intelligently detects and classifies different categories of waste from images using **YOLO11** (Ultralytics).

The system is built with a full **MLOps pipeline** — from automated data ingestion and validation all the way through model training, containerization, and cloud deployment on AWS with zero-touch CI/CD.

### What it does:
- Takes an image as input via a modern web UI
- Converts it to base64 and sends to the Flask API
- Runs YOLO11 inference to detect waste objects with bounding boxes
- Returns the annotated prediction image back to the browser in real time

### Why it was built:
Manual waste sorting is slow, labor-intensive, error-prone, and expensive. Improper segregation causes environmental pollution and recycling inefficiency. This AI system automates that process at scale.

---

## 📊 Dataset

| Property | Detail |
|---|---|
| **Source** | Roboflow |
| **Project** | `garbage-euqch-y33ea` |
| **Workspace** | `gouthums-workspace` |
| **Total Images** | **6,075 images** |
| **Annotation Format** | YOLO11 (bounding boxes) |
| **Number of Classes** | **10 classes** |
| **License** | CC BY 4.0 |

### 🏷️ Waste Classes

```
0  →  Battery
1  →  Cardboard
2  →  Clothes
3  →  Glass
4  →  Metal
5  →  Miscellaneous Trash
6  →  Organic
7  →  Paper
8  →  Plastic
9  →  Shoes
```

### Dataset Structure

```
waste_detection/
├── train/
│   ├── images/
│   └── labels/
├── valid/
│   ├── images/
│   └── labels/
├── test/
│   ├── images/
│   └── labels/
└── data.yaml
```

### data.yaml

```yaml
train: ../train/images
val:   ../valid/images
test:  ../test/images

nc: 10
names: ['battery', 'cardboard', 'clothes', 'glass', 'metal',
        'miscellaneous trash', 'organic', 'paper', 'plastic', 'shoes']

roboflow:
  workspace: gouthums-workspace
  project: garbage-euqch-y33ea
  version: dataset
  license: CC BY 4.0
  url: https://app.roboflow.com/gouthums-workspace/garbage-euqch-y33ea/dataset
```

---

## 🏗️ Project Architecture

```
                        ┌─────────────────────────┐
                        │      Google Drive        │
                        │  (waste_detection.zip)   │
                        └───────────┬─────────────┘
                                    │ gdown download
                                    ▼
                        ┌─────────────────────────┐
                        │    Data Ingestion        │
                        │  download_data()         │
                        │  extract_zip_file()      │
                        │  → artifacts/data_       │
                        │    ingestion/fs/         │
                        └───────────┬─────────────┘
                                    │
                                    ▼
                        ┌─────────────────────────┐
                        │    Data Validation       │
                        │  validate_all_files_     │
                        │  exist()                 │
                        │  → status.txt            │
                        │  → True / False          │
                        └───────────┬─────────────┘
                                    │ if True
                                    ▼
                        ┌─────────────────────────┐
                        │    Model Trainer         │
                        │  custom_yolo11.yaml      │
                        │  yolo11n.pt (pretrained) │
                        │  YOLO11 Training         │
                        │  → artifacts/model_      │
                        │    trainer/best.pt       │
                        └───────────┬─────────────┘
                                    │
                                    ▼
                        ┌─────────────────────────┐
                        │    Flask Web App         │
                        │  / → index.html          │
                        │  /train → pipeline       │
                        │  /predict → inference    │
                        │  /live → webcam          │
                        └───────────┬─────────────┘
                                    │
                                    ▼
                        ┌─────────────────────────┐
                        │    Docker Container      │
                        │  python:3.11-slim-       │
                        │  bullseye                │
                        └───────────┬─────────────┘
                                    │
                                    ▼
                        ┌─────────────────────────┐
                        │    GitHub Actions        │
                        │  CI → CD → Deploy        │
                        └───────────┬─────────────┘
                                    │
                                    ▼
                        ┌─────────────────────────┐
                        │    Amazon ECR            │
                        │  Docker Image Registry   │
                        └───────────┬─────────────┘
                                    │
                                    ▼
                        ┌─────────────────────────┐
                        │    AWS EC2 (Ubuntu)      │
                        │  Self-Hosted Runner      │
                        │  Docker Container Live   │
                        └─────────────────────────┘
```

---

## ⚙️ MLOps Workflow — Step by Step

### 1️⃣ Data Ingestion

**File:** `ecosortvision/components/data_ingestion.py`

The Data Ingestion component is responsible for downloading the waste detection dataset from Google Drive and extracting it to the feature store.

**Config (`DataIngestionConfig`):**

| Parameter | Value |
|---|---|
| `data_ingestion_dir` | `artifacts/data_ingestion` |
| `feature_store_file_path` | `artifacts/data_ingestion/fs` |
| `data_download_url` | Google Drive shared link |

**Functions:**

```python
download_data()         # Downloads waste_detection.zip from Google Drive using gdown
extract_zip_file()      # Extracts zip into artifacts/data_ingestion/fs/
initiate_data_ingestion()  # Orchestrates both and returns DataIngestionArtifact
```

**Output Artifact:**

```python
@dataclass
class DataIngestionArtifact:
    data_zip_file_path: str     # Path to the downloaded zip
    feature_store_path: str     # Path to extracted dataset
```

**How gdown works in the code:**

```python
file_id = dataset_url.split("/")[-2]
prefix = 'https://drive.google.com/uc?/export=download&id='
gdown.download(prefix + file_id, zip_file_path)
```

---

### 2️⃣ Data Validation

**File:** `ecosortvision/components/data_validation.py`

The Data Validation component performs multiple levels of checks to ensure the dataset is complete and consistent before training begins.

**Config (`DataValidationConfig`):**

| Parameter | Value |
|---|---|
| `data_validation_dir` | `artifacts/data_validation` |
| `valid_status_file_dir` | `artifacts/data_validation/status.txt` |
| `required_file_list` | `['train', 'valid', 'test', 'data.yaml']` |

**Validation Checks performed:**

```
✅ Check 1 → Required top-level directories exist: train/, valid/, test/, data.yaml
✅ Check 2 → Sub-directories exist: train/images, train/labels, valid/images,
             valid/labels, test/images, test/labels
✅ Check 3 → Image count == Label count for train, valid, and test splits
✅ Check 4 → data.yaml exists and is not empty
```

**Output:**

```
artifacts/data_validation/status.txt
→ Validation status: True
```

**Output Artifact:**

```python
@dataclass
class DataValidationArtifact:
    validation_status: bool     # True if all checks pass, False otherwise
```

If validation passes, the zip file is copied to the working directory for the model trainer to unzip.

---

### 3️⃣ Model Trainer

**File:** `ecosortvision/components/model_trainer.py`

The Model Trainer uses YOLO11 with a custom architecture configuration to train on the waste detection dataset.

**Config (`ModelTrainerConfig`):**

| Parameter | Value |
|---|---|
| `model_trainer_dir` | `artifacts/model_trainer` |
| `weight_name` | `yolo11n.pt` |
| `no_epochs` | `1` |
| `batch_size` | `16` |
| `img_size` | `640 x 640` |

**Training Steps:**

```
Step 1  →  Unzip waste_detection.zip
Step 2  →  Read data.yaml → extract number of classes (nc=10)
Step 3  →  Load ultralytics/ultralytics/cfg/models/11/yolo11.yaml
Step 4  →  Update nc in config to 10
Step 5  →  Write custom_yolo11.yaml
Step 6  →  Load pretrained yolo11n.pt weights
Step 7  →  Run YOLO11 training (epochs=1, imgsz=640, batch=16)
Step 8  →  Copy best.pt → artifacts/model_trainer/best.pt
```

**Training command executed:**

```python
os.system(
    f'python -c "from ultralytics import YOLO; '
    f'model=YOLO(\'ultralytics/ultralytics/cfg/models/11/custom_yolo11.yaml\'); '
    f'model.load(\'{self.model_trainer_config.weight_name}\'); '
    f'model.train(data=\'data.yaml\', '
    f'epochs={self.model_trainer_config.no_epochs}, '
    f'imgsz=640, '
    f'batch={self.model_trainer_config.batch_size}, '
    f'cache=False, '
    f'name=\'garbage_detection\')"'
)
```

**Training Outputs (Artifacts):**

```
runs/detect/garbage_detection/weights/
├── best.pt             ← Best model (copied to artifacts/model_trainer/)
└── last.pt             ← Last epoch model

runs/detect/garbage_detection/
├── results.csv         ← Training metrics per epoch
├── confusion_matrix.png
├── PR_curve.png
├── F1_curve.png
├── P_curve.png
└── R_curve.png
```

**Output Artifact:**

```python
@dataclass
class ModelTrainerArtifact:
    trained_model_file_path: str    # ultralytics/best.pt
```

---

## 🧠 Model Details

| Property | Value |
|---|---|
| **Architecture** | YOLO11n (nano) |
| **Framework** | Ultralytics |
| **Backend** | PyTorch |
| **Pretrained Weights** | `yolo11n.pt` |
| **Custom Config** | `custom_yolo11.yaml` |
| **Input Image Size** | `640 × 640` |
| **Epochs** | 1 (configurable via constants) |
| **Batch Size** | 16 |
| **Output Model** | `artifacts/model_trainer/best.pt` |

---

## 🖥️ Flask Web Application

**File:** `app.py`

### Routes

| Route | Method | Description |
|---|---|---|
| `/` | GET | Renders `templates/index.html` |
| `/train` | GET | Triggers full training pipeline |
| `/predict` | POST | Accepts base64 image, returns predicted image |
| `/live` | GET | Starts webcam inference with YOLO11 |

### Prediction Flow

```
Browser
  │
  │  Upload image
  ▼
jQuery (AJAX POST)
  │
  │  { "image": "<base64_string>" }
  ▼
Flask /predict
  │
  │  decodeImage() → saves to data/inputImage.jpg
  ▼
YOLO11 predict
  │
  │  model=artifacts/model_trainer/best.pt
  │  source=data/inputImage.jpg
  │  conf=0.5
  │  project=runs/detect
  │  name=prediction
  │  exist_ok=True
  ▼
encodeImageIntoBase64()
  │
  │  reads runs/detect/prediction/inputImage.jpg
  ▼
Flask returns
  │
  │  { "image": "<base64_predicted_image>" }
  ▼
Browser displays annotated result
```

### Utility Functions (`ecosortvision/utils/main_utils.py`)

```python
def decodeImage(imgstring, fileName):
    """Decodes base64 string and saves image to data/inputImage.jpg"""
    imgdata = base64.b64decode(imgstring)
    with open("./data/" + fileName, 'wb') as f:
        f.write(imgdata)

def encodeImageIntoBase64(croppedImagePath):
    """Reads predicted image and returns base64 encoded bytes"""
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
```

---

## 🎨 Frontend — Modern UI

**File:** `templates/index.html`

The frontend is a fully animated, futuristic command-center interface built with HTML, CSS, JavaScript, and jQuery.

### Features

| Feature | Description |
|---|---|
| **Particle Galaxy Background** | 120 interactive cyan/violet nodes with mouse-reactive connections using Canvas API |
| **Scrolling Ticker Belt** | Live scrolling display of all 10 waste class names |
| **Live Stats Dashboard** | Confidence %, FPS, Waste Classes, Latency — all ticking every 2 seconds |
| **Dual Panel Layout** | Input Frame panel (cyan) + Detection Output panel (violet) |
| **Scan Line Animations** | Sweeping scan lines inside both panels |
| **Radar Sweep** | Animated radar in the output panel while awaiting results |
| **Glowing Corner Brackets** | Pulsing corner indicators on panels |
| **Loading Overlay** | Full-screen blur overlay with spinner + animated progress bar |
| **Responsive Design** | Works on mobile and desktop |

### Technologies Used

```
HTML5 + CSS3 (animations, gradients, custom properties)
JavaScript (Canvas API, requestAnimationFrame)
jQuery 3.4.1 (AJAX calls)
Bootstrap 4.0.0 (grid utilities)
Google Fonts — Space Grotesk + JetBrains Mono
```

---

## 📂 Project Structure

```
EcoSort-Vision/
│
├── .github/
│   └── workflows/
│       └── main.yaml                      ← GitHub Actions CI/CD pipeline
│
├── artifacts/
│   ├── data_ingestion/
│   │   └── fs/                            ← Extracted dataset (feature store)
│   │       ├── train/images + labels
│   │       ├── valid/images + labels
│   │       ├── test/images + labels
│   │       ├── data.yaml
│   │       └── waste_detection.zip
│   ├── data_validation/
│   │   └── status.txt                     ← Validation result: True/False
│   └── model_trainer/
│       └── best.pt                        ← Trained YOLO11 model
│
├── config/
│   └── config.yaml
│
├── data/
│   ├── .gitkeep
│   └── inputImage.jpg                     ← Inference input image
│
├── ecosortvision/
│   ├── components/
│   │   ├── __init__.py
│   │   ├── data_ingestion.py              ← Downloads + extracts dataset
│   │   ├── data_validation.py             ← Validates dataset integrity
│   │   ├── model_trainer.py               ← YOLO11 training logic
│   │   ├── classifier_trainer.py
│   │   └── prediction.py
│   │
│   ├── constants/
│   │   ├── __init__.py
│   │   ├── application.py                 ← APP_HOST, APP_PORT
│   │   └── training_pipeline/
│   │       └── __init__.py                ← All training constants
│   │
│   ├── entity/
│   │   ├── config_entity.py               ← Dataclass configs for each pipeline stage
│   │   └── artifacts_entity.py            ← Dataclass artifacts for each pipeline stage
│   │
│   ├── exception/
│   │   └── __init__.py                    ← Custom AppException with traceback details
│   │
│   ├── logger/
│   │   └── __init__.py                    ← Timestamped log files in /log/
│   │
│   ├── pipeline/
│   │   ├── __init__.py
│   │   ├── training_pipeline.py           ← Orchestrates all 3 pipeline stages
│   │   └── prediction_pipeline.py
│   │
│   └── utils/
│       ├── __init__.py
│       └── main_utils.py                  ← read_yaml, write_yaml, encode/decode image
│
├── flowcharts/
│   ├── Data_Ingestion.png
│   ├── Data_Validation.png
│   └── Model_Trainer.png
│
├── log/                                   ← Auto-generated timestamped log files
│
├── research/
│   ├── trials.ipynb                       ← gdown download experiments
│   └── Waste_Detection_Using_YOLO_v11.ipynb
│
├── static/
│   ├── css/style.css
│   ├── js/script.js
│   └── images/.gitkeep
│
├── templates/
│   └── index.html                         ← Animated futuristic Flask UI
│
├── ultralytics/
│   └── ultralytics/cfg/models/11/
│       ├── yolo11.yaml                    ← Base YOLO11 architecture
│       └── custom_yolo11.yaml             ← Auto-generated with nc=10
│
├── app.py                                 ← Main Flask application
├── Dockerfile                             ← Container definition
├── requirements.txt                       ← All dependencies
├── setup.py                               ← Package setup
├── template.py                            ← Project scaffolding script
├── data.yaml                              ← Dataset config
├── yolo11n.pt                             ← Pretrained YOLO11 nano weights
├── .gitignore
└── README.md
```

---

## 🔧 Constants

**File:** `ecosortvision/constants/training_pipeline/__init__.py`

```python
ARTIFACTS_DIR = "artifacts"

# Data Ingestion
DATA_INGESTION_DIR_NAME          = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR = "fs"
DATA_DOWNLOAD_URL                = "https://drive.google.com/file/d/1orj3RpwtiAE4RfRW9hPSNaMSSuMZUpTm/view?usp=sharing"

# Data Validation
DATA_VALIDATION_DIR_NAME         = "data_validation"
DATA_VALIDATION_STATUS_FILE      = "status.txt"
DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "valid", "test", "data.yaml"]

# Model Trainer
MODEL_TRAINER_DIR_NAME               = "model_trainer"
MODEL_TRAINER_PRETRAINED_WEIGHT_NAME = "yolo11n.pt"
MODEL_TRAINER_NO_EPOCHS              = 1
MODEL_TRAINER_BATCH_SIZE             = 16
```

**File:** `ecosortvision/constants/application.py`

```python
APP_HOST = "0.0.0.0"
APP_PORT = 8080
```

---

## 📦 Entity Dataclasses

### Config Entities (`config_entity.py`)

```python
@dataclass
class TrainingPipelineConfig:
    artifacts_dir: str = ARTIFACTS_DIR

@dataclass
class DataIngestionConfig:
    data_ingestion_dir:     str   # artifacts/data_ingestion
    feature_store_file_path: str  # artifacts/data_ingestion/fs
    data_download_url:      str   # Google Drive URL

@dataclass
class DataValidationConfig:
    data_validation_dir:    str   # artifacts/data_validation
    valid_status_file_dir:  str   # artifacts/data_validation/status.txt
    required_file_list:     list  # ['train', 'valid', 'test', 'data.yaml']

@dataclass
class ModelTrainerConfig:
    model_trainer_dir: str        # artifacts/model_trainer
    weight_name:       str        # yolo11n.pt
    no_epochs:         int        # 1
    batch_size:        int        # 16
```

### Artifact Entities (`artifacts_entity.py`)

```python
@dataclass
class DataIngestionArtifact:
    data_zip_file_path: str       # Path to downloaded zip
    feature_store_path: str       # Path to extracted dataset

@dataclass
class DataValidationArtifact:
    validation_status: bool       # True or False

@dataclass
class ModelTrainerArtifact:
    trained_model_file_path: str  # ultralytics/best.pt
```

---

## 🐳 Docker

**File:** `Dockerfile`

```dockerfile
FROM python:3.11-slim-bullseye

WORKDIR /app
COPY . /app

RUN apt update -y && apt install awscli -y

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 unzip -y && pip install -r requirements.txt

CMD ["python3", "app.py"]
```

### Build and Run Locally

```bash
# Build image
docker build -t ecosortvision .

# Run container
docker run -p 8080:8080 ecosortvision
```

Open browser at `http://localhost:8080`

---

## 💻 Local Setup & Installation

### Prerequisites

- Python 3.11
- Conda
- Git
- Docker (optional for local testing)

---

### Step 1 — Clone the Repository

```bash
git clone https://github.com/GouthumKharvi/EcoSort-Vision.git
cd EcoSort-Vision
```

---

### Step 2 — Create and Activate Conda Environment

```bash
conda create -n ecosort python=3.11 -y
conda activate ecosort
```

---

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 4 — Install the Package

```bash
pip install -e .
```

---

### Step 5 — Run the Flask Application

```bash
python app.py
```

Open your browser at:

```
http://localhost:8080
```

---

### Step 6 — Train the Model (via Browser)

Navigate to:

```
http://localhost:8080/train
```

This triggers the full training pipeline:

```
Data Ingestion  →  Data Validation  →  YOLO11 Training  →  best.pt saved
```

---

### Step 7 — Run Prediction

1. Open `http://localhost:8080`
2. Click **Upload Image** → select any waste image
3. Click **Run Detection**
4. View annotated result with bounding boxes in the output panel

---

## 📚 Libraries & Dependencies

### Core

| Library | Purpose |
|---|---|
| `flask` | Web application framework |
| `flask-cors` | Cross-Origin Resource Sharing |
| `gdown` | Google Drive dataset download |
| `from-root` | Root-relative path resolution |
| `dill` | Enhanced serialization |

### Computer Vision & Deep Learning

| Library | Purpose |
|---|---|
| `ultralytics>=8.3.0` | YOLO11 model training and inference |
| `torch>=2.7.0` | PyTorch deep learning backend |
| `torchvision>=0.22.0` | Vision transforms and datasets |
| `opencv-python>=4.10.0` | Image reading and processing |
| `Pillow>=10.0.0` | Image manipulation |

### Data & Utilities

| Library | Purpose |
|---|---|
| `numpy>=1.26.0` | Numerical operations |
| `pandas>=2.2.0` | Data analysis |
| `PyYAML>=6.0` | YAML config file parsing |
| `scikit-learn>=1.6.0` | Metrics and evaluation |
| `matplotlib>=3.8.0` | Training curve plotting |
| `seaborn>=0.13.0` | Visualization |
| `scipy>=1.13.0` | Scientific computing |
| `requests>=2.32.0` | HTTP requests |
| `tqdm>=4.67.0` | Progress bars |

---

## ☁️ AWS Deployment

### Architecture

```
GitHub Repository
       │
       │  git push → main
       ▼
GitHub Actions (CI/CD)
       │
       │  Build Docker Image
       ▼
Amazon ECR
(Elastic Container Registry)
       │
       │  docker pull
       ▼
AWS EC2 (Ubuntu, t2.medium+)
Self-Hosted GitHub Runner
       │
       │  docker run -p 8080:8080
       ▼
Flask App Live on EC2 Public IP
```

---

### Step 1 — Create IAM User

Go to AWS Console → IAM → Users → Create User

Attach these policies directly:

```
AmazonEC2FullAccess
AmazonEC2ContainerRegistryFullAccess
```

Download **Access Key ID** and **Secret Access Key** — you'll need these for GitHub Secrets.

---

### Step 2 — Create ECR Repository

Go to AWS Console → Elastic Container Registry → Create Repository

```
Repository name: ecosortvision
Visibility:      Private
```

Save the **Repository URI**, it will look like:

```
<account_id>.dkr.ecr.<region>.amazonaws.com/ecosortvision
```

---

### Step 3 — Launch EC2 Instance

Go to AWS Console → EC2 → Launch Instance

```
AMI:           Ubuntu Server 22.04 LTS
Instance Type: t2.medium (minimum — YOLO11 is heavy)
Storage:       30 GB (gp2)
Security Group: Allow inbound port 8080 (Custom TCP) from anywhere
```

---

### Step 4 — Install Docker on EC2

SSH into your EC2 instance and run:

```bash
# Update packages
sudo apt-get update -y
sudo apt-get upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add ubuntu user to docker group
sudo usermod -aG docker ubuntu
newgrp docker

# Verify Docker is working
docker --version
```

---

### Step 5 — Configure Self-Hosted GitHub Actions Runner on EC2

Go to your GitHub repo:

```
Settings → Actions → Runners → New self-hosted runner
```

Select **Linux** as the OS. GitHub will provide a set of commands — copy and run each one on your EC2 instance:

```bash
# Example commands provided by GitHub (run on EC2):
mkdir actions-runner && cd actions-runner
curl -o actions-runner-linux-x64-2.x.x.tar.gz -L https://github.com/actions/runner/releases/...
tar xzf ./actions-runner-linux-x64-2.x.x.tar.gz
./config.sh --url https://github.com/<your-username>/EcoSort-Vision --token <TOKEN>
./run.sh
```

Your EC2 instance is now a self-hosted runner for the `Continuous-Deployment` job.

---

### Step 6 — Configure GitHub Secrets

Go to your GitHub repo:

```
Settings → Secrets and variables → Actions → New repository secret
```

Add the following secrets:

| Secret Name | Value |
|---|---|
| `AWS_ACCESS_KEY_ID` | Your IAM user access key ID |
| `AWS_SECRET_ACCESS_KEY` | Your IAM user secret access key |
| `AWS_REGION` | e.g. `ap-south-1` or `us-east-1` |
| `AWS_ECR_LOGIN_URI` | e.g. `566373416292.dkr.ecr.ap-south-1.amazonaws.com` |
| `ECR_REPOSITORY_NAME` | `ecosortvision` |

---

## 🔄 CI/CD Pipeline

**File:** `.github/workflows/main.yaml`

The GitHub Actions workflow has **3 stages** that run sequentially on every push to `main`.

### Trigger

```yaml
on:
  push:
    branches:
      - main
    paths-ignore:
      - 'README.md'
```

---

### Stage 1 — Continuous Integration

**Runner:** `ubuntu-latest`

```
✅ Checkout Code
✅ Lint code
✅ Run unit tests
```

---

### Stage 2 — Continuous Delivery

**Runner:** `ubuntu-latest`

```
✅ Checkout Code
✅ Install utilities (jq, unzip)
✅ Configure AWS credentials (from GitHub Secrets)
✅ Login to Amazon ECR
✅ Build Docker image
✅ Tag image as :latest
✅ Push Docker image to Amazon ECR
```

Docker build & push command in workflow:

```bash
docker build -t $ECR_REGISTRY/$ECR_REPOSITORY:latest .
docker push $ECR_REGISTRY/$ECR_REPOSITORY:latest
```

---

### Stage 3 — Continuous Deployment

**Runner:** `self-hosted` (your EC2 instance)

```
✅ Checkout Code
✅ Configure AWS credentials
✅ Login to Amazon ECR
✅ Pull latest Docker image from ECR
✅ Run Docker container on port 8080
✅ Clean up old images and containers
```

Docker run command:

```bash
docker run -d -p 8080:8080 --ipc="host" --name=ecosortvision \
  -e 'AWS_ACCESS_KEY_ID=${{ secrets.AWS_ACCESS_KEY_ID }}' \
  -e 'AWS_SECRET_ACCESS_KEY=${{ secrets.AWS_SECRET_ACCESS_KEY }}' \
  -e 'AWS_REGION=${{ secrets.AWS_REGION }}' \
  ${{ secrets.AWS_ECR_LOGIN_URI }}/${{ secrets.ECR_REPOSITORY_NAME }}:latest
```

Cleanup after deploy:

```bash
docker system prune -f
```

---

### Full CI/CD Flow Diagram

```
git push → main
     │
     ▼
┌─────────────────────────────────────────────────────┐
│  Job 1: Continuous Integration (ubuntu-latest)       │
│  → Checkout → Lint → Unit Tests                     │
└──────────────────────────┬──────────────────────────┘
                           │ needs: integration
                           ▼
┌─────────────────────────────────────────────────────┐
│  Job 2: Continuous Delivery (ubuntu-latest)          │
│  → Configure AWS → Login ECR                        │
│  → docker build → docker push to ECR               │
└──────────────────────────┬──────────────────────────┘
                           │ needs: build-and-push-ecr-image
                           ▼
┌─────────────────────────────────────────────────────┐
│  Job 3: Continuous Deployment (self-hosted EC2)      │
│  → Login ECR → docker pull latest                   │
│  → docker run -p 8080:8080                          │
│  → docker system prune -f                           │
└─────────────────────────────────────────────────────┘
                           │
                           ▼
          App Live at http://<EC2-Public-IP>:8080
```

---

## 📋 Exception Handling

**File:** `ecosortvision/exception/__init__.py`

Custom exception class that captures filename, line number, and error message for precise debugging:

```python
class AppException(Exception):
    def __init__(self, error_message, error_detail):
        self.error_message = error_message_detail(error_message, error_detail)

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error in script [{0}] at line [{1}]: {2}".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message
```

---

## 📝 Logging

**File:** `ecosortvision/logger/__init__.py`

Timestamped log files auto-generated in `/log/` directory:

```python
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(from_root(), 'log', LOG_FILE)

logging.basicConfig(
    filename=lOG_FILE_PATH,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
```

Every pipeline stage logs its entry, operations, and exit — making debugging straightforward.

---

## 🔮 Future Improvements

- [ ] FastAPI backend for async inference
- [ ] Video file inference support
- [ ] Real-Time webcam detection in browser (WebRTC)
- [ ] Multi-Object Tracking
- [ ] MLflow Integration for experiment tracking
- [ ] Data Drift Detection
- [ ] AWS ECS / Kubernetes deployment
- [ ] Model monitoring dashboard
- [ ] Streamlit alternative frontend
- [ ] More training epochs + larger YOLO11 variant

---

## 🧪 Research Notebooks

| Notebook | Description |
|---|---|
| `research/trials.ipynb` | gdown download experiments, Google Drive URL parsing |
| `research/Waste_Detection_Using_YOLO_v11.ipynb` | Full YOLO11 training experiments |

---

## 📋 Workflow Order

When building this project from scratch, follow this order:

```
1. constants          →  Define all config constants
2. entity             →  Define config and artifact dataclasses  
3. components         →  Build data_ingestion, data_validation, model_trainer
4. pipeline           →  Wire components in training_pipeline.py
5. app.py             →  Flask routes connecting pipeline + prediction
```

---

## 👨‍💻 Author

<div align="center">

### Gouthum Kharvi
**AI / ML Engineer**

[![GitHub](https://img.shields.io/badge/GitHub-GouthumKharvi-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/GouthumKharvi)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Gouthum%20Kharvi-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gouthum-kharvi-2366a6219/)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-FF6B6B?style=for-the-badge&logo=google-chrome&logoColor=white)](https://gouthumkharvi.github.io/Datascience_Portfolio/)

</div>

---

## 🙏 Acknowledgements

- [Ultralytics](https://github.com/ultralytics/ultralytics) — YOLO11 framework
- [Roboflow](https://roboflow.com) — Dataset annotation and hosting
- [Flask](https://flask.palletsprojects.com) — Web framework
- [PyTorch](https://pytorch.org) — Deep learning backend
- [AWS](https://aws.amazon.com) — Cloud deployment
- [GitHub Actions](https://github.com/features/actions) — CI/CD automation

---

## 📜 License

This project is licensed under the **MIT License**.

---

<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer&animation=twinkling"/>

**⭐ If you found EcoSort-Vision useful, please give it a star on GitHub!**

</div>
