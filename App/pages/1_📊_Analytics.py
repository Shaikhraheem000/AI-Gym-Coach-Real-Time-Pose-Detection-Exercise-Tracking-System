import streamlit as st
import pandas as pd
import plotly.express as px
from services.persistence.exercise_repository import get_users_exercises
from services.reporting.pdf_generator import generate_workout_pdf

st.set_page_config(page_title="Analytics - Apna AI Coach", page_icon="📊", layout="wide")

# Ensure the user is logged in
if "user_id" not in st.session_state:
    st.warning("Please log in from the main page to view your analytics.")
    st.stop()

with st.sidebar:
    st.title("🏋️‍♂️ Apna AI Coach")
    st.caption(f"👤 Login as **{st.session_state.get('username', 'User')}**")
    if st.button("Logout", key="logout_analytics", use_container_width=True):
        st.session_state.pop("user_id", None)
        st.session_state.pop("username", None)
        st.rerun()

st.title("📊 Workout Dashboard")
st.markdown("Track your progress, analyze your trends, and download your reports.")
st.markdown("---")

user_id = st.session_state["user_id"]
username = st.session_state.get("username", "User")

exercises = get_users_exercises(user_id)

if not exercises:
    st.info("You haven't completed any workouts yet! Go to the live coach and do some reps.")
    st.stop()

# Prepare Data
df = pd.DataFrame(exercises)
df['created_at'] = pd.to_datetime(df['created_at'])
df['date'] = df['created_at'].dt.date
df['exercise_name'] = df['exercise_name'].str.replace('_', ' ').str.title()

# High-Level Metrics
total_calories = df['calories_burned'].sum()
total_time_mins = df['time_seconds'].sum() / 60.0
total_reps = df['reps'].sum()
total_workouts = df.shape[0]

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("🔥 Total Calories", f"{total_calories:.1f} kcal")
with col2:
    st.metric("⏱️ Total Time", f"{total_time_mins:.1f} mins")
with col3:
    st.metric("💪 Total Reps", f"{total_reps}")
with col4:
    st.metric("📈 Workouts Logged", f"{total_workouts}")

st.markdown("---")

# Visualizations Layout
st.subheader("📈 Workout Trends")

tab1, tab2 = st.tabs(["Time Spent by Exercise", "Calories Burned Over Time"])

with tab1:
    time_per_day = df.groupby(['date', 'exercise_name'])['time_seconds'].sum().reset_index()
    time_per_day['time_minutes'] = time_per_day['time_seconds'] / 60.0
    
    fig_time = px.bar(
        time_per_day, 
        x='date', 
        y='time_minutes', 
        color='exercise_name',
        title="Workout Time (Minutes) per Day",
        labels={'date': 'Date', 'time_minutes': 'Time (Mins)', 'exercise_name': 'Exercise'},
        barmode='stack',
        template='plotly_dark'
    )
    # Improve x-axis formatting for single-day data
    fig_time.update_xaxes(type='category')
    st.plotly_chart(fig_time, use_container_width=True)

with tab2:
    cals_per_day = df.groupby('date')['calories_burned'].sum().reset_index()
    
    fig_cals = px.bar(
        cals_per_day,
        x='date',
        y='calories_burned',
        title="Total Calories Burned per Day",
        labels={'date': 'Date', 'calories_burned': 'Calories (kcal)'},
        text_auto=True,
        template='plotly_dark'
    )
    # Improve x-axis formatting for single-day data
    fig_cals.update_xaxes(type='category')
    st.plotly_chart(fig_cals, use_container_width=True)


st.markdown("---")

# PDF Generation
st.subheader("📄 Download Weekly Report")
st.write("Generate a clean PDF report of all your workouts, calories burned, and total times.")

if st.button("Generate PDF Report", type="primary"):
    with st.spinner("Generating PDF..."):
        pdf_path = generate_workout_pdf(username, exercises)
        with open(pdf_path, "rb") as f:
            pdf_bytes = f.read()
            
        st.download_button(
            label="⬇️ Download PDF",
            data=pdf_bytes,
            file_name=f"Apna_Coach_Report_{username}.pdf",
            mime="application/pdf"
        )
