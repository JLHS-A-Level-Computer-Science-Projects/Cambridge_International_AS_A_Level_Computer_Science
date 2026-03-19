#Created by 4AMAlan

# 全局变量定义
# Jobs是一个二维数组，存储作业信息，每行包含作业编号和优先级
Jobs = [[0 for i in range(2)] for i in range(100)]
# NumberOfJobs记录当前已添加的作业数量
NumberOfJobs = 0

def Initialise():
	"""
	初始化作业队列的函数
	将Jobs数组中的所有元素初始化为-1，并将作业数量重置为0
	"""
	global Jobs, NumberOfJobs
	# 遍历整个Jobs数组，将所有元素初始化为-1（表示空位）
	for i in range(100):
		for j in range(2):
			Jobs[i][j] = -1
	# 将作业数量重置为0
	NumberOfJobs = 0

def AddJob(JobNumber,Priority):
	"""
	添加作业到队列的函数
	参数：
	- JobNumber: 作业编号
	- Priority: 作业优先级（数字越小优先级越高）
	"""
	global Jobs, NumberOfJobs
	# 标记作业是否成功添加
	AddFlag = False
	# 遍历Jobs数组，寻找空闲位置
	for i in range(100):
		# 如果找到空闲位置（用-1标识）
		if Jobs[i][0] == -1:
			# 在该位置添加作业信息
			Jobs[i][0] = JobNumber  # 存储作业编号
			Jobs[i][1] = Priority  # 存储作业优先级
			AddFlag = True  # 标记作业已添加
			NumberOfJobs += 1  # 作业总数加1
			break  # 退出循环
	# 根据作业是否成功添加，输出相应信息
	if AddFlag == True:
		print("Added")
	else:
		print("Not added")


def InsertionSort():
	"""
	使用插入排序算法按优先级对作业进行排序的函数
	优先级数字越小，优先级越高
	"""
	global Jobs, NumberOfJobs
	# 遍历从第1个到NumberOfJobs-1的作业
	for i in range(NumberOfJobs):
		# 保存当前作业的编号和优先级
		CurrentItem1 = Jobs[i][0]  # 当前作业编号
		CurrentItem2 = Jobs[i][1]  # 当前作业优先级
		# 当i>0且前一个作业的优先级大于当前作业优先级时，继续向前比较和移动
		# （优先级数字越小，优先级越高）
		while i > 0 and Jobs[i - 1][1] > CurrentItem2:
			# 将前一个作业的信息后移一位
			Jobs[i][0] = Jobs[i - 1][0]  # 移动作业编号
			Jobs[i][1] = Jobs[i - 1][1]  # 移动作业优先级
			i -= 1  # 继续向前比较
		# 将当前作业信息插入到正确位置
		Jobs[i][0] = CurrentItem1  # 插入作业编号
		Jobs[i][1] = CurrentItem2  # 插入作业优先级

def PrintArray():
	"""
	打印所有已添加作业信息的函数
	遍历Jobs数组，打印非空作业的编号和优先级
	"""
	global Jobs, NumberOfJobs
	# 遍历整个Jobs数组
	for i in range(100):
		# 如果该位置不是空位（作业编号不为-1）
		if Jobs[i][0] != -1:
			# 打印作业编号和优先级
			print(Jobs[i][0], "priority", Jobs[i][1])

# 程序主执行部分
# 1. 初始化作业队列
Initialise()
# 2. 添加5个作业到队列
AddJob(12,10)
AddJob(526,9)
AddJob(33,8)
AddJob(12,9)
AddJob(78,1)
# 3. 按优先级对作业进行排序（优先级数字越小，优先级越高）
InsertionSort()
# 4. 打印排序后的作业列表
PrintArray()