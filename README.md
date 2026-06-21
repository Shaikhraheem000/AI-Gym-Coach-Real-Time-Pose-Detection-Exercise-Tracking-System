# 🏋️‍♂️ Apna AI Coach

![Apna AI Coach Banner](https://img.shields.io/badge/Status-Live-success?style=for-the-badge) ![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python) ![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit) ![Supabase](https://img.shields.io/badge/Supabase-Database-3ECF8E?style=for-the-badge&logo=supabase)

**Summary**  
Apna AI Coach is an intelligent, real-time fitness coaching application built with Streamlit. It tracks your exercise form using computer vision, provides proactive AI voice feedback, securely stores your workout history in the cloud, and offers insightful analytics.

🔗 **Quick Links**
* **Landing Page**: [https://apna-ai-coach.netlify.app/](https://apna-ai-coach.netlify.app/)
* **Live App (Streamlit)**: [Try the App Here](https://ai-gym-coach-real-time-pose-detection-exercise-tracking-system.streamlit.app/)
* **GitHub Repository**: [Source Code](https://github.com/Shaikhraheem000/AI-Gym-Coach-Real-Time-Pose-Detection-Exercise-Tracking-System)

---

## **Key Features**
* **Real-Time Pose Detection**: Form analysis for Squats, Push-ups, Lunges, Biceps Curls, and Shoulder Presses using MediaPipe.
* **Proactive AI Voice Coaching**: Instant, personalized verbal feedback using the Groq API.
* **Cloud Authentication & Database**: Secure user logins and workout tracking powered by Supabase.
* **Interactive Analytics Dashboard**: Beautiful visual trends of your workouts and calories burned using Plotly.
* **PDF Workout Reports**: Automatically generate clean summaries of your fitness history.

---

## **Technology Stack**
* **Frontend**: Streamlit, Custom CSS (Glassmorphism), Plotly Express
* **Backend**: Supabase (PostgreSQL), Python bcrypt
* **Computer Vision**: OpenCV, MediaPipe
* **AI Integration**: Groq API, TTS
* **Reporting**: FPDF2

---

## **Installation**
Clone the repository and install the required dependencies:
```bash
git clone https://github.com/yourusername/Apna-AI-Coach.git
cd Apna-AI-Coach
python -m venv .venv

# Activate Virtual Environment
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate
```

**Requirements**
Install the dependencies inside your virtual environment:
```bash
pip install -r App/requirements.txt
```

---

## **Environment Variables**
Create a `.env` file inside the `App/` directory with the following keys:
```env
GROQ_API_KEY=your_groq_api_key_here
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key
```

---

*created with 💖 shaikh raheem*
