import os
import subprocess
import pickle
import hashlib
import random
import string
import sqlite3
from flask import Flask, request, render_template

app = Flask(__name__)

# 1. Hardcoded secret key
SECRET_KEY = "supersecretkey"  # Sensitive information should not be hardcoded

# 2. Using a predictable password hash
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # MD5 is not secure

# 3. Insecure random token generation
def generate_token(length=16):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

# 4. Unsafe pickle usage
def save_user_data(user_data):
    with open("user_data.pkl", "wb") as f:
        pickle.dump(user_data, f)  # Insecure: pickle can execute arbitrary code

def load_user_data():
    with open("user_data.pkl", "rb") as f:
        return pickle.load(f)

# 5. SQL Injection vulnerability
def get_user_from_db(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"  # Insecure: SQL Injection
    cursor.execute(query)
    return cursor.fetchone()

# 6. Insecure command execution
def list_directory(path):
    return subprocess.check_output(f"ls -la {path}", shell=True)  # Insecure: Shell injection

@app.route('/')
def index():
    return render_template('index.html')

# 7. Flask app running with debug mode enabled
if __name__ == "__main__":
    app.run(debug=True)  # Debug mode should not be used in production

# 8. Hardcoded database credentials
DATABASE_USER = "admin"
DATABASE_PASS = "password123"  # Credentials should be stored securely

def connect_to_db():
    conn_string = f"dbname='mydb' user='{DATABASE_USER}' host='localhost' password='{DATABASE_PASS}'"
    return subprocess.call(f"psql {conn_string}", shell=True)  # Dangerous: credentials in command line

# 9. Insecure file handling
def read_config_file(filepath):
    with open(filepath, 'r') as file:
        config = file.read()  # Potential security risk if filepath is user-controlled
    return config

# 10. Logging sensitive information
def login(username, password):
    print(f"Attempting login with username: {username} and password: {password}")  # Logging sensitive info
    stored_password_hash = hash_password(password)
    user = get_user_from_db(username)
    if user and user['password'] == stored_password_hash:
        return "Login successful"
    else:
        return "Login failed"

# 11. Unrestricted file upload (hypothetical example)
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save(os.path.join('/uploads', file.filename))  # Save file without validating its type

# 12. Insecure deserialization (another example)
def insecure_deserialize(data):
    return pickle.loads(data)  # Insecure: deserializing untrusted data

# 13. Insecure HTTP connections
def fetch_data_from_api(api_url):
    response = os.system(f"curl {api_url}")  # Insecure: No SSL/TLS validation
    return response

# 14. Insufficient input validation
def unsafe_redirect(url):
    return redirect(url)  # Potential Open Redirect vulnerability

# 15. Weak password generation
def generate_weak_password():
    return "password123"  # Easily guessable password

# 16. Unrestricted admin access (Hypothetical)
def admin_access(user_role):
    if user_role == "admin":
        print("Access granted to admin")
    else:
        print("Access denied")

# 17. Arbitrary file write
def save_user_profile(profile_data):
    with open("/etc/passwd", "a") as f:  # Dangerous: Writing to sensitive system file
        f.write(profile_data)

# 18. Use of deprecated functions
def deprecated_function_example():
    password = input("Enter your password: ")  # Insecure: use of input() for sensitive data

# 19. Insufficiently protected API keys
API_KEY = "1234567890abcdef"  # API key should be stored securely

# 20. Hardcoded sensitive URLs
SECRET_ADMIN_URL = "http://example.com/admin"  # Exposing sensitive URLs in code

