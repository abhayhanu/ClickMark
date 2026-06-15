import streamlit as st
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen
from src.screens.home_screen import home_screen
from src.ui.base_layout import style_base_layout
from src.components.dialog_auto_enroll import auto_enroll_dialog

def main():
    st.set_page_config(
        page_title='ClickMark - Makes Attendance marking Easier',
        page_icon="https://tse3.mm.bing.net/th/id/OIP.iaUElCeQQflAvcfDKJ65FgHaDt?r=0&rs=1&pid=ImgDetMain&o=7&rm=3.png"
    )
    style_base_layout()

    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None
    
    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()
        case 'student':
            student_screen()
        case None:
            home_screen()

    join_code = st.query_params.get('join-code')
    if join_code:
        if st.session_state.login_type != 'student':
            st.session_state.login_type = 'student'
        if st.session_state.get('is_logged_in') and st.session_state.get('user_role') == 'student':
            auto_enroll_dialog(join_code)
main()