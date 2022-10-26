# TODO: Feature 2
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository
from app import app
#import pytest
movie_repository = get_movie_repository()

# test that feature works 
def test_movie_created_successfully():
    test_app = app.test_client()
    #this should make the movie
    movie_repository.create_movie('Psycho', 'Ur Mom', 5)
    movie = Movie('Psycho', 'Ur Mom', 5)

    assert type(movie) == Movie
    assert movie.title == 'Psycho'
    assert movie.director == 'Ur Mom'
    assert movie.rating == 5

# test that feature doesn't work
def test_movie_not_created_successfully():
    test_app = app.test_client()

    movie_repository.create_movie('The Godmother', 'Bob Ricky', 3)
    movie = Movie('The Godmother', 'Bob Ricky', 3)
    
    assert not movie.title == 'The Godmothers'
    assert not movie.director == 'Bob Rickyo'
    assert not movie.rating == 4
