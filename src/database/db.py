from src.database.config import supabase
import bcrypt

def hash_pass(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def check_pass(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed.encode())

def check_teacher_exists(username):
    # check for unique username else returns false
    response = supabase.table("teachers").select("username").eq("username", username).execute()
    return len(response.data) > 0

def create_teacher(username, password, name, email):
    # hashing the password
    data = {
        "username": username,
        "password": hash_pass(password),
        "name": name,
        "email": email
    }
    response = supabase.table("teachers").insert(data).execute()
    return response.data

def teacher_login(username, password):
    response = supabase.table("teachers").select("*").eq("username", username).execute()
    if response.data:
        teacher = response.data[0]
        if check_pass(password, teacher["password"]):
            return teacher
    return None

def get_all_students():
    response = supabase.table("students").select("*").execute()
    return response.data

def create_student_profile(new_name, face_embeddings=None, voice_embedding = None):
    data = {'name': new_name, 'face_embeddings': face_embeddings, 'voice_embeddings': voice_embedding}
    response = supabase.table('students').insert(data).execute() 
    return response.data

def create_subject(sub_code, name, section, teacher_id):
    data = {"subject_code": sub_code, "name": name, "section": section, "teacher_id": teacher_id}
    response = supabase.table("subjects").insert(data).execute()
    return response.data

def get_teacher_subject(teacher_id):
    response = supabase.table('subjects').select('*, subject_students(count), attendance_log(timestamp)').eq("teacher_id", teacher_id).execute()
    subjects = response.data

    for sub in subjects:
        sub['total_students'] = sub.get("subjects_student", [{}])[0].get('count', 0) if sub.get('subject_students') else 0
        attendance = sub.get('attendance_log', [])
        unique_sessions = len(set(log['timestamp'] for log in attendance))
        sub['total_classes'] = unique_sessions

        sub.pop('subject_student', None)
        sub.pop('attendence_log', None)

    return subjects

def enroll_student_to_subject(student_id, subject_id):
    data = {'student_id': student_id, "subject_id": subject_id}
    response = supabase.table('subject_studets').insert(data).execute()
    return response.data

def unenroll_student_to_subject(student_id, subject_id):
    response = supabase.table('subject_studets').delete().eq('student_id', student_id).eq('subject_id', subject_id).execute()
    return response.data

def get_student_subjects(student_id):
    response = supabase.table('subject_students').select('*, subjects(*)').eq('student_id', student_id).execute()
    return response.data


def get_student_attendance(student_id):
    response = supabase.table('attendance_logs').select('*, subjects(*)').eq('student_id', student_id).execute()
    return response.data


def create_attendance(logs):
    response = supabase.table('attendance_logs').insert(logs).execute()
    return response.data

def get_attendance_for_teacher(teacher_id):
    response = supabase.table('attendance_log').select("*, subjects!inner(*)").eq('subjects.teacher_id', teacher_id).execute()
    return response.data