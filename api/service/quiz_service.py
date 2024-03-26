from flask import request

from api.constant.ApplicationConstant import ApplicationConstant
from api.exception.QuizError import QuizError


class QuizService():

    def __init__(self):
        # Dummy data for the sake of example
        self.quizzes = [
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

    def get_quiz(self):
        return self.quizzes

    def get_quiz_by_id(self, id):
        for each_quiz in self.quizzes:
            db_quiz_id = each_quiz.get("id")
            if (db_quiz_id == id):
                return each_quiz
        raise QuizError(ApplicationConstant.quiz_not_found_message)

    def create_quiz(self):
        quiz = request.get_json()
        self.quizzes.append(quiz)
        return self.quizzes


    # todo delete this method
    #it method is just to should how to mock when testing using get_quiz_by_id function
    def show_mock(self, id):
        self.get_quiz_by_id(id)
        return self.quizzes[0]
