from repo.repo import Repository
from domain.rental import *
import pickle
from repo_text.textrepo import TextRepo
class BinaryRepo(TextRepo):
    def __init__(self):
        super().__init__()
################################################################################################

    def _loadRentals(self):
        try:
            f = open("rentals.pickle", "rb")
            self._rentals = pickle.load(f)
        except Exception:
            self._rentals = []

    def _loadClients(self):
        try:
            f = open("clients.pickle", "rb")
            self._clients = pickle.load(f)
        except Exception:
            self._clients = []

    def _loadMovies(self):
        try:
            f = open("movies.pickle", "rb")
            self._movies = pickle.load(f)
        except Exception:
            self._movies = []

################################################################################################

    def _saveRentals(self):
        f = open("rentals.pickle", "wb")
        pickle.dump(self._rentals, f)

    def _saveClients(self):
        f = open("clients.pickle", "wb")
        pickle.dump(self._clients, f)

    def _saveMovies(self):
        f = open("movies.pickle", "wb")
        pickle.dump(self._movies, f)

################################################################################################