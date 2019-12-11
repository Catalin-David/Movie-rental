from repo.repo import Repository
from domain.rental import *
from domain.client import Client
from domain.movie import Movie
class TextRepo(Repository):
    def __init__(self):
        super().__init__()
        self._loadClients()
        self._loadMovies()
        self._loadRentals()

################################################################################################

    def _loadClients(self):
        f = open("clients.txt", "r")
        self._clients = []
        tokens = f.readline().strip().split(',')
        while len(tokens) == 2:
            self._clients.append(Client(tokens[0].strip(), tokens[1].strip()))
            tokens = f.readline().strip().split(',')
        f.close()

    def _loadMovies(self):
        f = open("movies.txt", "r")
        self._movies = []
        tokens = f.readline().split(',')
        while len(tokens) == 4:
            self._movies.append(Movie(tokens[0].strip(), tokens[1].strip(), tokens[2].strip(), tokens[3].strip()))
            tokens = f.readline().split(',')
        f.close()

    def _loadRentals(self):
        f = open("rentals.txt", 'r')
        self._rentals = []
        tokens = f.readline().strip().split(',')
        while len(tokens) == 12:
            self._rentals.append(Rental(tokens[0].strip(), tokens[1].strip(), tokens[2].strip(), Date(tokens[3].strip(), tokens[4].strip(), tokens[5].strip()), Date(tokens[6].strip(), tokens[7].strip(), tokens[8].strip()), Date(tokens[9].strip(), tokens[10].strip(), tokens[11].strip())))
            tokens = f.readline().strip().split(',')
        f.close()

################################################################################################

    def _saveRentals(self):
        f = open("rentals.txt", "w")
        for rental in self._rentals:
            line = str(rental.RentalId) + "," + str(rental.MovieId) + "," + str(rental.ClientId) + "," + str(rental.RentedDate.Day) + "," + str(rental.RentedDate.Month) + "," + str(rental.RentedDate.Year) + "," + str(rental.DueDate.Day) + "," + str(rental.DueDate.Month) + "," + str(rental.DueDate.Year) + "," + str(rental.ReturnedDate.Day) + "," + str(rental.ReturnedDate.Month) + "," + str(rental.ReturnedDate.Year) +'\n'
            f.write(line)
        f.close()

    def _saveClients(self):
        f = open("clients.txt", "w")
        for client in self._clients:
            line = str(client.Id) + "," + str(client.Name) + '\n'
            f.write(line)
        f.close()

    def _saveMovies(self):
        f = open("movies.txt", "w")
        for movie in self._movies:
            line = str(movie.Id) + "," + str(movie.Title) + "," + str(movie.Description) + "," + str(movie.Genre) + '\n'
            f.write(line)
        f.close()

################################################################################################

    def _addClient(self, newId, newName, U=""):
        self._loadClients()
        super()._addClient(newId, newName, U)
        self._saveClients()

    def _removeClient(self, newId, U=""):
        self._loadClients()
        super()._removeClient(newId, U)
        self._saveClients()

    def _updateClient(self, newId, newName, U=""):
        self._loadClients()
        super()._updateClient(newId, newName, U)
        self._saveClients()

################################################################################################

    def _addMovie(self, newId, newTitle, newDesc, newGenre, U=""):
        self._loadMovies()
        super()._addMovie(newId, newTitle, newDesc, newGenre, U)
        self._saveMovies()

    def _removeMovie(self, newId, U=""):
        self._loadMovies()
        super()._removeMovie(newId, U)
        self._saveMovies()

    def _updateMovie(self, newId, newTitle, newDesc, newGenre, U=""):
        self._loadMovies()
        super()._updateMovie(newId, newTitle, newDesc, newGenre, U)
        self._saveMovies()

################################################################################################

    def _addRental(self, rentalId, movieId, clientId, dueDate, U=""):
        self._loadRentals()
        super()._addRental(rentalId, movieId, clientId, dueDate, U)
        self._saveRentals()

    def _removeRental(self, rentalId, U=""):
        self._loadRentals()
        super()._removeRental(rentalId, U)
        self._saveRentals()
    
    def _deleteRental(self, movieId, U=""):
        self._loadRentals()
        super()._deleteRental(movieId, U)
        self._saveRentals()

    def _undoReturn(self, movieId, U=""):
        self._loadRentals()
        super()._undoReturn(movieId, U)
        self._saveRentals()

################################################################################################