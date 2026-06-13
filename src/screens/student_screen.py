import streamlit as st
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
import numpy as np
from PIL import Image
from src.pipelines.face_pipeline import predict_attendance, get_face_embeddings, train_classifier
from src.pipelines.voice_pipeline import get_voice_embeddings
from src.database.config import supabase
from src.database.db import get_all_students, create_student_profile
import time

def student_dashboard():
    st.header("Student Dashboard")
    st.write("Welcome to your dashboard, ", st.session_state['student_data']['name'])
    

def student_screen():
    style_background_dashboard()
    style_base_layout()

    if "student_data" in st.session_state:
        student_dashboard()
        return

    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")
    with c1:
        header_dashboard()
    with c2:
        st.button("Go Back To Home", type="secondary", key = "Home", shortcut = "ctrl+backspace", on_click=lambda: st.session_state.update({'login_type': None}))
    st.header("login using FaceID", text_alignment="center")
    st.space()
    st.space()

    show_registration = False

    photo = st.camera_input("Position your face in the center and Take a picture")
    if photo:
        img_array = np.array(Image.open(photo))
        with st.spinner("Processing..."):
            detected, all_ids, num_faces = predict_attendance(photo)
            if num_faces ==0:
                st.warning("No face detected. Please try again.")
            elif num_faces > 1:
                st.warning("Multiple faces detected. Please try again.")
            else:
                if detected:
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students()
                    student = next((s for s in all_students if s['student_id'] == student_id), None)

                    if student:
                        st.session_state['is_logged_in'] = True
                        st.session_state['user_role'] = 'student'
                        st.session_state['student_data'] = student
                        st.toast(f"Welcome Back {student['name']}")
                        time.sleep(2)
                        st.rerun()
                else:
                    st.warning("Face not recognized. Please try again.")
                    show_registration = True
    if show_registration:
        with st.container(border=True):
            st.header("Register New Profile")
            new_name = st.text_input("Enter your name", placeholder="Your Name")
            new_photo = st.camera_input("Take a picture for your profile")

            st.subheader("Optional: Voice Enrollment")
            st.info("Enroll for Voice only attendance")

            audio_data = None

            try:
                audio_data = st.audio_input("Record your voice for enrollment like I am Present, My name is Abhay")
            except Exception as e:
                st.warning("Audio data Failed")

            if st.button('Create Account', type='primary'):
                if new_name and new_photo:
                    with st.spinner("Creating Profile..."):
                        img = np.array(Image.open(new_photo))
                        encodings = get_face_embeddings(img)
                        if encodings:
                            face_encoding = encodings[0].tolist()

                            voice_emb = None
                            if audio_data and audio_data.get("data"):
                                voice_emb = get_voice_embeddings(audio_data)
                            response_data = create_student_profile(new_name, face_embedding = face_encoding, voice_embedding = voice_emb)
                            if response_data:
                                train_classifier()
                                st.session_state['is_logged_in'] = True
                                st.session_state['user_role'] = 'student'
                                st.session_state['student_data'] = response_data[0]
                                st.toast(f"profile created! Hi {new_name}!")
                                time.sleep(2)
                                st.rerun()
                        else:
                            st.error('Could not Capture Your facial feature for registration')

                else:
                    st.warning("Please fill in all fields.")

    footer_dashboard()