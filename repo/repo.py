from domain.movie import Movie
from domain.client import Client
from domain.rental import Rental
from domain.rental import Date
from datetime import date
from business.exception import CustomError
import random
from business.stackobject import StackObject
    
class Repository():
    def __init__(self):
        self._movies = self._initMovies()
        self._clients = self._initClients()
        self._rentals = self._initRentals()

        self._commands = self._initCommands()

        self._stack = []
        self._helpStack = []
        self._redoStack = []
        
        today = date.today()
        s = str(today)
        self._globalDate = self._getTheDate(s)

################################################################################################

    def _initMovies(self):
        movieNames = ["Mowgly", "Endgame", "Joker", "Facebook", "Last man standing", "Hunger games", "7 pinguins", "Last Christmas", "Fifty shades of Grey", "Tall Grass"]
        movieDescs = ["A boy in the jungle pretty much", "Thanos is not even relevant anymore", "Finally a good movie came out this year", "That one movie about Mark Zuckerberg",
                        "Fortnite battle royale simulator", "Similar to fortnite battle royale but with better graphics", "The title is pretty much explanatory", 
                        "Some generic Christmas movie", "Do I need to explain this one?", "This one was so weeeeeiirdddd"]
        movieGenres = ["Adventure", "Action", "Thriller", "Inspirational", "Game", "Comedy", "Romance", "Horror"]
        ids = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        takeOut = 0
        List = []
        for i in range(1, 11):
            r =  random.randint(0, 9-takeOut)
            r1 = random.randint(0, 9-takeOut)
            r2 = random.randint(0, 9-takeOut)
            r3 = random.randint(0, 7)
            List.append(Movie(ids[r], movieNames[r1], movieDescs[r2], movieGenres[r3]))
            ids.remove(ids[r])
            movieNames.remove(movieNames[r1])
            movieDescs.remove(movieDescs[r2])
            takeOut = takeOut+1
        return List

    def _initClients(self):
        lastNames = ["Ana", "Barbos", "Carmen", "David", "Enache", "Filip", "Gheorghe", "Hangiu", "Ionescu", "Jasmine"]
        firstNames = ["Maria", "Grigore", "Antonia", "Catalin", "Flavius", "Andrei", "Vasile", "Robert", "Cosmin", "Poppy"]
        ids = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        takeOut = 0
        List = []
        for i in range (1, 11):
            r  = random.randint(0, 9-takeOut)
            r1 = random.randint(0, 9-takeOut)
            r2 = random.randint(0, 9-takeOut)
            List.append(Client(ids[r], lastNames[r1] + " " + firstNames[r2]))
            ids.remove(ids[r])
            lastNames.remove(lastNames[r1])
            firstNames.remove(firstNames[r2])
            takeOut = takeOut+1
        return List

    def _initRentals(self):
        List = []
        List.append(Rental("1", "1", "1", Date(19, 10, 2019), Date(21, 11, 2019)))
        List.append(Rental("2", "2", "3", Date(17, 11, 2019), Date(18, 11, 2019)))
        List.append(Rental("3", "3", "5", Date(15, 6, 2015), Date(12, 12, 2020)))
        List.append(Rental("4", "4", "7", Date(2, 6, 2000), Date(2, 6, 2020)))
        List.append(Rental("5", "5", "9", Date(6, 11, 2019), Date(6, 12, 2019)))
        return List

    def _initCommands(self):
        commands = {
            "self._addMovie" : self._addMovie,
            "self._removeMovie" : self._removeMovie,
            "self._addClient" : self._addClient,
            "self._removeClient" : self._removeClient,
            "self._updateMovie" : self._updateMovie,
            "self._updateClient" : self._updateClient,
            "self._addRental" : self._addRental,
            "self._deleteRental" : self._deleteRental,
            "self._undoReturn" : self._undoReturn,
            "self._removeRental" : self._removeRental
        }
        return commands

################################################################################################
    
    def _getTheDate(self, s):
        idx = s.find("-")
        year = s[:idx]
        s = s[idx+1:]
        idx = s.find("-")
        month = s[:idx]
        day = s[idx+1:]
        return Date(day, month, year)

################################################################################################

    def _addMovie(self, newId, newTitle, newDesc, newGenre, U=""):
        '''
        Function adds a movie to the list
        '''
        self._movies.append(Movie(newId, newTitle, newDesc, newGenre))
        if U != "U":
            self._stack.append(StackObject("self._removeMovie", [newId]))
            self._helpStack.append(StackObject("self._addMovie", [newId, newTitle, newDesc, newGenre]))
            self._redoStack.clear()

    def _addClient(self, newId, newName, U=""):
        '''
        Function adds a client to the list
        '''
        self._clients.append(Client(newId, newName))
        if U != "U":
            self._stack.append(StackObject("self._removeClient", [newId]))
            self._helpStack.append(StackObject("self._addClient", [newId, newName]))
            self._redoStack.clear()

    def _addRental(self, rentalId, movieId, clientId, dueDate, U=""):
        if self._userOk(clientId) and self._movieOk(movieId):
            self._rentals.append(Rental(rentalId, movieId, clientId, self._globalDate, dueDate))
            if U != "U":
                self._stack.append(StackObject("self._removeRental", [rentalId]))
                self._helpStack.append(StackObject("self._addRental", [rentalId, movieId, clientId, dueDate]))
                self._redoStack.clear()

################################################################################################

    def _removeMovie(self, newId, U=""):
        '''
        Function removes a movie from the list
        '''
        i = 0
        while i < len(self._movies):
            if self._movies[i].Id == newId:
                if U != "U":
                    self._stack.append(StackObject("self._addMovie", [self._movies[i].Id, self._movies[i].Title, self._movies[i].Description, self._movies[i].Genre]))
                    self._helpStack.append(StackObject("self._removeMovie", [newId]))
                    self._redoStack.clear()
                self._movies.remove(self._movies[i])
                i = i-1
            i = i+1

    def _removeClient(self, newId, U=""):
        '''
        Function removes a client from the list
        '''

        i = 0
        while i < len(self._clients):
            if self._clients[i].Id == newId:
                if U != "U":
                    self._stack.append(StackObject("self._addClient", [self._clients[i].Id, self._clients[i].Name]))
                    self._helpStack.append(StackObject("self._removeClient", [newId]))
                    self._redoStack.clear()
                self._clients.remove(self._clients[i])
                i = i-1
            i = i+1

    def _removeRental(self, rentalId, U=""):
        for rental in self._rentals:
            if rental.RentalId == rentalId:
                self._rentals.remove(rental)

################################################################################################

    def _updateMovie(self, newId, newTitle, newDesc, newGenre, U=""):
        '''
        Function updates a movie in the list
        '''
        for movie in self._movies:
            if movie.Id == newId:
                if U != "U":
                    self._stack.append(StackObject("self._updateMovie", [movie.Id, movie.Title, movie.Description, movie.Genre]))
                    self._helpStack.append(StackObject("self._updateMovie", [newId, newTitle, newDesc, newGenre]))
                    self._redoStack.clear()
                movie.Title = newTitle
                movie.Description = newDesc
                movie.Genre = newGenre

    def _updateClient(self, newId, newName, U=""):
        '''
        Function updates a client in the list
        '''
        for client in self._clients:
            if client.Id == newId:
                if U != "U":
                    self._stack.append(StackObject("self._updateClient", [client.Id, client.Name]))
                    self._helpStack.append(StackObject("self._updateClient", [newId, newName]))
                    self._redoStack.clear()
                client.Name = newName

    def _deleteRental(self, movieId, U=""):
        for rental in self._rentals:
            if rental.MovieId == movieId:
                if U != "U":
                    self._stack.append(StackObject("self._undoReturn", [movieId]))
                    self._helpStack.append(StackObject("self._deleteRental", [movieId]))
                    self._redoStack.clear()
                rental.ReturnedDate = self._globalDate
                break

    def _undoReturn(self, movieId, U=""):
        for rental in self._rentals:
            if rental.MovieId == movieId:
                rental.ReturnedDate = Date(0,0,0)
                break

################################################################################################

    def _movieExists(self, movieId):
        isId = False
        for movie in self._movies:
            if movie.Id == movieId:
                isId = True
        return isId

    def _clientExists(self, clientId):
        isId = False
        for client in self._clients:
            if client.Id == clientId:
                isId = True
        return isId

    def _movieOk(self, movieId):
        isId = False
        for movie in self._movies:
            if movie.Id == movieId:
                isId = True
        if isId == False: raise CustomError("There is no movie with such id")
        for rental in self._rentals:
            if rental.MovieId == movieId:
                raise CustomError("This movie is already rented")
        return True

    def _userOk(self, clientId):
        isId = False
        for client in self._clients:
            if client.Id == clientId:
                isId = True
        if isId == False: raise CustomError("There is no client with such id")
        for rental in self._rentals:
            if rental.ClientId == clientId and rental.DueDate < self._globalDate:
                raise CustomError("This user already has a movie past its due date")
        return True

################################################################################################

    def _undo(self):
        if len(self._stack) == 0:
            raise CustomError("Ain't got nothin' to undo")
        toUndo = self._stack[-1]
        self._redoStack.append(self._helpStack[-1])

        if len(toUndo.Params) == 1:
            self._commands[toUndo.Name](toUndo.Params[0], "U")
        elif len(toUndo.Params) == 2:
            self._commands[toUndo.Name](toUndo.Params[0], toUndo.Params[1], "U")
        elif len(toUndo.Params) == 3:
            self._commands[toUndo.Name](toUndo.Params[0], toUndo.Params[1], toUndo.Params[2], "U")
        elif len(toUndo.Params) == 4:
            self._commands[toUndo.Name](toUndo.Params[0], toUndo.Params[1], toUndo.Params[2], toUndo.Params[3], "U")
        elif len(toUndo.Params) == 5:
            self._commands[toUndo.Name](toUndo.Params[0], toUndo.Params[1], toUndo.Params[2], toUndo.Params[3], toUndo.Params[4], "U")
        elif len(toUndo.Params) == 6:
            self._commands[toUndo.Name](toUndo.Params[0], toUndo.Params[1], toUndo.Params[2], toUndo.Params[3], toUndo.Params[4], toUndo.Params[5], "U")
        del self._stack[-1]
        del self._helpStack[-1]

    def _redo(self):
        if len(self._redoStack) == 0:
            raise CustomError("Ain't got nothing' to redo")
        toRedo = self._redoStack[-1]

        if len(toRedo.Params) == 1:
            self._commands[toRedo.Name](toRedo.Params[0], "U")
        elif len(toRedo.Params) == 2:
            self._commands[toRedo.Name](toRedo.Params[0], toRedo.Params[1]), "U"
        elif len(toRedo.Params) == 3:
            self._commands[toRedo.Name](toRedo.Params[0], toRedo.Params[1], toRedo.Params[2], "U")
        elif len(toRedo.Params) == 4:
            self._commands[toRedo.Name](toRedo.Params[0], toRedo.Params[1], toRedo.Params[2], toRedo.Params[3], "U")
        elif len(toRedo.Params) == 5:
            self._commands[toRedo.Name](toRedo.Params[0], toRedo.Params[1], toRedo.Params[2], toRedo.Params[3], toRedo.Params[4], "U")
        elif len(toRedo.Params) == 6:
            self._commands[toRedo.Name](toRedo.Params[0], toRedo.Params[1], toRedo.Params[2], toRedo.Params[3], toRedo.Params[4], toRedo.Params[5], "U")
        if len(self._redoStack) != 0:
            del self._redoStack[-1]       

################################################################################################

    @property
    def Movies(self):
        return self._movies
    
    @property
    def Clients(self):
        return self._clients

    @property
    def Rentals(self):
        return self._rentals