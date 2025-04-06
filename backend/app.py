from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os


app = Flask(__name__)
CORS(app) 

user_info = {}


USER_FILE = 'users.json'

def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(data):
    with open(USER_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/signup', methods=['POST'])
def signup():
    info = request.json
    username = info.get('username')
    email = info.get("email")
    password = info.get('password')

    user_info = load_users()

    if username in user_info:
        return jsonify({"message": "Already in system"})
    else:
        user_info[username] = {
            "email":email,
            "password": password
        }
        save_users(user_info)
        return jsonify({"message": "Succesful!"})


    

@app.route('/add-expense', methods=['POST'])
def add_expense():
     info = request.json
     username = info['username']
    # expense = info['expense']

    # user_data.setdefault(username, []).append(expense)
    
     return jsonify({"message": "Expense added successfully!"})


if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = "8080", debug = True)