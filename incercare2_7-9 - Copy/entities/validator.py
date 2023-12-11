from colorama import Fore, Back, Style, init
init()

class MovieValidator:
    def __init__(self):
        pass

    def validate_movie(self, movie):
        errors = []

        if len(movie.get_id_movie()) != 6:
            errors.append(Fore.CYAN + "Invalid ID. "+ Style.RESET_ALL)

        if movie.get_id_movie() == "":
            errors.append(Fore.CYAN + "Invalid name, cannot have blank name. " + Style.RESET_ALL)

        if movie.get_duration() < 2:
            errors.append(Fore.CYAN + "There are no movies shorter than 2 mins. "+ Style.RESET_ALL)
            
        if movie.get_type() not in ['action', 'horror', 'comedy', 'drama', 'family', 'romance', 'musical', 'war']:
            errors.append(Fore.CYAN + "Invalid movie type. "+ Style.RESET_ALL)

        if len(errors) > 0:
            error_string = '\n'.join(errors)
            raise ValueError(error_string)
        

class ClientValidator:
    def __init__(self):
        pass

    def validate_client(self, client):
        errors = []
        if len(client.get_id_client()) != 4:
            errors.append(Fore.CYAN + "Invalid ID. "+ Style.RESET_ALL)
        
        if len(client.get_name()) == 0:
            errors.append(Fore.CYAN + "Invalid name. "+ Style.RESET_ALL)
        
        if len(client.get_cnp()) != 13:
            errors.append(Fore.CYAN + "Invalid CNP. "+ Style.RESET_ALL)

        if len(errors) > 0:
            error_string = '\n'.join(errors)
            raise ValueError(error_string)
