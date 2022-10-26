# TODO: Feature 2
from flask.testing import FlaskClient

def test_create_page(test_app: FlaskClient):
    response = test_app.get('/movies/new')
    response_data = response.data

    assert b'<p class="mb-3">Create a movie rating below</p>' in response_data