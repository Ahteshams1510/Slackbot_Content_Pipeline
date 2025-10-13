# Slackbot_Content_Pipeline

# Slackbot Content Pipeline – AI Engineer Assignment

### Author
**Ahtesham Shaikh**

---

### Overview
This project is a Python-based mock Slackbot application built for the AI Engineer assignment.  
It simulates a content-generation workflow using Flask and produces automated PDF reports.

---

### Features
- Flask server that mimics Slack event handling  
- Mock content generator simulating AI text output  
- Automated PDF report generation using ReportLab  
- Test script (`test_request.py`) to simulate Slack requests  

---

### Folder Structure

Slackbot_Content_Pipeline/
│
├── main.py
├── slack_bot.py
├── content_generator.py
├── pdf_generator.py
├── test_request.py
├── requirements.txt
├── README.md
│
└── outputs/
└── AI_Report_<timestamp>.pdf


---

### How to Run Locally

1. **Activate the virtual environment**
   ```bash
   venv\Scripts\activate


## 🧩 Step 2 — Install dependencies
pip install -r requirements.txt


## 🧩 Step 3 — Run the Flask app
python main.py


## 🧩 Step 4 — Run the test script

python test_request.py


---

## 🧩 Step 5 — Final check before submission

✅ Double-check that:
- You can run `python main.py` and see “Running on http://127.0.0.1:3000”  
- Then `python test_request.py` prints:


- And a **PDF report** is created inside `outputs/`

---

## 🧩 Step 6 — Zip and Submit

Now, right-click the `Slackbot_Content_Pipeline` folder →  
**Send to → Compressed (zipped) folder**  
Rename it to:

Project completed as part of AI Engineer Assignment – Empowerverse (Author: Ahtesham Shaikh)



