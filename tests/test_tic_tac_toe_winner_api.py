from tic_tac_toe.api import app


def test_api_is_wsgi_app():
    assert hasattr(app, 'wsgi_app')


def test_api_missing_parameter():
    assert app.test_client().get('/winner').status_code == 400


def test_api_response_is_json():
    response = app.test_client().get('/winner?board=_________')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert isinstance(response.json, dict)
    assert 'winner' in response.json


# to nie sa dobre testy jednostkowe

def test_api_3x_in_a_row():
    response = app.test_client().get('/winner?board=XXX_O_O__')
    assert response.status_code == 200 and response.json['winner'] == 'X'


def test_api_unfinished_game():
    response = app.test_client().get('/winner?board=X_____O__')
    assert response.status_code == 200 and response.json['winner'] is None




