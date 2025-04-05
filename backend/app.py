from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

user_info = {}

@app.route('/signup', methods=['POST'])
def signup():
    info = request.json
    username = info.get('username')
    

@app.route('/add-expense', methods=['POST'])
def add_expense():
    info = request.json
    username = info['username']
    expense = info['expense']

    user_data.setdefault(username, []).append(expense)
    
    return jsonify({"message": "Expense added successfully!"})