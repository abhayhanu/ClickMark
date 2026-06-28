import streamlit as st
from src.components.footer import footer_home
from src.components.header import header_home
from src.ui.base_layout import style_base_layout, style_background_home

def home_screen():

    header_home()
    style_background_home()
    style_base_layout()

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.header("Teacher Portal")
        st.image("https://thumbs.dreamstime.com/b/charming-d-animated-female-teacher-character-presentation-cheerful-ready-to-present-holds-marker-notebook-dressed-357823021.jpg", width=150)
        if st.button('Teacher Portal', type='primary'):
            st.session_state['login_type'] = 'teacher'
            st.rerun()

    with col2:
        st.header("Student Portal")
        st.image("https://img.freepik.com/premium-vector/student-girl-cartoon-character-isolated-white-background_918868-2081.jpg", width=150)
        if st.button('Student Portal', type='primary'):
            st.session_state['login_type'] = 'student'
            st.rerun()
    
    footer_home()