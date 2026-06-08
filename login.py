from flask import Flask, request, redirect, render_template_string, session, url_for
import sqlite3
import bcrypt

app = Flask(__name__)
app.secret_key = "secure_secret_key"

# Database Setup
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password BLOB
)
""")

conn.commit()
conn.close()

# Register Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']

        if len(username) < 3 or len(password) < 6:
            return "Username must be 3+ chars and Password 6+ chars"

        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        try:
            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO users(username, password) VALUES (?, ?)",
                (username, hashed)
            )

            conn.commit()
            conn.close()

            return redirect('/login')

        except:
            return "Username already exists"

    return render_template_string("""
    <h2>Register</h2>
    <form method="post">
        Username:<br>
        <input type="text" name="username"><br><br>
        Password:<br>
        <input type="password" name="password"><br><br>
        <input type="submit" value="Register">
    </form>
    <a href="/login">Login</a>
    """)

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT password FROM users WHERE username=?",
            (username,)
        )

        user = cursor.fetchone()
        conn.close()

        if user and bcrypt.checkpw(password.encode('utf-8'), user[0]):
            session['user'] = username
            return redirect('/dashboard')

        return "Invalid Username or Password"

    return render_template_string("""
    <h2>Login</h2>
    <form method="post">
        Username:<br>
        <input type="text" name="username"><br><br>
        Password:<br>
        <input type="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
    <a href="/register">Register</a>
    """)

# Dashboard
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')

    return render_template_string(f"""
    <h2>Welcome, {session['user']}</h2>
    <a href="/logout">Logout</a>
    """)

# Logout
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)