import json

import pytest
from flask import template_rendered, session
from flask_login import FlaskLoginClient
from werkzeug.test import Client

from quizzes.app import app
from quizzes.models import User


def check_response_status_code_and_template_name(client, captured_templates, endpoint, template_name):
    response = client.get(endpoint)
    assert response.status_code == 200
    assert len(captured_templates) == 1
    template, _ = captured_templates[0]
    assert template.name == template_name


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


def test_ranking_data(client, ):
    template_name = '/ranking.json'
    response = client.get(template_name)
    assert response.status_code == 200

    data = json.loads(response.get_data(as_text=True))
    assert data[0] == 4
