# 🏋️‍♂️ Apna AI Coach

![App Demo](https://img.shields.io/badge/Status-Live-brightgreen) ![Python](https://img.shields.io/badge/Python-3.11+-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-App-red)

**Apna AI Coach** is a real-time computer vision fitness tracking application. It uses your webcam to track your exercise posture, count repetitions, and provides proactive AI voice coaching to ensure your form is perfect.

### 🔗 Quick Links
* **Landing Page:** [https://apna-ai-coach.netlify.app/](https://apna-ai-coach.netlify.app/)
* **Live App (Streamlit):** [Try the App Here](https://ai-gym-coach-real-time-pose-detection-exercise-tracking-system.streamlit.app/)
* **GitHub Repository:** [Source Code](https://github.com/Shaikhraheem000/AI-Gym-Coach-Real-Time-Pose-Detection-Exercise-Tracking-System/)

---

## ✨ Key Features
* **Real-Time Pose Detection:** Uses MediaPipe to track 33 body landmarks instantly.
* **Exercise Tracking:** Automatically counts reps and sets for multiple exercises:
  * Squats (Tracks Depth)
  * Push-ups (Tracks Body Alignment & Hip Status)
  * Biceps Curls (Tracks Arm Swing)
  * Shoulder Press (Tracks Extension & Back Arch)
  * Lunges (Tracks Balance)
* **Proactive Voice Coaching:** Powered by the incredibly fast Groq LLM API. The AI actively talks to you during your workout, encouraging you and correcting your form based on live metrics.
* **Privacy First:** All video processing is done entirely within your browser using WebRTC; video streams are never saved or uploaded.

---

## 🛠️ Technology Stack
* **Frontend/UI:** Streamlit, Vanilla HTML/CSS (Landing Page)
* **Computer Vision:** OpenCV, Google MediaPipe (Pose Landmarker)
* **Video Streaming:** `streamlit-webrtc`
* **AI Engine:** Groq API (LLM) & gTTS (Voice Synthesis)
* **Deployment:** Netlify (Frontend) & Streamlit Community Cloud (Backend)

---

## 🚀 Running Locally

If you want to run this app on your own machine:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Shaikhraheem000/AI-Gym-Coach-Real-Time-Pose-Detection-Exercise-Tracking-System.git
   cd AI-Gym-Coach-Real-Time-Pose-Detection-Exercise-Tracking-System
   ```

2. **Install dependencies:**
   ```bash
   pip install -r App/requirements.txt
   ```

3. **Set up Environment Variables:**
   Create a `.env` file inside the `App/` folder and add your API keys:
   ```env
   GROQ_API_KEY=your_groq_api_key
   ```

4. **Run the app:**
   ```bash
   streamlit run App/main.py
   ```

---
*Built with ❤️ to make personal fitness training accessible to everyone.*
