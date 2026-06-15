import streamlit as st

from src.database.config import supabase
import time
from src.database.db import enroll_student_to_subject


@st.dialog("Enroll in Subject")
def enroll_dialog():
    st.write("Enter the Subject Code")
    sub_code = st.text_input("Subject Code", placeholder = 'CS302L')
    
    if st.button("Enroll Now", type = 'primary', width='stretch'):
        if sub_code:
            try:
                res = supabase.table('subjects').select('subject_id, name, subject_code').eq('subject_code', sub_code).execute()
                if res.data:
                     subject = res.data[0]
                     student_id = st.session_state.student_data['student_id']

                     check = supabase.table('subject_students').select('*').eq('subject_id', subject['subject_id']).eq('student_id', student_id).execute()
                     if check.data:
                          st.warning('you are already Enrolled in this program')
                     else:
                          enroll_student_to_subject(student_id, subject['subject_id'])
                          st.success('Successfully Enrolled')
                          time.sleep(2)
                          st.rerun()   
                
                st.rerun()
            except Exception as e:
                st.error(f"Error: {str(e)}")
        else:
                st.warning("Please enter the Subject Code")
