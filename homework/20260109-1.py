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

    def SetIsRequested(self, borrower_id):
        self.__IsRequested = True
        self.__RequestedBy = borrower_id

    def GetRequestedBy(self):
        return self.__RequestedBy

    def PrintDetails(self):
        print("Book Details")
        LibraryItem.PrintDetails(self)
        print("Is Requested:", self.__IsRequested)
        print("Requested By:", self.__RequestedBy)

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

def borrow_book():
    book_id = int(input("Enter book ID: "))
    borrower_id = int(input("Enter borrower ID: "))
    
    for book in books:
        if book._LibraryItem__ItemID == book_id:
            for borrower in borrowers:
                if borrower.GetBorrowerID() == borrower_id:
                    book.Borrowing()
                    borrower.UpdateItemOnLoan(borrower.GetItemsOnLoan() + 1)
                    print("Book borrowed successfully")
                    return
    print("Book or borrower not found")

def return_book():
    book_id = int(input("Enter book ID: "))
    borrower_id = int(input("Enter borrower ID: "))
    
    for book in books:
        if book._LibraryItem__ItemID == book_id:
            for borrower in borrowers:
                if borrower.GetBorrowerID() == borrower_id:
                    book.Returning()
                    borrower.UpdateItemOnLoan(borrower.GetItemsOnLoan() - 1)
                    print("Book returned successfully")
                    return
    print("Book or borrower not found")

def borrow_cd():
    cd_id = int(input("Enter CD ID: "))
    borrower_id = int(input("Enter borrower ID: "))
    
    for cd in cds:
        if cd._LibraryItem__ItemID == cd_id:
            for borrower in borrowers:
                if borrower.GetBorrowerID() == borrower_id:
                    cd.Borrowing()
                    borrower.UpdateItemOnLoan(borrower.GetItemsOnLoan() + 1)
                    print("CD borrowed successfully")
                    return
    print("CD or borrower not found")

def return_cd():
    cd_id = int(input("Enter CD ID: "))
    borrower_id = int(input("Enter borrower ID: "))
    
    for cd in cds:
        if cd._LibraryItem__ItemID == cd_id:
            for borrower in borrowers:
                if borrower.GetBorrowerID() == borrower_id:
                    cd.Returning()
                    borrower.UpdateItemOnLoan(borrower.GetItemsOnLoan() - 1)
                    print("CD returned successfully")
                    return
    print("CD or borrower not found")

def request_book():
    book_id = int(input("Enter book ID: "))
    borrower_id = int(input("Enter borrower ID: "))
    
    for book in books:
        if book._LibraryItem__ItemID == book_id:
            book.SetIsRequested(borrower_id)
            print("Book requested successfully")
            return
    print("Book not found")

def print_all_details():
    print("\n=== ALL BORROWERS ===")
    for borrower in borrowers:
        borrower.PrintDetails()
        print()
    
    print("\n=== ALL BOOKS ===")
    for book in books:
        book.PrintDetails()
        print()
    
    print("\n=== ALL CDs ===")
    for cd in cds:
        cd.PrintDetails()
        print()

def add_new_borrower():
    name = input("Enter borrower's name: ")
    borrower_id = int(input("Enter borrower's ID: "))
    borrowers.append(Borrower(name, borrower_id))
    print("Added")

def add_new_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    item_id = int(input("Enter book ID (integer): "))
    books.append(Book(title, author, item_id))
    print("Added")

def add_new_cd():
    title = input("Enter CD title: ")
    artist = input("Enter artist: ")
    item_id = int(input("Enter CD ID (integer): "))
    cds.append(CD(title, artist, item_id))
    print("Added")


borrowers = []
books = []
cds = []
while True:
    print("1 - Add a new borrower")
    print("2 - Add a new book")
    print("3 - Add a new CD")
    print("4 - Borrow a book")
    print("5 - Return a book")
    print("6 - Borrow a CD")
    print("7 - Return a CD")
    print("8 - Request book")
    print("9 - Print all details")
    print("99 - Exit program")

    choice = int(input("Enter your menu choice: "))

    if choice == 1:
        add_new_borrower()
    elif choice == 2:
        add_new_book()
    elif choice == 3:
        add_new_cd()
    elif choice == 4:
        borrow_book()
    elif choice == 5:
        return_book()
    elif choice == 6:
        borrow_cd()
    elif choice == 7:
        return_cd()
    elif choice == 8:
        request_book()
    elif choice == 9:
        print_all_details()
    elif choice == 99:
        break
    else:
        print("Invalid")
