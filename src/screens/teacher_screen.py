import streamlit as st
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.database.db import check_teacher_exists, create_teacher, teacher_login
import time

def teacher_screen():
    style_background_dashboard()
    style_base_layout()

    if "teacher_data" in st.session_state:
        # Show teacher dashboard
        teacher_dashboard()
    elif 'teacher_login_type' not in st.session_state or st.session_state['teacher_login_type'] == 'login':
        teacher_screen_login()
    elif st.session_state['teacher_login_type'] == 'register':
        teacher_screen_register()
   
def teacher_dashboard():
    teacher_data = st.session_state['teacher_data']

    st.header(f"Welcome {teacher_data['name']}")

def login_teacher(teacher_username, teacher_password):
    if not teacher_username or not teacher_password:
        return False
    teacher = teacher_login(teacher_username, teacher_password)
    if teacher:
        st.session_state['teacher_data'] = teacher
        st.session_state['user_role'] = 'teacher'
        st.session_state['is_logged_in'] = True
        return True

    return False

def register_teacher(teacher_name, teacher_username, teacher_email, teacher_password, teacher_pass_confirm):
    if not teacher_username or not teacher_password or not teacher_name:
        return False, "All fields are required"
    if teacher_password != teacher_pass_confirm:
        return False, "Passwords do not match"
    if check_teacher_exists(teacher_username):
        return False, "Username already exists"
    try:
        create_teacher(teacher_username, teacher_password, teacher_name)
        return True, "Registration successful, Login to continue"
    except Exception as e:
        return False, "Error occurred during registration"

def teacher_screen_login():
    style_background_dashboard()
    style_base_layout()

    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")
    with c1:
        header_dashboard()
    with c2:
        st.button("Go Back To Home", type="secondary", key = "Home", shortcut = "ctrl+backspace", on_click=lambda: st.session_state.update({'login_type': None}))
    st.header("Enter Your Password", text_alignment="center")
    st.space()
    st.space()
    teacher_username = st.text_input("Username", placeholder="Enter your username", key="teacher_username")
    teacher_password = st.text_input("Password", placeholder="Enter your password", type="password", key="teacher_password")
    st.divider()

    btnc1, btnc2 = st.columns(2, gap="large")
    with btnc1:
        if st.button("Login", type="primary", key="teacher_login", icon = ':material/passkey:', shortcut = "ctrl+enter", width='stretch'):
            if login_teacher(teacher_username, teacher_password):
                st.toast("welcome back!")
                time.sleep(2)
                st.rerun()
            else:
                st.error("Invalid username or password")

    with btnc2:
        if st.button("Register", type="secondary", key="teacher_register", icon = ':material/passkey:', shortcut = "ctrl+enter", width='stretch'):
            st.session_state['teacher_login_type'] = 'register'
    footer_dashboard()

def teacher_screen_register():
    style_background_dashboard()
    style_base_layout()

    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")
    with c1:
        header_dashboard()
    with c2:
        st.button("Go Back To Home", type="secondary", key = "Home", shortcut = "ctrl+backspace", on_click=lambda: st.session_state.update({'login_type': None}))
    st.header("Register Your Teacher Profile")

    st.space()
    st.space()
    teacher_name = st.text_input("Name", placeholder="Enter your name", key="teacher_name")
    teacher_username = st.text_input("Username", placeholder="Enter your username", key="teacher_username")
    teacher_email = st.text_input("Email", placeholder="Enter your email", key="teacher_email")
    teacher_password = st.text_input("Password", placeholder="Enter your password", type="password", key="teacher_password")
    teacher_pass_confirm = st.text_input("Confirm Password", placeholder="Confirm your password", type="password", key="teacher_pass_confirm")

    st.divider()

    btnc1, btnc2 = st.columns(2, gap="large")
    with btnc1:
        if st.button("Register Now", type="primary", key="teacher_login", icon = ':material/passkey:', shortcut = "ctrl+enter", width='stretch'):
            success, message = register_teacher(teacher_name, teacher_username, teacher_email, teacher_password, teacher_pass_confirm)
            if success:
                st.success(message)
                time.sleep(2)
                st.session_state['teacher_login_type'] = 'login'
                st.rerun()
            else:
                st.error(message)

    with btnc2:
        if st.button("Login Instead", type="secondary", key="teacher_register", icon = ':material/passkey:', shortcut = "ctrl+enter", width='stretch'):
            st.session_state['teacher_login_type'] = 'login'
    footer_dashboard()

