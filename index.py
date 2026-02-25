from flask import Flask,request,render_template,redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3


app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("mydatabases.db")
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Fullname TEXT NOT NULL,
    Username TEXT NOT NULL,
    Password TEXT NOT NULL,
    Role TEXT DEFAULT 'user'
    );
    """)
    
    conn.commit()
    conn.close()



@app.route('/register',methods=["GET", "POST"])
def home():

    if request.method == "POST":
        fullname = request.form["fullname"]
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("mydatabases.db")
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO users (Fullname, Username, Password)
            VALUES (?, ?, ?)
            """, (fullname, username, password))

        conn.commit()
        conn.close()

    return render_template("register.html")


@app.route('/logout')
def logout():
    session.clear()
    return redirect("/login")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)