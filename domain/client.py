class Client():

    def __init__(self, myid, name):
        self.Id = myid
        self.Name = name

    @property
    def Id(self):
        return self._id
    @Id.setter
    def Id(self, value):
        self._id = value

    @property
    def Name(self):
        return self._name
    @Name.setter
    def Name(self, value):
        self._name = value

    def __str__(self):
        string = "The client's name is " + self._name + " and their id is " + str(self._id) + "."
        return string

    def _copy(self):
        return Client(self._id, self._name)