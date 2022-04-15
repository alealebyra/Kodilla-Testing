import pytest
from wtforms import Form

from quizzes.forms import quiz_form_factory
from quizzes.models import QuizQuestion, QuizTaken


@pytest.fixture
def quiz_question():
    quiz_question = QuizQuestion(
        question='Question?', correct_answer='correct', incorrect_answers=['incorrect', 'incorrect']
    )
    return quiz_question


@pytest.fixture
def quiz_taken(quiz_question):
    quiz_taken = QuizTaken(uuid='2137', difficulty='medium', questions=[quiz_question, quiz_question, quiz_question])
    return quiz_taken


def test_quiz_form_factory(quiz_taken):
    quiz_form = quiz_form_factory(quiz_taken)
    assert quiz_form.__name__ == "QuizForm"
    assert quiz_form.__bases__ == (Form,)

