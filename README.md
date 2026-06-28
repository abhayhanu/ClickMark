# ClickMark 🎯
### AI-Powered Attendance Management System

ClickMark automates classroom attendance using facial and voice recognition. Teachers capture photos or audio of the classroom and the system identifies enrolled students automatically.

---

## Features

**Teacher Portal**
- Register/login with secure bcrypt-hashed passwords
- Create and manage subjects with unique subject codes
- Take attendance via classroom photos (face recognition) or audio (voice recognition)
- Share subject enrollment codes via QR link
- View attendance records grouped by session

**Student Portal**
- Face ID login — no password needed
- Register with face capture and optional voice enrollment
- Enroll in subjects via code or QR link
- View personal attendance stats per subject

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Database | Supabase (PostgreSQL) |
| Face Detection | dlib, face_recognition_models |
| Face Classification | scikit-learn SVC |
| Voice Recognition | Resemblyzer, librosa |
| Auth | bcrypt |
| QR Codes | segno |

---

## Project Structure

```
├── app.py                  # Entry point
├── requirements.txt
└── src/
    ├── screens/
    │   ├── home_screen.py
    │   ├── teacher_screen.py
    │   └── student_screen.py
    ├── components/
    │   ├── subject_card.py
    │   ├── header.py
    │   ├── footer.py
    │   ├── dialog_create_subject.py
    │   ├── dialog_share_subject.py
    │   ├── dialog_add_photo.py
    │   ├── dialog_enroll.py
    │   ├── dialog_attendance_results.py
    │   └── dialog_voice_attendance.py
    ├── pipelines/
    │   ├── face_pipeline.py
    │   └── voice_pipeline.py
    ├── database/
    │   ├── config.py
    │   └── db.py
    └── ui/
        └── base_layout.py
```

---

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/abhayhanu/clickmark.git
cd clickmark
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Configure Supabase**

Create a `.env` file or set environment variables:
```
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_anon_key
```

**4. Run the app**
```bash
streamlit run app.py
```

---

## Database Tables

| Table | Description |
|---|---|
| `teachers` | Teacher accounts |
| `students` | Student profiles with face/voice embeddings |
| `subjects` | Subject records linked to teachers |
| `subject_students` | Enrollment join table |
| `attendance_log` | Per-session attendance records |

---

## How Attendance Works

1. Teacher selects a subject and uploads classroom photos
2. Each photo is processed — faces are detected using dlib and embedded into 128-d vectors
3. An SVC classifier matches embeddings against enrolled students
4. Results are logged to Supabase with a session timestamp
5. Alternatively, teacher can use voice attendance — students speak a phrase and Resemblyzer identifies them

---

## Author

Built by **Abhay Soni**
