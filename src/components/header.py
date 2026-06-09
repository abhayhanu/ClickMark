import streamlit as st


def header_home():

    logo_url = "https://tse3.mm.bing.net/th/id/OIP.iaUElCeQQflAvcfDKJ65FgHaDt?r=0&rs=1&pid=ImgDetMain&o=7&rm=3.png"

    st.markdown(f"""
        <div style='display: flex; flex-direction: column; align-items: center; justify-content: center; margin-bottom: 20px; margin-top: 20px;'>
                <img src='{logo_url}' alt='Logo' style='width: 100px;'>
                <h1 style='font-family: "Archivo Black", sans-serif; color: #E0E3FF;'>ClickMark</h1>
        </div>
            """,unsafe_allow_html=True)

def header_dashboard():

    logo_url = "https://tse3.mm.bing.net/th/id/OIP.iaUElCeQQflAvcfDKJ65FgHaDt?r=0&rs=1&pid=ImgDetMain&o=7&rm=3.png"

    st.markdown(f"""
        <div style='display: flex; align-items: center; justify-content: center; gap: 10px;'>
                <img src='{logo_url}' alt='Logo' style='width: 85px;'>
                <h2 style='font-family: "Archivo Black", sans-serif; color: #5865F2;'>ClickMark</h2>
        </div>
            """,unsafe_allow_html=True)
