class QuizError(Exception):
    def __init__(self, message="A error occurred"):
        self.message = message
        super().__init__(self.message)