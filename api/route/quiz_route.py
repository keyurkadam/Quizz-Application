from flask import Blueprint, jsonify

from api.exception.QuizError import QuizError
from api.service.quiz_service import QuizService

quiz_route = Blueprint("quiz_route", __name__)


quiz_service = QuizService()

@quiz_route.route('/', methods=['GET'])
def get_quizzes():
    quizzes = quiz_service.get_quiz()
    return jsonify({"quizzes": quizzes})

@quiz_route.route('/<int:id>', methods=['GET'])
def get_quizzes_by_id(id):
    try:
        quizzes = quiz_service.get_quiz_by_id(id)
    except QuizError as e:
        return jsonify({'error': str(e)}), 404
    return jsonify({"quizzes": quizzes})

@quiz_route.route('/', methods=['POST'])
def add_quiz():
    quizzes = quiz_service.create_quiz()
    return jsonify({"quizzes": quizzes}), 201