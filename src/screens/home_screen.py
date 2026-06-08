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
        st.image("https://tse3.mm.bing.net/th/id/OIP.iaUElCeQQflAvcfDKJ65FgHaDt?r=0&rs=1&pid=ImgDetMain&o=7&rm=3.png", width=150)
        if st.button('Teacher Portal', type='primary'):
            st.session_state['login_type'] = 'teacher'
            st.rerun()

    with col2:
        st.header("Student Portal")
        st.image("https://tse3.mm.bing.net/th/id/OIP.iaUElCeQQflAvcfDKJ65FgHaDt?r=0&rs=1&pid=ImgDetMain&o=7&rm=3.png", width=150)
        if st.button('Student Portal', type='primary'):
            st.session_state['login_type'] = 'student'
            st.rerun()
    
    footer_home()