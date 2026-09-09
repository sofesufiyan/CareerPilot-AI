# 🚀 CareerPilot AI

<p align="center">
  <strong>
    AI-powered Career Guidance Platform that analyzes resumes, identifies skill gaps,
    recommends career paths, generates personalized learning roadmaps,
    and prepares students for interviews using Google Gemini AI.
  </strong>
</p>

<p align="center">
  <a href="https://carrer-pilot-ai-red.vercel.app" target="_blank">
    <img src="https://img.shields.io/badge/🚀%20Live%20Demo-Visit%20Now-blue?style=for-the-badge" alt="Live Demo">
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react" alt="React">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase" alt="Firebase">
  <img src="https://img.shields.io/badge/Gemini-AI-blue?style=for-the-badge" alt="Gemini AI">
  <img src="https://img.shields.io/badge/Vercel-black?style=for-the-badge&logo=vercel" alt="Vercel">
  <img src="https://img.shields.io/badge/Render-46E3B7?style=for-the-badge" alt="Render">
</p>

---

## 🌟 Overview

CareerPilot AI is an intelligent career mentor built with modern AI technologies. It combines resume analysis, AI-powered career guidance, interview coaching, skill gap analysis, and personalized learning roadmaps into one platform.

The application is designed to help students and professionals make informed career decisions through interactive AI assistance and data-driven insights.

## ✨ Features

- 🔐 Secure Authentication (Email/Password & Google Sign-In)
- 📄 AI Resume Analysis & ATS Score
- 🤖 AI Career Mentor Chat
- 🛣️ Personalized Learning Roadmap
- 🎯 Skill Gap Analysis
- 💼 AI Interview Coach
- 📊 Interactive Career Dashboard
- 📥 PDF Resume Upload
- ☁️ Firebase Authentication
- ⚡ FastAPI Backend
- 🧠 Gemini AI Integration
- 📱 Responsive Modern UI

## 🛠️ Tech Stack

### Frontend
- React.js
- Vite
- Tailwind CSS
- React Router
- Lucide React

### Backend
- FastAPI
- Python
- Uvicorn

### AI & Machine Learning
- Google Gemini API
- Google ADK
- MCP (Model Context Protocol)

### Authentication
- Firebase Authentication
- Google OAuth

### Database & Storage
- Firebase

### Deployment
- Vercel (Frontend)
- FastAPI Backend — Render

### Version Control
- Git
- GitHub

## 🏗️ System Architecture

```text
                +---------------------------+
                |        React + Vite       |
                |      (Frontend UI)        |
                +------------+--------------+
                             |
                             |
                  Firebase Authentication
                             |
                             |
                +------------v--------------+
                |      FastAPI Backend      |
                |    (Business Logic/API)   |
                +------------+--------------+
                             |
          +------------------+------------------+
          |                  |                  |
          |                  |                  |
   Resume Analysis     Interview Coach    Career Mentor
          |                  |                  |
          +------------------+------------------+
                             |
                             |
                    Google Gemini API
                             |
                             |
                     AI Generated Results
```

# 📸 Project Screenshots

## 🏠 Landing Page

![Landing Page](frontend/screenshots/landing-page.png)
---

## 🔐 Login Page

![Login Page](frontend/screenshots/login-page.png)

---

## 📊 Dashboard

![Dashboard](frontend/screenshots/dashboard.png)

---

## 📄 Resume Analysis

![Resume Analysis](frontend/screenshots/resume-analysis.png)

---

## 🤖 AI Career Mentor

![AI Mentor](frontend/screenshots/ai-mentor.png)

---

## 🛣️ Learning Roadmap

![Learning Roadmap](frontend/screenshots/roadmap.png)

---

## 🎯 Skill Gap Analysis

![Skill Gap Analysis](frontend/screenshots/skill-gap.png)

---

## 💼 Interview Coach

![Interview Coach](frontend/screenshots/interview-coach.png)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/sofesufiyan/CareerPilot-AI.git
```

### 2. Navigate to the Project

```bash
cd CareerPilot-AI
```

### 3. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### 4. Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 5. Open the Application

Frontend:

```
http://localhost:5173
```

Backend:

```
http://localhost:8000
```
## 🔐 Environment Variables


### Frontend (`frontend/.env`)

```env
VITE_API_URL=
VITE_FIREBASE_API_KEY=
VITE_FIREBASE_AUTH_DOMAIN=
VITE_FIREBASE_PROJECT_ID=
VITE_FIREBASE_STORAGE_BUCKET=
VITE_FIREBASE_MESSAGING_SENDER_ID=
VITE_FIREBASE_APP_ID=
```

### Backend (`backend/.env`)

```env
GEMINI_API_KEY=
FIREBASE_PROJECT_ID=
```

> **Note:** Never commit real API keys or secrets to GitHub. Keep them in your local `.env` files or your deployment platform's environment variable settings.

## 📂 Project Structure

```text
CareerPilot-AI/
│
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   ├── api/
│   │   ├── auth/
│   │   ├── core/
│   │   ├── db/
│   │   ├── formatters/
│   │   ├── models/
│   │   ├── resume/
│   │   ├── router/
│   │   ├── services/
│   │   ├── tools/
│   │   └── main.py
│   │
│   ├── screenshots/
│   ├── .env.example
│   ├── .gitignore
│   ├── README.md
│   ├── package-lock.json
│   ├── requirements.txt
│   ├── test.py
│   └── test_gemini.py
│
├── frontend/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── context/
│   │   ├── firebase/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── App.css
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── main.jsx
│   │
│   ├── docs/
│   ├── public/
│   ├── screenshots/
│   ├── .gitignore
│   ├── README.md
│   └── ...
│
├── docs/
├── specs/
├── .gitignore
├── LICENSE
├── Procfile
├── README.md
├── backend_structure.txt
├── frontend_structure.txt
├── package-lock.json
├── railway.json
└── runtime.txt
```
---

## 💡 Project Highlights

- 🤖 **AI-Powered Career Guidance** — Provides personalized career recommendations using Google Gemini AI.
- 📄 **Resume Intelligence** — Analyzes uploaded resumes and generates ATS scoring, skills, and improvement suggestions.
- 🎯 **Skill Gap Analysis** — Identifies missing skills and highlights areas for improvement.
- 🛣️ **Personalized Learning Roadmaps** — Generates structured learning paths based on the user's career goals and skills.
- 💬 **AI Career Mentor** — Provides interactive AI-powered career guidance and resume-based assistance.
- 🎤 **AI Interview Coach** — Supports configurable mock interviews for technical and behavioral preparation.
- 🔐 **Secure Authentication** — Uses Firebase Authentication with Email/Password and Google OAuth.
- ⚡ **Full-Stack Architecture** — React frontend connected to a FastAPI backend and Gemini AI services.
- ☁️ **Cloud Deployment** — Frontend deployed on Vercel and backend deployed on Render.

---
---

## 🔄 How It Works

1. 🔐 **Sign Up / Sign In**  
   Users securely authenticate using Firebase Authentication.

2. 📄 **Upload Resume**  
   Upload a PDF resume for AI-powered analysis.

3. 🤖 **AI Analysis**  
   CareerPilot AI analyzes the resume using Google Gemini AI to identify skills, ATS score, skill gaps, and career opportunities.

4. 🎯 **Personalized Guidance**  
   Users receive career recommendations, learning roadmaps, AI mentoring, and interview preparation.

---
## 📊 Project Status

| Component | Status |
|-----------|--------|
| 🎨 Frontend | ✅ Completed |
| ⚡ FastAPI Backend | ✅ Completed |
| 🤖 Gemini AI Integration | ✅ Completed |
| 🔐 Firebase Authentication | ✅ Completed |
| 📄 Resume Analysis | ✅ Completed |
| 🎯 Skill Gap Analysis | ✅ Completed |
| 🛣️ Learning Roadmap | ✅ Completed |
| 🎤 AI Interview Coach | ✅ Completed |
| ☁️ Cloud Deployment | ✅ Live |

---
## 🚀 Future Scope

CareerPilot AI will continue to evolve with more intelligent career assistance features, including:

- 🎤 AI Voice Interview Coach
- 🌍 Multi-language Support
- 📈 Personalized Career Progress Tracking
- 🧑‍🤝‍🧑 Peer Resume Review System
- 🏢 Company-Specific Interview Preparation
- 📚 AI-Powered Course Recommendations
- 📅 Smart Study Planner
- 📊 Advanced Analytics Dashboard
- 📱 Mobile Application (Android & iOS)
- 🤝 Multi-Agent Collaboration for Career Planning

 ---

## 👨‍💻 Author

### Mohammed Sufiyan

🎓 B.Tech Artificial Intelligence & Machine Learning Student  
🤖 AI/ML & Full-Stack AI Developer  
🚀 Interested in Generative AI, AI Agents and Intelligent Applications

### 🔗 Connect With Me

- 💼 LinkedIn: Mohammed Sufiyan
- 🐙 GitHub: sofesufiyan
- 📧 Email: Sofesufiyan2799@gmail.com

---

⭐ If you find CareerPilot AI interesting, consider giving the repository a star! 
