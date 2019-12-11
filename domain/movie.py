class Movie():

    def __init__(self, myid, title, description, genre):
        self.Id = myid
        self.Title = title
        self.Description = description
        self.Genre = genre

    @property
    def Id(self):
        return self._id
    @Id.setter
    def Id(self, value):
        self._id = value

    @property
    def Title(self):
        return self._title
    @Title.setter
    def Title(self, value):
        self._title = value

    @property 
    def Description(self):
        return self._description
    @Description.setter
    def Description(self, value):
        self._description = value

    @property
    def Genre(self):
        return self._genre
    @Genre.setter
    def Genre(self, value):
        self._genre = value    

    def __str__(self):
        string = ""
        string = string + "Movie -"+ self._title + "- has id=" + str(self._id) + ", its main genre is " + self._genre + ".\n"
        string = string + "A short description for this movie would be: " + self._description + "."
        return string

    def _copy(self):
        return Movie(self._id, self._title, self._description, self._genre)