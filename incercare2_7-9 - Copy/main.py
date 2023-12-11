import sys
sys.path.append('C:\\Alex Zdroba\\python projects\\fp\\incercare2_7-9 - Copy\\entities')

inputClient =  r'C:\Alex Zdroba\python projects\fp\incercare2_7-9 - Copy\inputs\inputClient.txt'
inputRental = r'C:\Alex Zdroba\python projects\fp\incercare2_7-9 - Copy\inputs\inputRental.txt'
inputMovie=  r'C:\Alex Zdroba\python projects\fp\incercare2_7-9 - Copy\inputs\inputMovie.txt'

from service.client_service import ClientController
from service.movie_service import MovieController
from service.rental_service import RentalController

from entities.validator import ClientValidator, MovieValidator

from repository.movie_repository import MovieMemoryRepository
from repository.client_repository import ClientMemoryRepository
from repository.rental_repository import RentalMemoryRepository

from ui.console import Console


client_repository = ClientMemoryRepository(inputClient)
movie_repository = MovieMemoryRepository(inputMovie)
rental_repository = RentalMemoryRepository(inputRental)

client_validator = ClientValidator()
movie_validator = MovieValidator()

client_controller = ClientController(client_repository, client_validator)
movie_controller = MovieController(movie_repository, movie_validator)
rental_controller = RentalController(rental_repository)

console = Console(client_controller, movie_controller, rental_controller)

console.run()
