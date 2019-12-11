class CustomError(Exception):

    def __init__(self, message):
        self._message = message

    def _print_message(self):
        print(self._message)