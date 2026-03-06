#Created by 4AMAlan

import datetime  # 导入datetime模块，用于处理日期

class LibraryItem:
	def __init__(self, t, a, i):
		# 初始化方法，创建一个LibraryItem对象
		self.__Title = t                          #Private attribute, Type: STRING
		self.__Author_Artist = a                  #Private attribute, Type: STRING
		self.__ItemID = i                         #Private attribute, Type: INTEGER
		self.__OnLoan = False                     #Private attribute, Type: BOOLEAN
		self.__DueDate = datetime.date.today()    #Private attribute, Type: DATE

	def GetTitle(self):
		# 获取并返回图书标题的方法
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

	def GetIsRequested(self):
		# 获取并返回IsRequested状态的方法
		return self.__IsRequested

	def SetIsRequested(self):
		# 将IsRequested状态设置为True的方法
		self.__IsRequested = True

class CD(LibraryItem):
	def __init__(self, t, a, i):
		# 初始化方法，创建一个CD对象，继承自LibraryItem
		LibraryItem.__init__(self, t, a, i)
		self.__Genre = ""                       #Private attribute, Type: STRING

	def GetGenre(self):
		# 获取并返回CD流派的方法
		return self.__Genre

	def SetGenre(self, g):
		# 设置CD流派的方法
		self.__Genre = g

# 创建一个Book对象Book1
Book1 = Book("Cambridge International AS & A-Level Computer Science", "Sylvia Langfield & Dave Duddell", 114514)

# 对Book1执行一系列操作
Book1.PrintDetails()      # 打印Book1的初始详情
Book1.GetTitle()          # 获取Book1的标题（但未保存返回值）
Book1.Borrowing()         # 借阅Book1，更新其状态和还书日期
Book1.GetIsRequested()    # 检查Book1的请求状态（但未保存返回值）
Book1.PrintDetails()      # 打印借阅后的详情
Book1.SetIsRequested()    # 将Book1的请求状态设为True
Book1.Returning()         # 归还Book1，将其OnLoan状态设为False
Book1.PrintDetails()      # 打印归还后的详情

print() # 打印一个空行，用于分隔输出

# 创建一个CD对象CD1
CD1 = CD("Tiny Daydream", "Liyuu", 240601)

# 对CD1执行一系列操作
CD1.PrintDetails()        # 打印CD1的初始详情
CD1.GetTitle()            # 获取CD1的标题（但未保存返回值）
CD1.Borrowing()           # 借阅CD1，更新其状态和还书日期
CD1.PrintDetails()        # 打印借阅后的详情
CD1.SetGenre("Pop")       # 将CD1的流派设置为"Pop"
CD1.GetGenre()            # 获取CD1的流派（但未保存返回值）
CD1.Returning()           # 归还CD1，将其OnLoan状态设为False
CD1.PrintDetails()        # 打印归还后的详情