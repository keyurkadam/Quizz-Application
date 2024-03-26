from unittest.mock import patch

import pytest

from api.constant.ApplicationConstant import ApplicationConstant
from api.exception.QuizError import QuizError
from api.service.quiz_service import QuizService

quiz_service = QuizService()

@patch("api.service.quiz_service.QuizService.get_quiz_by_id")
def test_show_mock_success (mock_get_quiz_by_id):
    quiz__ = {
        "id": 1,
        "title": "General Knowledge Quiz",
        "description": "Test your general knowledge with this quiz."
    }
    mock_get_quiz_by_id.return_value = quiz__
    test_id = 1
    reponse = quiz_service.show_mock(test_id)
    mock_get_quiz_by_id.assert_called_once()
    assert reponse["id"] == quiz__["id"]
    assert reponse["title"] == quiz__["title"]
    assert reponse["description"] == quiz__["description"]\

@patch("api.service.quiz_service.QuizService.get_quiz_by_id")
def test_show_mock_shoud_throw_an_error_when_id_is_invalid(mock_get_quiz_by_id):
    mock_get_quiz_by_id.side_effect = QuizError(ApplicationConstant.quiz_not_found_message)
    test_id = 1
    with pytest.raises(QuizError):
        quiz_service.show_mock(test_id)
