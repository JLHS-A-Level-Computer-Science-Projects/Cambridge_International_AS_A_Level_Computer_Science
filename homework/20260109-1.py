import datetime

class LibraryItem:
    def __init__(self, t, a, i):
        self.__Title = t  #private, string
        self.__Author_Artist = a  #private, string
        self.__ItemID = i  #private, integer
        self.__OnLoan = False  #private, boolean
        self.__DueDate = datetime.date.today()  #private, date

    def GetTitle(self):
        return self.__Title

    def Borrowing(self):
        self.__OnLoan = True
        self.__DueDate = self.__DueDate + datetime.timedelta(weeks=3)

    def Returning(self):
        self.__OnLoan = False

    def PrintDetails(self):
        print("Title:", self.__Title)
        print("Author/Artist:", self.__Author_Artist)
        print("Item ID:", self.__ItemID)
        print("On Loan:", self.__OnLoan)
        print("Due Date:", self.__DueDate)

class Book(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__IsRequested = False  #private, boolean
        self.__RequestedBy = 0  #private, integer

    def GetIsRequested(self):
        return self.__IsRequested

    def SetIsRequested(self):
        self.__IsRequested = True

    def PrintDetails(self):
        print("Book Details")
        LibraryItem.PrintDetails(self)
        print("Is Requested:", self.__IsRequested)

class CD(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__Genre = ""  #private, string

    def GetGenre(self):
        return self.__Genre

    def SetGenre(self, g):
        self.__Genre = g

    def PrintDetails(self):
        print("CD Details")
        LibraryItem.PrintDetails(self)
        print("Genre:", self.__Genre)

class Borrower:
    def __init__(self, n, e, b):
        self.__BorrowerName = n  #private, string
        self.__EmailAddress = e  #private, string
        self.__BorrowerID = b  #private, integer
        self.__ItemsOnLoan = 0  #private, integer

    def GetBorrowerName(self):
        return self.__BorrowerName

    def GetEmailAddress(self):
        return self.__EmailAddress
    
    def GetBorrowerID(self):
        return self.__BorrowerID

    def GetItemsOnLoan(self):
        return self.__ItemsOnLoan

    def UpdateItemOnLoan(self, i):
        self.__ItemsOnLoan=i

    def PrintDetails(self):
        print("Borrower Name:", self.__BorrowerName)
        print("Email Address:", self.__EmailAddress)
        print("Borrower ID:", self.__BorrowerID)
        print("Items on Loan:", self.__ItemsOnLoan)
