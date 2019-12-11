from business.testing import PerformTests
from repo.repo import Repository
from repo_binary.binaryrepo import BinaryRepo
from repo_text.textrepo import TextRepo
from domain.rental import Date
from business.exception import CustomError

class Service:
    def __init__(self):
        PerformTests()
        f = open("settings.properties", "r")
        prop = f.readline()
        prop.strip()
        if prop[9] == "1":
            self._repository = Repository()
        elif prop[9] == "2":
            self._repository = TextRepo()
        elif prop[9] == "3":
            self._repository = BinaryRepo()

################################################################################################

    def _addMovie(self, newId, newTitle, newDesc, newGenre):
        '''
        Function adds a movie to the list
        '''
        self._repository._addMovie(newId, newTitle, newDesc, newGenre)

    def _addClient(self, newId, newName):
        '''
        Function adds a client to the list
        '''
        self._repository._addClient(newId, newName)

    def _removeMovie(self, newId):
        '''
        Function removes a movie from the list
        '''
        self._repository._removeMovie(newId)
    
    def _removeClient(self, newId):
        '''
        Function removes a client from the list
        '''
        self._repository._removeClient(newId)

    def _updateMovie(self, newId, newTitle, newDesc, newGenre):
        '''
        Function updates a movie in the list
        '''
        self._repository._updateMovie(newId, newTitle, newDesc, newGenre)
    
    def _updateClient(self, newId, newName):
        '''
        Function updates a client in the list
        '''
        self._repository._updateClient(newId, newName)

    def _getMovies(self):
        '''
        Function returns the list of movies
        '''
        return self._repository.Movies

    def _getClients(self):
        '''
        Function returns the list of clients
        '''
        return self._repository.Clients

    def _rentMovie(self, rentalId, movieId, clientId, dueDate):
        self._repository._addRental(rentalId, movieId, clientId, dueDate)

    def _returnMovie(self, movieId):
        self._repository._deleteRental(movieId)

    def _undo(self):
        self._repository._undo()

    def _redo(self):
        self._repository._redo()        

################################################################################################

    def _movieOk(self, movieId):
        isId = False
        for movie in self._repository.Movies:
            if movie.Id == movieId:
                isId = True
        if isId == False: raise CustomError("There is no movie with such id")
        for rental in self._repository.Rentals:
            if rental.MovieId == movieId:
                raise CustomError("This movie is already rented")
        return True

    def _userOk(self, clientId):
        isId = False
        for client in self._repository.Clients:
            if client.Id == clientId:
                isId = True
        if isId == False: raise CustomError("There is no client with such id")
        for rental in self._repository.Rentals:
            if rental.ClientId == clientId and rental.DueDate < self._repository._globalDate:
                raise CustomError("This user already has a movie past its due date")
        return True

    def _movieExists(self, movieId):
        isId = False
        for movie in self._repository.Movies:
            if movie.Id == movieId:
                isId = True
        return isId

    def _clientExists(self, clientId):
        isId = False
        for client in self._repository.Clients:
            if client.Id == clientId:
                isId = True
        return isId

    def _getRentals(self):
        newList = []
        for rental in self._repository.Rentals:
            if self._clientExists(rental.ClientId) and self._movieExists(rental.MovieId):
                newList.append(rental)
        return newList

    def _searchMovies(self, key):
        newList = []
        for movie in self._repository.Movies:
            newMovie = movie._copy()
            newMovie.Id = newMovie.Id.casefold()
            newMovie.Description = newMovie.Description.casefold()
            newMovie.Title = newMovie.Title.casefold()
            newMovie.Genre = newMovie.Genre.casefold()
            if key in newMovie.Id or key in newMovie.Description or key in newMovie.Title or key in newMovie.Genre:
                newList.append(movie._copy())
        return newList

    def _searchClients(self, key):
        newList = []
        for client in self._repository.Clients:
            newClient = client._copy()
            newClient.Id = newClient.Id.casefold()
            newClient.Name = newClient.Name.casefold()
            if key in newClient.Name or key in newClient.Id:
                newList.append(client._copy())
        return newList

    def _searchAll(self, key):
        newList = []
        newList.extend(self._searchMovies(key))
        newList.extend(self._searchClients(key))
        return newList

################################################################################################

    def _findMovieById(self, key):
        for movie in self._repository.Movies:
            if movie._id == key:
                return movie._title

    def _findClientById(self, key):
        for client in self._repository.Clients:
            if client._id == key:
                return client._name

    def _movieStats(self):
        idList = []
        cxList = []
        for movie in self._repository.Movies:
            idList.append(movie._id)
            cxList.append(0)
        for rental in self._repository.Rentals:
            idx = 0
            while idx < len(idList):
                if idList[idx] == rental._movieId:
                    countedDays = 0
                    if rental._returnedDate == Date(0,0,0):
                        countedDays = self._repository._globalDate - rental._rentedDate
                    else:
                        countedDays = rental._returnedDate - rental._rentedDate
                    cxList[idx] = cxList[idx] + countedDays
                    break
                idx += 1
        for i in range(0, len(idList)):
            for j in range(i, len(idList)):
                if cxList[i] < cxList[j]:
                    idList[i], idList[j] = idList[j], idList[i]
                    cxList[i], cxList[j] = cxList[j], cxList[i]
        myList = []
        for i in range(0, len(idList)):
            if self._movieExists(idList[i]):
                myList.append("Movie " + self._findMovieById(idList[i]) + " has been rented for " + str(cxList[i]) + " days.")
        return myList

    def _clientStats(self):
        idList = []
        cxList = []
        for client in self._repository.Clients:
            idList.append(client._id)
            cxList.append(0)
        for rental in self._repository.Rentals:
            idx = 0
            while idx < len(idList):
                if idList[idx] == rental._clientId:
                    countedDays = 0
                    if rental._returnedDate == Date(0,0,0):
                        countedDays = self._repository._globalDate - rental._rentedDate
                    else:
                        countedDays = rental._returnedDate - rental._rentedDate
                    cxList[idx] = cxList[idx] + countedDays
                    break
                idx += 1
        for i in range(0, len(idList)):
            for j in range(i, len(idList)):
                if cxList[i] < cxList[j]:
                    idList[i], idList[j]= idList[j], idList[i]
                    cxList[i], cxList[j] = cxList[j], cxList[i]
        myList = []
        for i in range(0, len(idList)):
            if self._clientExists(idList[i]):
                myList.append("Client " + self._findClientById(idList[i]) + " has rented for " + str(cxList[i]) + " days.")
        return myList

    def _rentalStats(self):
        movList = []
        clList = []
        cxList = []
        for rental in self._repository.Rentals:
            if rental._returnedDate == Date(0,0,0) and (self._repository._globalDate - rental._dueDate)>0:
                movList.append(rental._movieId)
                clList.append(rental._clientId)
                cxList.append(self._repository._globalDate-rental._dueDate)
        for i in range(0, len(cxList)):
            for j in range(i, len(cxList)):
                if cxList[i] < cxList[j]:
                    movList[i], movList[j] = movList[j], movList[i]
                    clList[i], clList[j] = clList[j], clList[i]
                    cxList[i], cxList[j] = cxList[j], cxList[i]
        myList = []
        for i in range(0, len(cxList)):
            if self._clientExists(clList[i]) and self._movieExists(movList[i]):
                myList.append("Movie " + self._findMovieById(movList[i]) + ", rented by " + self._findClientById(clList[i]) + ", has been late for " + str(cxList[i]) + " days.")
        return myList

################################################################################################