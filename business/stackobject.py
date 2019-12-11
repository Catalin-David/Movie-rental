class StackObject:
    def __init__(self, name, params):
        self.Name = name
        self.Params = params

    @property
    def Name(self):
        return self._name
    @Name.setter
    def Name(self, value):
        self._name = value

    @property
    def Params(self):
        return self._params
    @Params.setter
    def Params(self, value):
        self._params = value