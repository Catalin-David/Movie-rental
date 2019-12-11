class Date:
    def __init__(self, day, month, year):
        self._day = int(day)
        self._month = int(month)
        self._year = int(year)

    @property
    def Year(self):
        return self._year
    
    @property
    def Month(self):
        return self._month

    @property
    def Day(self):
        return self._day

    def __sub__(self, other):
        if isinstance(other, Date) == False:
            return 0
        return (self._year-other.Year)*365 + (self._month-other.Month)*30 + self._day-other.Day

    def __eq__(self, other):
        if isinstance(other, Date) == False:
            return False

        return self._year == other.Year and self._month == other.Month and self._day == other.Day

    def __lt__(self, other):
        if isinstance(other, Date) == False:
            return False
        
        if self._year == other.Year:
            if self._month == other.Month:
                if self._day == other.Day:
                    return self._day < other.Day
            else:
                return self._month < other.Month
        else:
            return self._year < other.Year

    def __str__(self):
        string = ""
        string = string + str(self._day) + "/" + str(self._month) + "/" + str(self._year)
        return string

class Rental:
    def __init__(self, rentalId, movieId, clientId, rentedDate, dueDate, returnedDate=Date(0,0,0)):
        self.RentalId = rentalId
        self.MovieId = movieId
        self.ClientId = clientId
        self.RentedDate = rentedDate
        self.DueDate = dueDate
        self.ReturnedDate = returnedDate

    @property
    def RentalId(self):
        return self._rentalId
    @RentalId.setter
    def RentalId(self, value):
        self._rentalId = value

    @property
    def MovieId(self):
        return self._movieId
    @MovieId.setter
    def MovieId(self, value):
        self._movieId = value

    @property
    def ClientId(self):
        return self._clientId
    @ClientId.setter
    def ClientId(self, value):
        self._clientId = value

    @property
    def RentedDate(self):
        return self._rentedDate
    @RentedDate.setter
    def RentedDate(self, value):
        self._rentedDate = value

    @property
    def DueDate(self):
        return self._dueDate
    @DueDate.setter
    def DueDate(self, value):
        self._dueDate = value

    @property
    def ReturnedDate(self):
        return self._returnedDate
    @ReturnedDate.setter
    def ReturnedDate(self, date):
        self._returnedDate = date

    def __str__(self):
        string =""
        string = string + "Rental " + self._rentalId +", movie " + self._movieId + ", client " + self._clientId + ": " + str(self._rentedDate) + " -> " + str(self._dueDate) + ", " + str(self._returnedDate)
        return string