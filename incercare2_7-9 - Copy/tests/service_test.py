import sys
sys.path.append('C:\\Alex Zdroba\\python projects\\fp\\incercare2_7-9 - Copy\\entities')

from validator import ClientValidator, MovieValidator
from repository import ClientMemoryRepository, MovieMemoryRepository, RentalMemoryRepository
from service import ClientController, MovieController, RentalController


#CLIENT TESTS:
def test_add_client_service():
    repo = ClientMemoryRepository()
    validator = ClientValidator()
    client_service = ClientController(repo, validator)
    
    client_service.add_client('xxyx', 'Stefanescu', '17803041250765')
    test_client_list = client_service.get_all_client()
    assert(len(test_client_list) == 1)
    
    try:
        client_service.add_client('xxyx', 'ClientDoubleID', '17803234150765')
        assert False
    except ValueError:
        assert True

    try:
        client_service.add_client('11xyx', 'ClientInvalidID', '17803234150765')
        assert False
    except ValueError:
        assert True

    try:
        client_service.add_client('1234', 'ClientInvalidCNP', 'CNP1234')
        assert False
    except ValueError:
        assert True

def test_delete_client_service():
    repo = ClientMemoryRepository()
    validator = ClientValidator()
    client_service = ClientController(repo, validator)
    
    client_service.add_client('alex', 'Zdroba', '5041110125802')
    client_service.add_client('wgk0', 'Ionescu', '1740111827215')
    client_service.add_client('k72o', 'Popovic', '2750719126697')

    client_service.delete_client('alex')
    assert(len(client_service.get_all_client()) == 2)

    client_service.delete_client('wgk0')
    assert(len(client_service.get_all_client()) == 1)

    client_service.delete_client('k72o')
    assert(len(client_service.get_all_client()) == 0)
    
def test_update_client_service():
    repo = ClientMemoryRepository()
    validator = ClientValidator()
    client_service = ClientController(repo, validator)
    
    client_service.add_client('alex', 'Zdroba', '5041110125802')
    client_service.add_client('wgk0', 'Ionescu', '1740111827215')
    client_service.add_client('k72o', 'Popovic', '2750719126697')

    client_service.update_client('alex', 'Taurinius', '5041110125802')
    client_service.update_client('wgk0', 'Floreanuvici', '1740111827215')
    client_service.update_client('k72o', 'Comarnic', '2750719126697')
    #TO BE FINISHED

def test_find_client_service():
    repo = ClientMemoryRepository()
    validator = ClientValidator()
    client_service = ClientController(repo, validator)
    
    client_service.add_client('alex', 'Zdroba', '5041110125802')
    client_service.add_client('wgk0', 'Ionescu', '1740111827215')
    client_service.add_client('k72o', 'Popovic', '2750719126697')

    assert(client_service.find_client('alex') is not None)
    assert(client_service.find_client('wgk0') is not None)
    assert(client_service.find_client('k72o') is not None)

    assert(client_service.find_client('1232') is None)
    assert(client_service.find_client('asdf') is None)
    assert(client_service.find_client('XXX1') is None)

#MOVIE TESTS:

def test_add_movie_service():
    repo = MovieMemoryRepository()
    validator = MovieValidator()
    movie_service = MovieController(repo, validator)
    movie_service.add_movie('xyz123', 'Spiderman', 'action', 123 )
    test_moviet_list = movie_service.get_all_movie()
    assert(len(test_moviet_list) == 1)
    
    try:
        movie_service.add_movie('xyz123', 'DuplicateID', 'action', 123 )
        assert False
    except ValueError:
        assert True

    try:
        movie_service.add_movie('123456', 'InvalidType', 'coolmovie', 123 )
        assert False
    except ValueError:
        assert True

    try:
        movie_service.add_movie('power3', 'NoMovieLenght', 'action', 0 )
        assert False
    except ValueError:
        assert True

def test_delete_movie_service():
    repo = MovieMemoryRepository()
    validator = MovieValidator()
    movie_service = MovieController(repo, validator)

    movie_service.add_movie('abcdef', 'Cocaine Bear', 'horror', '95')
    movie_service.add_movie('1234qp', '2012', 'action', '158')
    movie_service.add_movie('qwerty', 'Censor', 'drama', '84')

    movie_service.delete_movie('abcdef')
    assert(len(movie_service.get_all_movie()) == 2)

    movie_service.delete_movie('1234qp')
    assert(len(movie_service.get_all_movie()) == 1)

    movie_service.delete_movie('qwerty')
    assert(len(movie_service.get_all_movie()) == 0)


def test_find_movie_servic():
    repo = MovieMemoryRepository()
    validator = MovieValidator()
    movie_service = MovieController(repo, validator)
    
    movie_service.add_movie('abcdef', 'Cocaine Bear', 'horror', '95')
    movie_service.add_movie('1234qp', '2012', 'action', '158')
    movie_service.add_movie('qwerty', 'Censor', 'drama', '84')

    assert(movie_service.find_movie('abcdef') is not None)
    assert(movie_service.find_movie('1234qp') is not None)
    assert(movie_service.find_movie('qwerty') is not None)

    assert(movie_service.find_movie('121232') is None)
    assert(movie_service.find_movie('asd23f') is None)
    assert(movie_service.find_movie('X12XX1') is None)

