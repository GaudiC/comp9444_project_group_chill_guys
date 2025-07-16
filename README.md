# 🧠 COMP9444 Group Project — Chill Guys  
> Fashion Image Label Extraction, Dataset Preprocessing & Directory Pipeline

---

## 📁 Project Overview

This repository (`comp9444_project_group_chill_guys`) contains Python code and documentation for extracting and processing labels from weakly annotated fashion datasets (AAT & LAT). The goal is to prepare structured label data and organize associated images for training deep learning models as part of UNSW's COMP9444 Neural Networks and Deep Learning course.

> ⚠️ **Note**: The entire dataset folder (`data/`) is too large to be included in the repository. All data files are stored and shared via **Google Drive only**.

---

## 📂 Project Directory Structure

<img width="503" height="909" alt="image" src="https://github.com/user-attachments/assets/eb98e88d-c677-44a9-8ffd-c94da6bfec71" />

###![Below seems to be broken when not open in full view]
comp9444_project_group_chill_guys/
│
├── data/ ← [📁 Google Drive only — not included here]
│ ├── raw/
│ │ └── AiDLabA100/
│ │ ├── AAT/
│ │ │ ├── image/
│ │ │ └── label/AAT.json
│ │ └── LAT/
│ │ ├── image/
│ │ └── label/LAT.json
│ ├── labels/
│ │ ├── aat_labels.json
│ │ ├── lat_labels.json
│ │ └── merged_labels.json
│ └── processed/
│ ├── AAT/
│ └── LAT/
│
├── src/
│ ├── label/
│ │ ├── merge_labels.py
│ │ ├── split_labels.py
│ │ └── copy_images.py
│ └── init.py
│
├── notebooks/
│ └── exploration.ipynb
│
├── assets/
│ └── directory_structure.png ← Screenshot of VS Code folder layout
│
├── requirements.txt
├── setup.py
├── .gitignore
└── README.md

> 📎 A preview of the folder structure is available in `/assets/directory_structure.png`.

---

## 🚀 How to Run This Project

### 1. Clone the Repository

git clone https://github.com/GaudiC/comp9444_project_group_chill_guys.git
cd comp9444_project_group_chill_guys

### 2. Install Dependencies

pip install -r requirements.txt
Alternatively, you can install it as a package:

pip install -e .

### 3. Run the Scripts

python src/label/merge_labels.py
python src/label/split_labels.py
python src/label/copy_images.py
🔒 These scripts only process top-level files. Subdirectories are not traversed.


### 4. 🗂 Dataset Access (Google Drive Only)
All image and label files are stored in a shared Google Drive folder.

The folder structure in Drive mirrors the local data/ layout.

Access is provided via a link in the shared project documentation (Google Docs).

### 5. ⚠️ Safety Notes
Some scripts will rename files and remove dummy entries during cleaning.

Make sure to back up your files before executing them on real datasets.

All project files must exist at the same folder level — nested structures are not supported.

### 🔐 Project Privacy & Collaboration
This repository is currently public. To make it private while still allowing group access:

Go to Settings → scroll to Danger Zone → click Make private

Go to Settings → Collaborators and invite each group member by their GitHub username

Members will receive an access invite via email or notification


### 🧾 .gitignore
As mentioned before the following folders below will not be included in this repo.

gitignore
data/
venv/

### 👥 Team Information
Team: Chill Guys

Course: COMP9444 — Neural Networks and Deep Learning


## 📜 License
This repository is part of an academic project for COMP9444 at UNSW.
It is provided for internal collaboration only and is not licensed for public distribution.
