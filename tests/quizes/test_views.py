import json

import pook as pook
import pytest
from flask import template_rendered, session
from flask_login import FlaskLoginClient
from werkzeug.test import Client

from quizzes.app import app
from quizzes.models import User, quiz_results, QuizResult, QuizTaken, quizzes_taken, QuizQuestion


def check_response_status_code_and_template_name(client, captured_templates, endpoint, template_name):
    response = client.get(endpoint)
    assert response.status_code == 200
    assert len(captured_templates) == 1
    template, _ = captured_templates[0]
    assert template.name == template_name


@pytest.fixture
def quiz_questions_list():
    return [
        {"question": "Who starred in the film 1973 movie &quot;Enter The Dragon&quot;?",
         "correct_answer": "Bruce Lee",
         "incorrect_answers": ["Jackie Chan", "Jet Li", " Yun-Fat Chow"]},
        {"question": "What does GHz stand for?", "correct_answer": "Gigahertz",
         "incorrect_answers": ["Gigahotz", "Gigahetz", "Gigahatz"]},
        {"question": "Which Russian oblast forms a border with Poland?",
         "correct_answer": "Kaliningrad",
         "incorrect_answers": ["Samara", "Nizhny Novgorod", "Omsk"]},
        {"question": "Which Twitch streamer is the vocalist for Red Vox?",
         "correct_answer": "Vinesauce",
         "incorrect_answers": ["The8BitDrummer", "LIRIK", "Sodapoppin"]},
        {"question": "Solid Snake is actually a clone from the DNA of Big Boss in the Metal Gear Solid "
                    "series&#039; history.",
         "correct_answer": "True", "incorrect_answers": ["False"]},
        {"question": "Deus Ex (2000) does not feature the World Trade Center because it was destroyed by "
                     "terrorist attacks according to the game&#039;s plot.",
         "correct_answer": "True", "incorrect_answers": ["False"]},
        {"question": "Which of the following is not a Flintstones character?",
         "correct_answer": "Lord Rockingham IX",
         "incorrect_answers": ["Rockhead Slate", "The Great Gazoo", "Barney Rubble"]},
        {"question": "In Star Trek: The Next Generation, what is the name of Data&#039;s cat?",
         "correct_answer": "Spot", "incorrect_answers": ["Mittens", "Tom", "Kitty"]},
        {"question": "Which restaurant&#039;s mascot is a clown?",
         "correct_answer": "McDonald&#039;s",
         "incorrect_answers": ["Whataburger", "Burger King", "Sonic"]},
        {"question": "Who is the creator of Touhou project?",
         "correct_answer": "Zun",
         "incorrect_answers": ["Jun", "Twilight Frontier", "Tasofro"]},
    ]


@pytest.fixture
def client():
    return Client(app)


@pytest.fixture
def user():
    with app.app_context():
        user = User.query.get(1)
    return user


@pytest.fixture
def captured_templates():
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)


@pytest.fixture
def fake_quiz_taken():
    quiz_taken = QuizTaken(
        uuid="fake-quiz-taken",
        difficulty="easy",
        questions=[
            QuizQuestion(
                question="Hello world?",
                correct_answer="Foo",
                incorrect_answers=["Bar", "Baz", "Qux"],
            )
        ],
    )
    return quiz_taken


@pytest.mark.parametrize('endpoint', ['/not-existing', '/sign-out'])
def test_page_not_found(client, endpoint):
    assert client.get(endpoint).status_code == 404


def test_sign_out_required_login(client):
    response = client.get('/quiz')
    assert response.status_code == 302


@pytest.mark.parametrize(('endpoint', 'template_name'), [('/', 'index.html'), ('/ranking', 'ranking.html')])
def test_views_with_no_login_required(client, captured_templates, endpoint, template_name):
    check_response_status_code_and_template_name(client, captured_templates, endpoint, template_name)


@pytest.mark.parametrize(('endpoint', 'template_name'), [('/quiz', 'choose_quiz_difficulty.html')])
def test_sign_in(user, captured_templates, endpoint, template_name):
    app.test_client_class = FlaskLoginClient

    with app.test_client(user=user) as client:
        check_response_status_code_and_template_name(client, captured_templates, endpoint, template_name)


def test_ranking_data_sorted_by_points(client):
    template_name = '/ranking.json'
    quiz_results['ranking'] = [
        QuizResult(4, '4dc898c4f5c446be98104a70e03fb44c', 2),
        QuizResult(2, '231898c4f5c446be98104a70e03fb44c', 5),
        QuizResult(3, '1dc898c4f5c446be98104a70e03fb44c', 4),
        QuizResult(1, '1ac898c4f5c446be98104a70e03fb44c', 4),
    ]
    response = client.get(template_name)
    assert response.status_code == 200

    data = json.loads(response.get_data(as_text=True))
    assert 'ranking' in data
    assert data['ranking'][0] == {'points': 5, 'quiz_uuid': '231898c4f5c446be98104a70e03fb44c', 'user_id': 2}
    assert data['ranking'][1] == {'points': 4, 'quiz_uuid': '1dc898c4f5c446be98104a70e03fb44c', 'user_id': 3}


@pytest.mark.parametrize('difficulty', ['easy', 'medium', 'hard'])
def test_prepare_quiz(difficulty, user, quiz_questions_list):
    app.test_client_class = FlaskLoginClient
    with app.test_client(user=user) as client:
        response = client.get(f'/quiz/prepare/{difficulty}')
        pook.get(
            f'https://opentdb.com/api.php?amount=10&difficulty={difficulty}',
            reply=302,
            response_json={'uuid': 'fake-uuid', 'difficulty': f'{difficulty}', 'questions': quiz_questions_list}
        )
        assert response.status_code == 302


def test_prepare_quiz_incorrect_difficulty(user):
    app.test_client_class = FlaskLoginClient
    with app.test_client(user=user) as client:
        response = client.get(f'/quiz/prepare/very-hard')
        pook.get(
            f'https://opentdb.com/api.php?amount=10&difficulty=very-hard',
            reply=302,
            response_json={'uuid': 'fake-uuid', 'difficulty': 'very-hard', 'questions': []}
        )
        assert response.status_code == 302


def test_take_quiz_raises_kay_error(user):
    app.test_client_class = FlaskLoginClient
    with app.test_client(user=user) as client:
        response = client.get(f'/quiz/take/fake-quiz-taken')
        assert response.location == '/quiz'


def test_take_quiz(user, captured_templates, fake_quiz_taken):
    quizzes_taken["fake-quiz-taken"] = fake_quiz_taken
    app.test_client_class = FlaskLoginClient
    with app.test_client(user=user) as client:
        response = client.get(f'/quiz/take/fake-quiz-taken')
        assert response.status_code == 200
        assert len(captured_templates) == 1
        template, context = captured_templates[0]
        assert template.name == 'take_quiz.html'
        assert 'form' in context


def test_take_quiz_post_method_with_form_validate(user, fake_quiz_taken):
    quizzes_taken["fake-quiz-taken"] = fake_quiz_taken
    app.test_client_class = FlaskLoginClient
    with app.test_client(user=user) as client:
        response = client.post(f'/quiz/take/fake-quiz-taken', data={'question_1': 'Foo'})
        assert response.status_code == 302
        assert quiz_results[user.id] == [QuizResult(user_id=1, quiz_uuid='fake-quiz-taken', points=1)]


def test_take_quiz_post_method(user, captured_templates, fake_quiz_taken):
    quizzes_taken["fake-quiz-taken"] = fake_quiz_taken
    app.test_client_class = FlaskLoginClient
    with app.test_client(user=user) as client:
        response = client.post(f'/quiz/take/fake-quiz-taken')
        assert response.status_code == 200
        assert len(captured_templates) == 1
        template, context = captured_templates[0]
        assert template.name == 'take_quiz.html'
        assert 'form' in context
