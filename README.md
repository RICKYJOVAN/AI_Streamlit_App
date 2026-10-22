# Practical 4: Deploy a Simple AI-enabled Web Application using Streamlit Community Cloud / AWS EC2

## Aim
To deploy a simple AI-enabled web application using Streamlit Community Cloud (and alternatively AWS EC2).

---

## Project Structure
```text
AI_Streamlit_App/
│
├── app.py             # Main Streamlit web application code
├── requirements.txt   # Dependencies (streamlit)
├── .gitignore         # Ignores virtualenv and cache files
└── README.md          # Project manual and deployment procedure
```

---

## 1. Running Locally (Verification)

### Step 1: Open Terminal in the project folder
```bash
cd x:\Productivity\COLLEGE\Practicals\AI_Streamlit_App
```

### Step 2: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Launch the Streamlit application
```bash
streamlit run app.py
```
> The app will run locally at `http://localhost:8501`.

---

## 2. Deployment on Streamlit Community Cloud (Recommended)

### Step 1: Create a GitHub Repository
1. Log in to your [GitHub](https://github.com/) account.
2. Click **New Repository** (`+` icon at top right).
3. Repository name: `AI_Streamlit_App`.
4. Visibility: **Public**.
5. Do not initialize with README (we will push from local).
6. Click **Create repository**.

### Step 2: Push Project Files to GitHub
Open your terminal in `AI_Streamlit_App` and run:
```bash
git init
git add .
git commit -m "Initial commit for Streamlit app"
git branch -M main
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/AI_Streamlit_App.git
git push -u origin main
```

### Step 3: Sign in to Streamlit Community Cloud
1. Navigate to [https://share.streamlit.io/](https://share.streamlit.io/).
2. Click **Sign in with GitHub**.
3. Authorize Streamlit to access your GitHub repositories.

### Step 4: Deploy the Application
1. In the Streamlit dashboard, click **Create app** (or **New app**).
2. Choose **I already have an app**.
3. Select your repository: `<YOUR_GITHUB_USERNAME>/AI_Streamlit_App`.
4. Branch: `main`.
5. Main file path: `app.py`.
6. Click **Deploy!**.

### Step 5: Access & Test the Application
1. Wait 1-2 minutes for Streamlit to install dependencies and deploy.
2. Streamlit will generate a live public URL (e.g., `https://ai-streamlit-app-xxxx.streamlit.app`).
3. Enter your name in the text input box.
4. Click **Submit** and verify the greeting message appears.

---

## 3. Alternative: Deployment on AWS EC2 (Ubuntu Linux)

If required to demonstrate deployment on an AWS EC2 instance:

### Step 1: Launch an EC2 Instance
1. In the AWS Management Console, go to **EC2** → **Launch Instance**.
2. Select **Ubuntu 22.04 LTS** / **Ubuntu 24.04 LTS** (t2.micro / Free tier eligible).
3. Create or select an existing Key Pair (`.pem`).
4. In **Network Settings**, configure the Security Group:
   - Allow **SSH** (port 22) from your IP.
   - Allow Custom TCP **Port 8501** from `0.0.0.0/0` (Streamlit default port).
   - Allow **HTTP** (port 80) if using a reverse proxy (Nginx).

### Step 2: Connect to EC2 & Set Up Environment
Connect via SSH:
```bash
ssh -i "your-key.pem" ubuntu@<EC2-PUBLIC-IP>
```

Update system and install Python + pip:
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-pip python3-venv git
```

### Step 3: Clone Repository and Install Requirements
```bash
git clone https://github.com/<YOUR_GITHUB_USERNAME>/AI_Streamlit_App.git
cd AI_Streamlit_App
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Step 4: Run Streamlit as a Background Service
Run in headless mode:
```bash
nohup streamlit run app.py --server.port 8501 --server.address 0.0.0.0 &
```

### Step 5: Access the EC2 Deployment
Open your browser and visit:
```text
http://<EC2-PUBLIC-IP>:8501
```
