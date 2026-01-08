import datetime

class LibraryItem:
    def __init__(self, t, a, i):
        self.__Title = t
        self.__Author_Artist = a
        self.__ItemID = i
        self.__OnLoan = False
        self.__DueDate = datetime.date.today()

    def GetTitle(self):
        return self.__Title

    def GetItemID(self): # 新增方法，用于通过ID查找项目
        return self.__ItemID

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
        print("-" * 30)


class Book(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__IsRequested = False
        self.__RequestedBy = 0

    def GetIsRequested(self):
        return self.__IsRequested

    def SetIsRequested(self):
        self.__IsRequested = True

    def GetRequestedBy(self): # 新增方法，用于获取请求者ID
        return self.__RequestedBy

    def SetRequestedBy(self, borrower_id): # 新增方法，用于设置请求者ID
        self.__RequestedBy = borrower_id


class CD(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__Genre = ""

    def GetGenre(self):
        return self.__Genre

    def SetGenre(self, g):
        self.__Genre = g


class Borrower: # 新增类，用于管理借阅者
    def __init__(self, name, borrower_id):
        self.__Name = name
        self.__BorrowerID = borrower_id
        self.__ItemsOnLoan = [] # 存储当前借阅的物品ID列表

    def GetName(self):
        return self.__Name

    def GetBorrowerID(self):
        return self.__BorrowerID

    def AddItemOnLoan(self, item_id):
        self.__ItemsOnLoan.append(item_id)

    def RemoveItemOnLoan(self, item_id):
        if item_id in self.__ItemsOnLoan:
            self.__ItemsOnLoan.remove(item_id)

    def GetItemsOnLoan(self):
        return self.__ItemsOnLoan.copy() # 返回副本，避免外部修改

    def PrintDetails(self):
        print("Borrower Name:", self.__Name)
        print("Borrower ID:", self.__BorrowerID)
        print("Items on Loan:", self.__ItemsOnLoan)
        print("-" * 30)


# 初始化全局数据结构
borrowers = []
books = []
cds = []

def add_new_borrower():
    name = input("Enter borrower's name: ")
    borrower_id = int(input("Enter borrower's ID (integer): "))
    new_borrower = Borrower(name, borrower_id)
    borrowers.append(new_borrower)
    print("Borrower '", name, "' with ID ", borrower_id, " added successfully.", sep='')


def add_new_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    item_id = int(input("Enter book ID (integer): "))
    new_book = Book(title, author, item_id)
    books.append(new_book)
    print("Book '", title, "' by ", author, " with ID ", item_id, " added successfully.", sep='')


def add_new_cd():
    title = input("Enter CD title: ")
    artist = input("Enter artist: ")
    item_id = int(input("Enter CD ID (integer): "))
    new_cd = CD(title, artist, item_id)
    cds.append(new_cd)
    print("CD '", title, "' by ", artist, " with ID ", item_id, " added successfully.", sep='')


def find_item_by_id(item_id):
    # 在所有书籍和CD中查找指定ID的项目
    for book in books:
        if book.GetItemID() == item_id:
            return book
    for cd in cds:
        if cd.GetItemID() == item_id:
            return cd
    return None


def find_borrower_by_id(borrower_id):
    # 根据借阅者ID查找借阅者
    for borrower in borrowers:
        if borrower.GetBorrowerID() == borrower_id:
            return borrower
    return None


def borrow_book():
    borrower_id = int(input("Enter your borrower ID: "))
    borrower = find_borrower_by_id(borrower_id)
    if not borrower:
        print("Borrower not found.")
        return

    item_id = int(input("Enter the book ID you want to borrow: "))
    item = find_item_by_id(item_id)
    if not item:
        print("Item not found.")
        return

    if not isinstance(item, Book):
        print("The specified item is not a book.")
        return

    if item._LibraryItem__OnLoan: # 检查是否已借出
        print("This book is already on loan.")
        return

    item.Borrowing()
    borrower.AddItemOnLoan(item_id)
    print("Book '", item.GetTitle(), "' has been borrowed successfully by ", borrower.GetName(), ".", sep='')


def return_book():
    borrower_id = int(input("Enter your borrower ID: "))
    borrower = find_borrower_by_id(borrower_id)
    if not borrower:
        print("Borrower not found.")
        return

    item_id = int(input("Enter the book ID you want to return: "))
    item = find_item_by_id(item_id)
    if not item:
        print("Item not found.")
        return

    if not isinstance(item, Book):
        print("The specified item is not a book.")
        return

    if not item._LibraryItem__OnLoan: # 检查是否在借阅状态
        print("This book is not currently on loan.")
        return

    item.Returning()
    borrower.RemoveItemOnLoan(item_id)
    print("Book '", item.GetTitle(), "' has been returned successfully.", sep='')


def borrow_cd():
    borrower_id = int(input("Enter your borrower ID: "))
    borrower = find_borrower_by_id(borrower_id)
    if not borrower:
        print("Borrower not found.")
        return

    item_id = int(input("Enter the CD ID you want to borrow: "))
    item = find_item_by_id(item_id)
    if not item:
        print("Item not found.")
        return

    if not isinstance(item, CD):
        print("The specified item is not a CD.")
        return

    if item._LibraryItem__OnLoan: # 检查是否已借出
        print("This CD is already on loan.")
        return

    item.Borrowing()
    borrower.AddItemOnLoan(item_id)
    print("CD '", item.GetTitle(), "' has been borrowed successfully by ", borrower.GetName(), ".", sep='')


def return_cd():
    borrower_id = int(input("Enter your borrower ID: "))
    borrower = find_borrower_by_id(borrower_id)
    if not borrower:
        print("Borrower not found.")
        return

    item_id = int(input("Enter the CD ID you want to return: "))
    item = find_item_by_id(item_id)
    if not item:
        print("Item not found.")
        return

    if not isinstance(item, CD):
        print("The specified item is not a CD.")
        return

    if not item._LibraryItem__OnLoan: # 检查是否在借阅状态
        print("This CD is not currently on loan.")
        return

    item.Returning()
    borrower.RemoveItemOnLoan(item_id)
    print("CD '", item.GetTitle(), "' has been returned successfully.", sep='')


def request_book():
    borrower_id = int(input("Enter your borrower ID: "))
    borrower = find_borrower_by_id(borrower_id)
    if not borrower:
        print("Borrower not found.")
        return

    item_id = int(input("Enter the book ID you want to request: "))
    item = find_item_by_id(item_id)
    if not item:
        print("Item not found.")
        return

    if not isinstance(item, Book):
        print("The specified item is not a book.")
        return

    item.SetIsRequested()
    item.SetRequestedBy(borrower_id) # 记录是哪个借阅者请求的
    print("Book '", item.GetTitle(), "' has been requested successfully by ", borrower.GetName(), ".", sep='')


def print_all_details():
    print("\n=== ALL BORROWERS ===")
    for borrower in borrowers:
        borrower.PrintDetails()

    print("\n=== ALL BOOKS ===")
    for book in books:
        book.PrintDetails()

    print("\n=== ALL CDs ===")
    for cd in cds:
        cd.PrintDetails()


def main_menu():
    while True:
        print("\n" + "="*50)
        print("          LIBRARY SYSTEM MENU")
        print("="*50)
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
        print("="*50)

        try:
            choice = int(input("Enter your menu choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

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
            print("Exiting the library system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


# --- 主程序入口 ---
if __name__ == "__main__":
    # 可以在这里预先添加一些示例数据，方便测试
    # 创建一个示例借阅者
    sample_borrower = Borrower("4AMAlan", 114514)
    borrowers.append(sample_borrower)

    # 创建一个示例图书
    sample_book = Book("Cambridge International AS & A-Level Computer Science", "Sylvia Langfield & Dave Duddell", 1919810)
    books.append(sample_book)

    # 创建一个示例CD
    sample_cd = CD("Tiny Daydream", "Liyuu", 109)
    sample_cd.SetGenre("Anime")
    cds.append(sample_cd)

    print("Welcome to the Library System!")
    main_menu()

