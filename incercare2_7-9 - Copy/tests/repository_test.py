import sys

from entities.client import Client
from entities.movie import Movie
from repository.client_repository import ClientMemoryRepository
from repository.movie_repository import MovieMemoryRepository
from repository.rental_repository import RentalMemoryRepository

sys.path.append('C:\\Alex Zdroba\\python projects\\fp\\incercare2_7-9 - Copy\\entities')

filename = r'C:\Alex Zdroba\python projects\fp\incercare2_7-9 - Copy\tests\inputForTest.txt'

#CLIENT TESTS:

def delete_file_content():
    try:
        with open(filename, mode='w'):
            pass
    except ValueError as e:
        print("Error deleting contents.")


def test_add_client_repo():
    test_repo = ClientMemoryRepository(filename)

    client1 = Client('0o0o', 'Zdrobix', '5041110125555')
    test_repo.store(client1)

    try:
        test_repo.store(client1)
        assert False
    except ValueError:
        assert True

    client2 = Client('uiui', 'Zaroba', '5041110124455')
    test_repo.store(client2)
    
def test_find_client_repo():
    test_repo = ClientMemoryRepository(filename)
    
    client1 = Client('0o0o', 'Zdrobix', '5041110125555')
    client2 = Client('uiui', 'Zaroba', '1741110124455')
    client3 = Client('123x', 'Gipilan', '2041110127788')

    test_repo.store(client1)
    test_repo.store(client2)
    test_repo.store(client3)

    assert(test_repo.find('0o0o') is not None)
    assert(test_repo.find('uiui') is not None)
    assert(test_repo.find('123x') is not None)

    assert(test_repo.find('aaaa') is None)
    assert(test_repo.find('hhhh') is None)
    assert(test_repo.find('9128') is None)

def test_delete_client_repo():
    test_repo = ClientMemoryRepository(filename)

    client1 = Client('0o0o', 'Zdrobix', '5041110125555')
    client2 = Client('uiui', 'Zaroba', '1741110124455')
    client3 = Client('123x', 'Gipilan', '2041110127788')

    test_repo.store(client1)
    test_repo.store(client2)
    test_repo.store(client3)

    deleted_client = test_repo.delete('0o0o')
    assert(test_repo.find('0o0o') is None)
    assert(deleted_client.get_name() == 'Zdrobix')

    deleted_client = test_repo.delete('uiui')
    assert(test_repo.find('uiui') is None)
    assert(deleted_client.get_name() == 'Zaroba')

    try:
        test_repo.delete('kkkk')
        assert False
    except ValueError:
        assert True

#

#MOVIE TESTS:
def test_add_movie_repo():
    test_repo = MovieMemoryRepository(filename)

    movie1 = Movie('1234xy', 'Movie', 'action', 123)
    test_repo.store(movie1)

    try:
        test_repo.store(movie1)
        assert False
    except ValueError:
        assert True

    movie2 = Movie('uiuiui', 'Zaroba and the Blue lake', 'family', 124)
    test_repo.store(movie2)
    
def test_find_movie_repo():
    test_repo = MovieMemoryRepository(filename)
    
    movie1 = Movie('677677', 'Oklahoma!', 'musical', '150')
    movie2 = Movie('nuprea', 'Cars', 'family', '117')
    movie3 = Movie('salut9', 'The Hobbit', 'action', '144')

    test_repo.store(movie1)
    test_repo.store(movie2)
    test_repo.store(movie3)
    
    assert(test_repo.find('677677') is not None)
    assert(test_repo.find('nuprea') is not None)
    assert(test_repo.find('salut9') is not None)

    assert(test_repo.find('a12aaa') is None)
    assert(test_repo.find('hyuhhh') is None)
    assert(test_repo.find('91qq28') is None)

def test_delete_movie_repo():
    test_repo = MovieMemoryRepository(filename)
    
    movie1 = Movie('677677', 'Oklahoma!', 'musical', '150')
    movie2 = Movie('nuprea', 'Cars', 'family', '117')
    movie3 = Movie('salut9', 'The Hobbit', 'action', '144')

    test_repo.store(movie1)
    test_repo.store(movie2)
    test_repo.store(movie3)

    deleted_movie = test_repo.delete('salut9')
    assert(test_repo.find('salut9') is None)
    assert(deleted_movie.get_title() == 'The Hobbit')

    deleted_movie = test_repo.delete('677677')
    assert(test_repo.find('677677') is None)
    assert(deleted_movie.get_title() == 'Oklahoma!')

    try:
        test_repo.delete('k12kkk')
        assert False
    except ValueError:
        assert True

#

#RENTAL TESTS:
def test_add_rental():
    test_repo = RentalMemoryRepository(filename)
    
    client = Client('0o0o', 'Zdrobix', '5041110125555')
    movie = Movie('nuprea', 'Cars', 'family', '117')

    test_repo.store(client, movie)
    


            





    
