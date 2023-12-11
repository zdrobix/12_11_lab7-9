import sys
sys.path.append('C:\\Alex Zdroba\\python projects\\fp\\incercare2_7-9 - Copy')

from entities.client import Client
from entities.movie import Movie
from entities.rental import RentalSystem
from entities.validator import ClientValidator, MovieValidator

def test_create_client():
    client = Client('1234', 'Zdroba', '5041110125555')
    assert(client.get_id_client() == '1234')
    assert(client.get_name() == 'Zdroba')
    assert(client.get_cnp() == '5041110125555')
    
    client.set_name('Zdrobix')
    client.set_cnp('5041110125666')

    assert(client.get_name() == 'Zdrobix')
    assert(client.get_cnp() == '5041110125666')

def test_equal_client():
    client1 = Client("fff1", "Man", 1890981264789)
    client2 = Client("fff1", "Man", 1890981264789)
    assert client1 == client2

def test_validate_client():
    validator = ClientValidator()
    
    client1 = Client('12345', 'InvalidID', '5041110125555')
    try:
        validator.validate_client(client1)
        assert False
    except ValueError:
        assert True

    client2 = Client('xxxx', 'InvalidCNP', '504cnpDAda')
    try:
        validator.validate_client(client2)
        assert False
    except ValueError:
        assert True

    client3 = Client('123x', '', '5041110125555')
    try:
        validator.validate_client(client3)
        assert False
    except ValueError:
        assert True

    client4 = Client('xzxz', 'ValidClient', '5041110125555')
    try:
        validator.validate_client(client4)
        assert True
    except ValueError:
        assert False

#
        
#MOVIE TESTS:
def test_create_movie():
    movie1 = Movie("12xo99", "The Man", "action", 120)
    movie2 = Movie("aba242", "Spiderman II", "family", 135)
    assert movie1.get_id_movie() == "12xo99"
    assert movie2.get_id_movie() == "aba242"
    assert movie1.get_duration() == 120
    assert movie2.get_duration() == 135
    
def test_equal_movie():
    movie1 = Movie("12xo99", "The Man", "action", 120)
    movie2 = Movie("12xo99", "The Man", "action", 120)
    assert movie1 == movie2

def test_validate_movie():
    validator = MovieValidator()

    movie1 = Movie("123", "InvalidID", "action", 120)
    movie2 = Movie("noname", "", "muzical", 135)
    movie3 = Movie("xxxrrr", "InvalidType", "coolmovie", 135)
    movie4 = Movie("asd123", "InvalidLenght", "action", 0)
    movie5 = Movie("kykyky", "ValidMovie", "family", 135)
    
    try:
        validator.validate_movie(movie1)
        assert False
    except ValueError:
        assert True

    try:
        validator.validate_movie(movie2)
        assert False
    except ValueError:
        assert True

    try:
        validator.validate_movie(movie3)
        assert False
    except ValueError:
        assert True

    try:
        validator.validate_movie(movie4)
        assert False
    except ValueError:
        assert True

    try:
        validator.validate_movie(movie5)
        assert True
    except ValueError:
        assert False
    
test_equal_movie()
test_create_movie()
test_validate_client()
test_create_client()
test_equal_client()
test_validate_movie()
