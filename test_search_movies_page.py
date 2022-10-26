# TODO: Feature 3
from flask.testing import FlaskClient


def test_home_page(test_app: FlaskClient):
    response = test_app.get('/movies/search')
    response_data = response.data

    assert b'<p class="mb-3">Search for a movie rating below</p>' in response_data