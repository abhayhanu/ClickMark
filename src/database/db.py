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

def create_teacher(username, password, name):
    # hashing the password
    data = {
        "username": username,
        "password": hash_pass(password),
        "name": name
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