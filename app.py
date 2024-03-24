from flask import Flask, jsonify, request
from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://kadamkeyur:{password}@cluster0.dw6ghym.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_string)

# dbs = client.list_database_names()
print(connection_string)
app = Flask(__name__)

# Dummy data for the sake of example
quizzes = [
    {
        "id": 1,
        "title": "General Knowledge Quiz",
        "description": "Test your general knowledge with this quiz."
    },
    {
        "id": 2,
        "title": "Science Quiz",
        "description": "A quiz for science enthusiasts."
    }
]

@app.route('/')
def index():
    return "Welcome to the Quiz App!"

@app.route('/quizzes', methods=['GET'])
def get_quizzes():
    return jsonify({"quizzes": quizzes})

@app.route('/quizzes', methods=['POST'])
def add_quiz():
    quiz = request.get_json()
    quizzes.append(quiz)
    return jsonify({"quizzes": quizzes}), 201

if __name__ == '__main__':
    app.run(debug=True)
