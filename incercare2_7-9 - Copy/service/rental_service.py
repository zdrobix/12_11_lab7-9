from repository.rental_repository import RentalMemoryRepository
from entities.rental import RentalSystem
import random

class RentalController:
    def __init__(self, repository: RentalMemoryRepository):
        self.__repo = repository

    def rent_movie(self, id_client, id_movie):
        self.__repo.store(id_client, id_movie)

    def get_all_clients_for_movie(self, id_movie):
        return self.__repo.get_clients(id_movie)

    def get_all_movies_for_client(self, id_client):
        return self.__repo.get_movies(id_client)

    def get_movie_number(self, id_client):
        return self.__repo.get_movie_number(id_client)

    def get_client_number(self, id_movie):
        return self.__repo.get_client_number(id_movie)

    def rand_rent(self, clients, movies,nr):
        added = []
        for i in range(nr):
            client = random.choice(clients)
            movie = random.choice(movies)
            rental = RentalSystem(client.get_id_client(), movie.get_id_movie())
            self.__repo.store(client.get_id_client(), movie.get_id_movie())
            added.append(rental)
        return added

    def create_tuple_list(self):
        list = self.__repo.create_tuple()
        list = sorted(list, key = lambda movie: movie[1] if movie[1] is not None else 0, reverse=True)
        return list

    def create_tuple_list_least(self):
        list = self.__repo.create_tuple()
        list = sorted(list, key=lambda movie: movie[1] if movie[1] is not None else 0, reverse=False)
        return list

    def create_tuple_client_alph(self):
        list = self.__repo.create_tuple_clients()
        list = sorted(list, key=lambda client: client[0], reverse=True)
        list = sorted(list, key=lambda client: client[1], reverse=True)
        return list

    def create_tuple_client(self):
        list = self.__repo.create_tuple_clients()
        list = sorted(list, key=lambda client: client[1], reverse=True)
        return list

    def delete_all(self):
        return self.__repo.delete_all()