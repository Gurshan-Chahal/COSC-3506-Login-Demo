# COSC 3506 Login Demo Project

## Project Overview

This project is a full-stack login demonstration application developed for the COSC 3506 Software Engineering course.

The application consists of:

- React frontend
- FastAPI backend
- SQLite database
- Password hashing using bcrypt
- REST API communication

---

## Technologies Used

### Frontend

- React
- Vite
- JavaScript
- CSS

### Backend

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Passlib
- bcrypt

---

## Project Structure

```
COSC 3506 Login Demo
│
├── backend
│   ├── app
│   ├── create_user.py
│   ├── login_demo.db
│   └── requirements.txt
│
├── frontend
│   ├── src
│   ├── package.json
│   └── vite.config.js
│
├── README.md
└── .gitignore
```

---

## Running the Backend

Open a terminal.

```
cd backend
py -m uvicorn app.main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## Running the Frontend

Open another terminal.

```
cd frontend
npm install
npm run dev
```

Frontend URL

```
http://localhost:5173
```

---

## Sample Login

Email

```
student@example.com
```

Password---->

Password123


## Features

- User Login
- Password Hashing
- SQLite Database
- REST API
- React Frontend
- Responsive Login Form

---

## Future Improvements

- User Registration
- JWT Authentication
- Logout Functionality
- User Dashboard

---

## Author

Gurshan Chahal

COSC 3506 Software Engineering