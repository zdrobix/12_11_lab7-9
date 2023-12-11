from entities.client import Client
from repository.client_repository import ClientMemoryRepository
from entities.validator import ClientValidator
import random

class ClientController:
    def __init__(self, repository: ClientMemoryRepository, client_validator: ClientValidator):
        self.__client_validator = client_validator
        self.__repo = repository

    def add_client(self, id: str, name: str, cnp: str):
        client = Client(id, name, cnp)
        self.__client_validator.validate_client(client)
        self.__repo.store(client)

    def delete_client(self, id: str):
        return self.__repo.delete(id)

    def update_client(self, id: str, new_name: str, new_cnp: str):
        self.__client_validator.validate_client(Client(id, new_name, new_cnp))
        return self.__repo.update(id, new_name, new_cnp)

    def find_client(self, id: str):
        return self.__repo.find(id)

    def get_all_client(self):
        return self.__repo.get_all()

    def rand_client(self, nr):
        added = []
        for i in range(nr):
            add = random.randint(5, 8)
            id = ""
            for j in range (0, 4):
                if j % 2 == 0:
                    id += random.choice(
                    ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y',
                     'z'])
                else:
                    id += random.choice(['1', '2', '3', '0', '7', '8', '9', '5'])
                if j == 4 and self.__repo.find(id) is not None:
                    id = ""
                    j = 0

            name = ""
            for j in range(add):
                if j == 0:
                    name += random.choice(
                    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'P', 'R', 'Z', 'S'])
                elif j % 2 == 0 and j != 0:
                    name += random.choice(['a', 'e', 'i', 'o', 'u'])
                else:
                    name += random.choice(
                    ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y',
                     'z'])

            cnp = str(random.randint(1111111111111, 9999999999999))

            client = Client(id, name, cnp)
            added.append(client)
            self.__client_validator.validate_client(client)
            self.__repo.store(client)
        return added


    def delete_all(self):
        return self.__repo.delete_all()