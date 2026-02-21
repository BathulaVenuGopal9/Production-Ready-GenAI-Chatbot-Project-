# AI Career Advisor Chatbot — Complete Project
## Project Overview

AI Career Advisor is an intelligent chatbot that helps users explore career paths, required skills, learning roadmap, and guidance using AI.
The application is built with Python + Streamlit and deployed on AWS EC2 for live public access.

## Features

AI-based career guidance

Suggests career paths based on user input

Skills & roadmap recommendations

Interactive chatbot UI

Runs on cloud (AWS)

Auto-start after reboot

Works 24/7 in background

## Tech Stack
Component	Technology
Language	Python
Frontend	Streamlit
Backend	Python
AI	LLM / API
Deployment	AWS EC2 (Ubuntu)
Process Manager	systemd
Port	8501
## Project Structure
AI-Career-Advisor/
│
├── app.py
├── requirements.txt
├── backend/
├── assets/
├── config/
├── logs/
└── venv/
## Local Setup (From Beginning)
1. Clone Project / Upload Files
git clone <repo-url>
cd AI-Career-Advisor
2. Create Virtual Environment
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Run Locally
streamlit run app.py

Open:

http://localhost:8501
☁️ AWS Deployment (Full Steps)
1. Launch EC2 Instance

Ubuntu 24.04

Allow ports: 22, 8501

Create key pair

Connect via SSH

2. Upload Project to EC2

Using SCP / Git / Upload method

cd AI-Career-Advisor
3. Setup Environment in AWS
sudo apt update
sudo apt install python3-pip python3-venv -y

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
4. Run App on Server
streamlit run app.py --server.port 8501 --server.address 0.0.0.0

Test:

http://<EC2-PUBLIC-IP>:8501
## Run in Background (Auto Start)

Create service:

sudo nano /etc/systemd/system/ai-career.service

Paste:

[Unit]
Description=AI Career Advisor Chatbot
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/AI-Career-Advisor
Environment="PATH=/home/ubuntu/AI-Career-Advisor/venv/bin"
ExecStart=/home/ubuntu/AI-Career-Advisor/venv/bin/streamlit run app.py --server.port 8501 --server.address 0.0.0.0
Restart=always

[Install]
WantedBy=multi-user.target

Save → CTRL + X → Y → Enter

Enable & Start
sudo systemctl daemon-reload
sudo systemctl enable ai-career
sudo systemctl start ai-career
sudo systemctl status ai-career

You must see:

active (running)
enabled
## Live Application
http://<EC2-PUBLIC-IP>:8501

Example:

http://13.235.254.98:8501
## Verification Checklist
Test	Result
App opens in browser	✔
Works after closing terminal	✔
Auto starts after reboot	✔
Runs after 1 week	✔
## AWS Console Check

Go to:

AWS → EC2 → Instances

Verify:

Instance State → Running

Status Check → 2/2 passed

Security Group → Port 8501 open

## Service Check Command

Run inside AWS terminal:

sudo systemctl status ai-career

👨‍💻 Author

Name: BATHULA VENU GOPAL
Project: AI Career Advisor Chatbot
Deployment: AWS Cloud
Year: 2026
