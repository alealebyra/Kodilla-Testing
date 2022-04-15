from flask import Response

from quizzes.app import create_app, init_database, global_vars_report


def test_api_is_wsgi_app():
    app = create_app()
    assert hasattr(app, 'wsgi_app')


# def test_init_database():
#     app(init_database)


# Czy mockowac Response?
def test_global_vars_report():
    response = Response
    assert response == global_vars_report(response=response)
