from uuid import uuid4

from quizzes.models import calculate_points, QuizTaken, QuizQuestion, User

import pytest


@pytest.fixture
def quiz_question():
    quiz_question = QuizQuestion(
        question='Question?', correct_answer='correct', incorrect_answers=['incorrect', 'incorrect']
    )
    return quiz_question


@pytest.fixture
def quiz_taken(quiz_question):
    quiz_taken = QuizTaken(uuid='2137', difficulty='medium', questions=[quiz_question, quiz_question])
    return quiz_taken


def test_calculate_points_dummy():
    quiz_taken = QuizTaken(uuid=uuid4().hex, difficulty='easy', questions=[])
    assert 0 == calculate_points(quiz_taken=quiz_taken, answers={})


def test_calculate_points_raises_value_error(quiz_taken):
    with pytest.raises(ValueError):
        calculate_points(quiz_taken=quiz_taken, answers={})


def test_calculate_points_with_correct_answer(quiz_taken):
    answers = {
        1: 'correct',
        2: 'incorrect',
    }
    assert 2 == calculate_points(quiz_taken=quiz_taken, answers=answers)


def test_new_user():
    user = User(id=1, active=True, username='Name', password='passwd', first_name='Name', last_name='Lastname')
    assert user.id == 1
    assert user.active
    assert user.username == 'Name'
    assert user.password == 'passwd'
    assert user.first_name == 'Name'
    assert user.last_name == 'Lastname'

