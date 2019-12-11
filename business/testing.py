from domain.client import Client
from domain.movie import Movie
from repo.repo import Repository
import unittest

class PerformTests(unittest.TestCase):
    def __init__(self):
        super().__init__()
        # Test Client class
        client = Client("001", "Gheorghe Vasile")
        self.assertEquals(client.Id, "001")
        self.assertEquals(client.Name, "Gheorghe Vasile")
        self.assertEquals(str(client), "The client's name is Gheorghe Vasile and their id is 001.")

        client.Name = "Andrei Pop"
        self.assertEquals(client.Name, "Andrei Pop")

        # Test Movie class
        movie = Movie("001", "Movie A", "Short description", "Genre C")
        self.assertEquals(movie.Id, "001")
        self.assertEquals(movie.Title, "Movie A")
        self.assertEquals(movie.Description, "Short description")
        self.assertEquals(movie.Genre, "Genre C")

        movie.Title = "New Title"
        self.assertEquals(movie.Title, "New Title")