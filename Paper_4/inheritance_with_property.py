import datetime  # 导入datetime模块，用于处理日期

class LibraryItem:
	def __init__(self, t, a, i):
		# 初始化方法，创建一个LibraryItem对象
		self.__Title = t                          #Private attribute, Type: STRING
		self.__Author_Artist = a                  #Private attribute, Type: STRING
		self.__ItemID = i                         #Private attribute, Type: INTEGER
		self.__OnLoan = False                     #Private attribute, Type: BOOLEAN
		self.__DueDate = datetime.date.today()    #Private attribute, Type: DATE

	@property
	def Title(self):
		# 使用@property装饰器创建一个只读属性Title，提供对私有属性__Title的安全访问
		# 这是与无property版本的主要区别：允许像访问公共属性一样访问私有属性
		# 例如：title = item.Title
		return self.__Title

	def Borrowing(self):
		# 处理借阅的方法，将OnLoan状态设为True，并将还书日期设置为当前日期加3周
		self.__OnLoan = True
		self.__DueDate = self.__DueDate + datetime.timedelta(weeks = 3)

	def Returning(self):
		# 处理归还的方法，将OnLoan状态设为False
		self.__OnLoan = False

	def PrintDetails(self):
		# 打印图书详细信息的方法
		print(self.__Title, ",", self.__Author_Artist, ",")
		print(self.__ItemID, ",", self.__OnLoan, ",", self.__DueDate)

class Book(LibraryItem):
	def __init__(self, t, a, i):
		# 初始化方法，创建一个Book对象，继承自LibraryItem
		LibraryItem.__init__(self, t, a, i)
		self.__IsRequested = False              #Private attribute, Type: BOOLEAN
		self.__RequestedBy = 0                  #Private attribute, Type: INTEGER

	@property
	def IsRequested(self):
		# 使用@property装饰器创建一个属性IsRequested，提供对私有属性__IsRequested的安全访问
		# 这使得外部代码可以像访问公共属性一样获取其值
		# 例如：status = book.IsRequested
		return self.__IsRequested

	@IsRequested.setter
	def IsRequested(self, b):
		# 使用@IsRequested.setter装饰器创建一个setter方法
		# 这使得外部代码可以像设置公共属性一样修改其值
		# 例如：book.IsRequested = True
		# 这是与无property版本的关键区别：提供了直接赋值的接口，但仍然保持了封装性
		self.__IsRequested = b

	def BookPrintDetails(self):
		# 专门用于打印书籍详细信息的方法，调用了父类的PrintDetails
		print("Book Details")
		LibraryItem.PrintDetails(self)
		print(self.IsRequested)

class CD(LibraryItem):
	def __init__(self, t, a, i):
		# 初始化方法，创建一个CD对象，继承自LibraryItem
		LibraryItem.__init__(self, t, a, i)
		self.__Genre = ""                       #Private attribute, Type: STRING

	@property
	def Genre(self):
		# 使用@property装饰器创建一个属性Genre，提供对私有属性__Genre的安全访问
		# 例如：genre = cd.Genre
		return self.__Genre

	@Genre.setter
	def Genre(self, g):
		# 使用@Genre.setter装饰器创建一个setter方法
		# 这使得外部代码可以像设置公共属性一样修改其值
		# 例如：cd.Genre = "Pop"
		# 这是与无property版本的关键区别：提供了直接赋值的接口，但仍然保持了封装性
		self.__Genre = g

	def CDPrintDetails(self):
		# 专门用于打印CD详细信息的方法，调用了父类的PrintDetails
		print("CD Details")
		LibraryItem.PrintDetails(self)
		print(self.__Genre)

# 创建一个Book对象Book1
Book1 = Book("Cambridge International AS & A-Level Computer Science", "Sylvia Langfield & Dave Duddell", 114514)

# 对Book1执行一系列操作
Book1.PrintDetails()      # 打印Book1的初始详情
print()                   # 打印一个空行，用于分隔输出
Book1.Borrowing()         # 借阅Book1，更新其状态和还书日期
Book1.IsRequested = True  # 使用property setter设置IsRequested状态
                          # 这是与无property版本的关键区别：可以直接赋值，而不是调用SetIsRequested()方法
Book1.Returning()         # 归还Book1，将其OnLoan状态设为False
Book1.BookPrintDetails()  # 打印书籍的最终详情

print() # 打印一个空行，用于分隔输出

# 创建一个CD对象CD1
CD1 = CD("Tiny Daydream", "Liyuu", 240601)

# 对CD1执行一系列操作
CD1.PrintDetails()        # 打印CD1的初始详情
CD1.Borrowing()           # 借阅CD1，更新其状态和还书日期
CD1.Genre = "Pop"         # 使用property setter设置CD的流派
                          # 这是与无property版本的关键区别：可以直接赋值，而不是调用SetGenre()方法
print()                 
CD1.Returning()           # 归还CD1，将其OnLoan状态设为False
CD1.CDPrintDetails()      # 打印CD的最终详情

# 与无property版本的关键区别总结：
# 1. 访问属性：有property版本可以使用 `obj.PropertyName`，无property版本需要 `obj.GetPropertyName()`
# 2. 修改属性：有property版本可以使用 `obj.PropertyName = value`，无property版本需要 `obj.SetPropertyName(value)`
# 3. 语法更简洁，更像操作公共属性，但内部仍然保持了私有属性的封装性和控制力