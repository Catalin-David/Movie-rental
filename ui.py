from os import *
from business.exception import CustomError
from domain.rental import Date
from business.service import Service

class UI:
    def __init__(self):
        self._service = Service()

    def _printMenu(self):
        print("Welcome to the best movie rental app")
        print("What would you like to do?")
        print("     0 -> Exit the program")
        print("     1 -> Add a new movie/client")
        print("     2 -> Remove a movie/client")
        print("     3 -> Update a movie/client")
        print("     4 -> List movies/clients")
        print("     5 -> Rent a movie")
        print("     6 -> Return a movie")
        print("     7 -> Search")
        print("     8 -> Stats")
        print("     9 -> Undo")
        print("     10 -> Redo")

    def _addItem(self):
        '''
        Function adds a new item to the current list
        '''
        which = input(">Would you like to add a movie or a client?\n>For movie type: m\n>For client type: c\n>")
        if which == "m":
            newId = input(">Give id of new movie: ")
            newTitle = input(">Give title of new movie: ")
            newDesc = input(">Give description of new movie: ")
            newGenre = input(">Give genre of new movie: ")
            self._service._addMovie(newId, newTitle, newDesc, newGenre)
        elif which == "c":
            newId = input(">Give id of new client: ")
            newName = input(">Give name of new client: ")
            self._service._addClient(newId, newName)
        else:
            raise CustomError("Please type either m or c")

    def _removeItem(self):
        '''
        Function removes an item from the current list
        '''
        which = input(">Would you like to add a movie or a client?\n>For movie type: m\n>For client type: c\n>")
        if which == "m":
            newId = input(">Give id of the movie you'd like to remove: ")
            self._service._removeMovie(newId)
        elif which == "c":
            newId = input(">Give id of the client you'd like to remove: ")
            self._service._removeClient(newId)
        else:
            raise CustomError("Please type either m or c")
    
    def _updateItem(self):
        '''
        Function updates an item in the current list
        '''
        which = input(">Would you like to add a movie or a client?\n>For movie type: m\n>For client type: c\n>")
        if which == "m":
            newId = input(">Give id of the movie you'd like to update: ")
            newTitle = input(">Give the new title of the movie: ")
            newDesc = input(">Give the new description of the movie: ")
            newGenre = input(">Give the new genre of the movie: ")  
            self._service._updateMovie(newId, newTitle, newDesc, newGenre)
        elif which == "c":
            newId = input(">Give id of the client you'd like to update: ")
            newName = input(">Give the new name of the client: ")
            self._service._updateClient(newId, newName)
        else:
            raise CustomError("Please type either m or c")

    def _listItems(self):
        '''
        Function lists item from a list
        '''
        which = input(">Would you like to list movies or clients?\n>For movies type: m\n>For clients type: c\n>")
        if which == "m":
            myList = self._service._getMovies()
        elif which == "c":
            myList = self._service._getClients()
        elif which == "r":
            myList = self._service._getRentals()
        else:
            raise CustomError("Please type either m or c")
        
        for item in myList:
            print(item)

    def _rentMovie(self):
        rentalId = input(">Give this rental a unique id: ")
        movieId = input(">Which movie would you like to rent? Type its id: ")
        clientId = input(">Which client is going to rent this movie? Type their id: ")
        print(">When does the client want to return the movie?")
        day = input(">Give day: ")
        month = input(">Give month: ")
        year = input(">Give year: ")
        dueDate = Date(day, month, year)
        self._service._rentMovie(rentalId, movieId, clientId, dueDate)


    def _returnMovie(self):
        movieId = input(">Give id of the movie you are returning: ")
        self._service._returnMovie(movieId)

    def _search(self):
        which = input("What would you like to search for?\nFor movies type: m\nFor clients type: c\nFor everything type: e\n>")
        if which not in ["m", "c", "e"]:
            raise CustomError("Please type either m, c or e")
        key = input(">Type a key word for the search: ")
        key.casefold()
        myList = []
        if which == "m":
            myList = self._service._searchMovies(key)
        elif which == "c":
            myList = self._service._searchClients(key)
        else:
            myList = self._service._searchAll(key)

        for item in myList:
            print(item)

    def _stats(self):
        which = input("For which category would you like stats?\nFor movies type: m\nFor clients type: c\nFor rentals type: r\n>")
        if which not in ["m", "c", "r"]:
            raise CustomError("Please type either m, c or  r")
        myList = []
        if which == "m":
            myList = self._service._movieStats()
        elif which == "c":
            myList = self._service._clientStats()
        else:
            myList = self._service._rentalStats()
        for item in myList:
            print(item)

    def _undo(self):
        self._service._undo()

    def _redo(self):
        self._service._redo()

    def _start(self):
        
        commands = {
            "1" : self._addItem,
            "2" : self._removeItem,
            "3" : self._updateItem,
            "4" : self._listItems,
            "5" : self._rentMovie,
            "6" : self._returnMovie,
            "7" : self._search,
            "8" : self._stats,
            "9" : self._undo,
            "10": self._redo
        }

        while True:
            self._printMenu()
            command = input(">Give command: ")
            print("")
            try:
                if command == "0":
                    break
                elif command in commands.keys():
                    commands[command]()
                else:
                    print("Invalid command")
            except Exception as e:
                print(e)

            print("")
            system("pause")
            system("cls")
            
ui = UI()
ui._start()