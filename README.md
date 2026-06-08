# Secure Login System

## Project Overview
The Secure Login System is a web application built using Python, Flask, SQLite, and bcrypt. It provides a secure authentication mechanism where users can register, log in, and log out safely. Passwords are stored in hashed format to protect user credentials, and parameterized SQL queries are used to prevent SQL injection attacks.

## Features
- User Registration
- Secure User Login
- Password Hashing with bcrypt
- SQLite Database Integration
- Input Validation
- SQL Injection Protection
- Session Management
- Logout Functionality
- Simple and Easy-to-Use Interface

## Technologies Used
- Python 3
- Flask
- SQLite3
- bcrypt

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/Secure-Login-System.git
cd Secure-Login-System
```

### 2. Install Required Packages
```bash
pip install flask bcrypt
```

## Project Structure
```text
Secure-Login-System/
│
├── app.py
├── users.db
└── README.md
```

## How to Run

Start the Flask application:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## Security Features

### Password Hashing
User passwords are hashed using bcrypt before being stored in the database.

### SQL Injection Prevention
Parameterized SQL queries are used to protect against SQL injection attacks.

### Session Management
Authenticated users are managed using Flask sessions and can securely log out.

### Input Validation
Basic validation ensures usernames and passwords meet minimum requirements.

## Usage

### Register
1. Open the application.
2. Navigate to the Register page.
3. Enter a username and password.
4. Submit the form to create an account.

### Login
1. Navigate to the Login page.
2. Enter your credentials.
3. Access the dashboard upon successful authentication.

### Logout
Click the Logout button to end the session securely.

## Expected Outcome
The application provides a secure login environment by:
- Storing passwords in hashed format.
- Preventing SQL injection attacks.
- Managing authenticated sessions securely.
- Allowing users to register, log in, and log out safely.

## Future Enhancements
- Two-Factor Authentication (2FA)
- Password Reset Functionality
- Email Verification
- Account Lockout After Multiple Failed Attempts
- Role-Based Access Control

## Author
Prasad N

## License
This project is developed for educational and learning purposes.
