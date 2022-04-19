from flask import Response

from quizzes.app import app, global_vars_report


def test_api_is_wsgi_app():
    assert hasattr(app, 'wsgi_app')


def test_global_vars_report():
    response = Response
    assert response == global_vars_report(response=response)
