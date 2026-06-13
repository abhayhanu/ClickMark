import streamlit as st


def style_background_home():
    st.markdown(
        """
        <style>
            .stApp {
                background-color: #5865f2 !important;
                padding: 20px !important;
                border-radius: 5px !important;
            }

            .stApp div[data-testid="stColumn"] {
                background-color: #E0E3FF !important;
                padding: 2.5rem !important;
                border-radius: 5rem !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )



def style_background_dashboard():
    st.markdown(
        """
        <style>
            .stApp {
                background-color: #E0E3FF !important;
                padding: 20px !important;
                border-radius: 5px !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )



def style_base_layout():
    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Archivo+Black&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap');
            
            /* Hide top stream bar */
            #MainMenu, footer, header {
                visibility: hidden;
            }
            .block-container {
                padding-top: 1.5rem !important;
            }

            h1{
                font-family: 'Archivo Black', sans-serif !important;
                font-size: 2.5rem !important;
                font-weight: 900 !important;
                color: Black !important;
                line-height: 1.1 !important;
                margin-bottom: 0rem !important;
            }

            h2{
                font-family: 'Archivo Black', sans-serif !important;
                font-size: 2.5rem !important;
                font-weight: 900 !important;
                color: Black !important;
                line-height: 1.1 !important;
                margin-bottom: 0rem !important;
            }

            h3, h4, p{
                font-family: 'Montserrat', sans-serif !important;
                color: #E0E3FF !important;
            }

            button[kind="primary"] {
                font-family: 'Montserrat', sans-serif !important;
                background-color: #5865F2 !important;
                border-radius: 1.5rem !important;
                color: white !important;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2) !important;
                border: none !important;
                padding: 10px 20px !important;
                transition: transform 0.2s ease-in-out !important;
            }

            button[kind="secondary"] {
                font-family: 'Montserrat', sans-serif !important;
                background-color: #EB459E !important;
                border-radius: 1.5rem !important;
                color: white !important;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2) !important;
                border: none !important;
                padding: 10px 20px !important;
                transition: transform 0.2s ease-in-out !important;
            }

            button[kind="tertiary"] {
                font-family: 'Montserrat', sans-serif !important;
                background: black !important;
                border-radius: 1.5rem !important;
                color: white !important;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2) !important;
                border: none !important;
                padding: 10px 20px !important;
                transition: transform 0.2s ease-in-out !important;
            }

            button:hover{
                transform: scale(1.1);
            }

        </style>
        """,
        unsafe_allow_html=True
    )
