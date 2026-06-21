import streamlit as st
from services.persistence.exercise_repository import authenticate_user, create_user, get_user

def render_login_wall():
    if st.session_state.get("user_id") is not None:
        return True
        
    st.markdown(
        """
        <style>
            [data-testid="collapsedControl"] { display: none; }
            [data-testid="stSidebar"] { display: none; }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    st.title("🏋️‍♂️ Apna AI Coach")
    st.markdown("### Welcome! Please log in or sign up to continue.")

    tab1, tab2 = st.tabs(["Log In", "Sign Up"])

    with tab1:
        with st.form("login_form", clear_on_submit=False):
            login_username = st.text_input("Username")
            login_password = st.text_input("Password", type="password")
            login_submit = st.form_submit_button("Log In", width="stretch")

        if login_submit:
            if not login_username or not login_password:
                st.error("Please enter both username and password.")
            else:
                user = authenticate_user(login_username, login_password)
                if user:
                    st.session_state["user_id"] = user["id"]
                    st.session_state["username"] = user["username"]
                    st.session_state["weight_kg"] = user.get("weight_kg", 70.0)
                    st.rerun()
                else:
                    st.error("Invalid username or password.")

    with tab2:
        with st.form("signup_form", clear_on_submit=False):
            signup_username = st.text_input("Choose a Username")
            signup_password = st.text_input("Choose a Password", type="password")
            signup_weight = st.number_input("Your Weight (kg)", min_value=30.0, max_value=250.0, value=70.0, help="Used to accurately calculate calories burned.")
            signup_submit = st.form_submit_button("Sign Up", width="stretch")

        if signup_submit:
            if not signup_username or not signup_password:
                st.error("Please fill out all fields.")
            else:
                existing_user = get_user(signup_username)
                if existing_user:
                    st.error("Username already taken. Please choose another one.")
                else:
                    new_user = create_user(signup_username, signup_password, float(signup_weight))
                    if new_user:
                        st.success("Account created successfully! You can now log in.")
                    else:
                        st.error("Failed to create account. Please try again.")

    return False