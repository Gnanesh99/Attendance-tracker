# Attendance Tracker 📋

A Flask web application for tracking daily attendance with user authentication, attendance history, and percentage calculation.

## Features

- User registration and login with hashed passwords
- Mark daily attendance — Present, Absent, or Late
- View full attendance history
- Attendance percentage calculation
- Protected routes — login required throughout
- Duplicate attendance prevention per day

## Tech Stack

- **Backend** — Python, Flask
- **Database** — SQLite via Flask-SQLAlchemy
- **Auth** — Flask-Bcrypt, Flask Sessions
- **Templating** — Jinja2
- **Environment** — python-dotenv

## Project Structure

```
attendance-tracker/
├── app.py               # App factory, config, blueprint registration
├── extensions.py        # Shared db and bcrypt instances
├── utils.py             # login_required decorator
├── .env                 # Secret keys (not committed)
├── .gitignore
├── requirements.txt
├── models/
│   └── user.py          # User and Attendance models
├── routes/
│   ├── auth.py          # Register, login, logout
│   └── attendance.py    # Dashboard, mark attendance
└── templates/
    ├── base.html
    ├── login.html
    ├── register.html
    └── dashboard.html
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/attendance-tracker.git
cd attendance-tracker
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root folder:

```
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///users.db
```

Generate a secure secret key:
```python
import secrets
print(secrets.token_hex(32))
```

### 5. Run the app

```bash
python app.py
```

Visit `http://127.0.0.1:5000`

## Usage

1. Register a new account
2. Login with your credentials
3. Mark your attendance for the day — Present, Absent, or Late
4. View your attendance history and percentage on the dashboard
5. Attendance can only be marked once per day

## API Routes

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/dashboard` | View dashboard |
| POST | `/mark` | Mark attendance |
| GET | `/register` | Show register form |
| POST | `/register` | Create new account |
| GET | `/login` | Show login form |
| POST | `/login` | Authenticate user |
| GET | `/logout` | Logout user |

## Author

Gorle Gnanesh
