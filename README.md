#  Vector Detection Project

This repository provides a step-by-step guide to enable your Anki Vector robot to recognize other Vector robots using its onboard camera and a custom-trained YOLOv8 object detection model.

---

##  Get Started

###  Dataset

You can either:
- **Download the dataset** directly: [dataset.zip](https://github.com/user-attachments/files/20275642/dataset.zip)  
- **Or create your own dataset** using the walkthrough here:  
  🔗 https://github.com/mparekh99/VectorDataCollection

---

###  Model Training & Evaluation

Visit the following repository to train the YOLOv8 model using the provided dataset and evaluate its performance:

🔗 https://github.com/mparekh99/VectorDetectionModel

---

###  Run the Detection Model on Vector

#### 1. Clone This Repository
```
git clone https://github.com/mparekh99/VectorDetection.git
cd VectorDetectionModel
```
#### 2. Set Up a Virtual Environment

Open a terminal and run:
```
python -m venv .venv
.\.venv\Scripts\activate
```

#### 3. Install Dependencies 
Once the environment is activated, install the required packages:
```
pip install -r requirements.txt
````
#### 4. Vector SDK Setup

Follow these setup guides:

- 📦 [Vector Setup by mparekh99](https://github.com/mparekh99/Vector-Setup)
- 🔌 [WIREPOD Installation Guide](https://github.com/kercre123/wire-pod/wiki/Installation)
- 🧠 [Wirepod Python SDK for Vector](https://github.com/kercre123/wirepod-vector-python-sdk)

> ⚠️ Make sure both Vectors are paired and configured via the WIREPOD and SDK before running any scripts.

## Usage
```
python detect.py
```

## Output 
![Recording - Made with Clipchamp](https://github.com/user-attachments/assets/f0caddc8-76d4-4bf1-b93a-19a1aaa13e75)


