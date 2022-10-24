# TODO: Feature 3

from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository
from app import app
import pytest
movie_repository = get_movie_repository()

#test what happens if the move is not in the list
def test_search_movies_No_Movie():
    test_app = app.test_client()
    #this gets the page
    response = test_app.get('/movies/search?title=dad')
    assert b' <h2>Enter in a valid movie</h2>' in response.data

#test what happens if the movie is in the list
def test_search_movies_yes_Movie():
    #this should make the movie
    movie = Movie('YoMama', 'George Lucas', 5)
    test_app = app.test_client()
    movie_repository.create_movie('YoMama', 'George Lucas', 5)
    response = test_app.get('/movies/search?title=YoMama')
    assert b'<h2> YoMama</h2>' in response.data
    assert b'<p> By George Lucas</p>' in response.data
    assert b' <p> With a rating of 5 </p>' in response.data
    

