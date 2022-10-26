# TODO: Feature 1

from src.repositories.movie_repository import get_movie_repository
from app import app
movie_repository = get_movie_repository()

#test what happens if the movie created does appear in the list
def test_get_all_movies_in_List():
    #test the app
    testing_app = app.test_client()

    #make a movie to test
    movie_repository.create_movie('The Last Jedi', 'Rian Johnson', 3)
    #this will get the response from the app client 
    response = testing_app.get('/movies')
    #check if the movie attributes are in the table 
    assert b'<td>The Last Jedi</td>' in response.data
    assert b'<td>Rian Johnson</td>' in response.data
    assert b'<td>3</td>' in response.data

#test what happens if the list displays content that wasn't entered in the create_movie()
def test_get_all_movies_not_in_List():
    #test the app, do not create a movie here
    testing_app = app.test_client()

    movie_repository.create_movie('The Last Jedi', 'Rian Johnson', 3)
    response = testing_app.get('/movies')
    #check that the title is different 
    assert not b'<td>The Last Sith</td>' in response.data
    assert b'<td>Rian Johnson</td>' in response.data
    assert b'<td>3</td>' in response.data
