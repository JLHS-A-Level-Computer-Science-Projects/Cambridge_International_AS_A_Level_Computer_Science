#Created by 4AMAlan

# 定义 TreasureChest 类
class TreasureChest:
	# 构造函数，初始化对象的属性
	def __init__(self, q, a, p): # 注意：原代码中 'init' 前缺少下划线，这里修正为 '__init__'
		# 私有属性，存储问题字符串
		self.__question = q      #Private attribute, type: STRING
		# 私有属性，存储答案整数
		self.__answer = a        #Private attribute, type: INTEGER
		# 私有属性，存储该宝箱可获得的最大分数
		self.__points = p        #Private attribute, type: INTEGER

	# 获取问题的方法
	def getQuestion(self):
		# 返回存储的问题字符串
		return self.__question

	# 检查用户答案是否正确的方法
	def checkAnswer(self, ua):
		# 将存储的答案转换为整数并与用户输入的答案进行比较
		if ua == int(self.__answer):
			# 如果答案正确，返回 True
			return True
		else:
			# 如果答案错误，返回 False
			return False

	# 根据尝试次数计算并返回得分的方法
	def getPoints(self, noa):
		# 如果只尝试了一次就答对了
		if noa == 1:
			# 返回全部分数
			return self.__points
		# 如果尝试了两次才答对
		elif noa == 2:
			# 返回一半的分数 (整数除法)
			return self.__points // 2
		# 如果尝试了三次或四次才答对
		elif noa == 3 or noa == 4:
			# 返回四分之一的分数 (整数除法)
			return self.__points // 4
		# 如果尝试次数超过四次
		else:
			# 返回零分
			return 0

# 全局数组，用于存储 TreasureChest 对象实例
arrayTreasure = []

# 定义读取数据的函数
def readData():
	# 声明使用全局变量 arrayTreasure
	global arrayTreasure
	try:
		# 尝试打开名为 "TreasureChestData.txt" 的文件进行读取
		f = open("TreasureChestData.txt", "r")
	except:
		# 如果文件未找到，则输出错误信息
		print("No such file or directory")
		# 如果文件打开失败，函数直接结束，避免后续操作
		return

	# 循环读取文件中的数据
	while True:
		# 读取一行作为问题
		QuestionLine = f.readline().strip()
		# 读取下一行作为答案
		AnswerLine = f.readline().strip()
		# 读取再下一行作为分数
		Points = f.readline().strip()

		# 检查是否读取到空行，如果任一行为空，则表示文件末尾，跳出循环
		if not QuestionLine or not AnswerLine or not Points:
			break

		# 使用读取到的数据创建一个 TreasureChest 对象实例
		# 注意：构造函数期望第二个参数是整数，这里直接传入字符串 'AnswerLine' 和 'Points' 是不正确的
		# 正确做法应该是：Question = TreasureChest(QuestionLine, int(AnswerLine), int(Points))
		Question = TreasureChest(QuestionLine, AnswerLine, Points)

		# 将新创建的对象添加到全局数组中
		arrayTreasure.append(Question)

	# 关闭文件
	f.close()

# 调用 readData 函数来加载数据
readData()

# 提示用户输入问题编号
QuestionNumber = int(input("Please enter question number:"))

# 检查用户输入的问题编号是否在有效范围内 (1 到 5)
if 1 <= QuestionNumber <= 5:
	# 初始化结果标志为 False，表示答案尚未正确
	result = False
	# 初始化尝试次数计数器
	NumberOfAttempts = 0

	# 当用户答案不正确时，循环继续
	while result == False:
		# 输出对应编号的问题
		print(arrayTreasure[QuestionNumber - 1].getQuestion())
		# 提示用户输入答案
		UserAnswer = int(input("Please enter answer:"))
		# 检查用户输入的答案是否正确，并更新 result 变量
		result = arrayTreasure[QuestionNumber - 1].checkAnswer(UserAnswer)
		# 无论答案是否正确，尝试次数都加一
		NumberOfAttempts += 1

	# 用户答对后，调用 getPoints 方法计算得分并输出
	print(arrayTreasure[QuestionNumber - 1].getPoints(NumberOfAttempts))
else:
	# 如果输入的问题编号无效，则输出提示信息
	print("Invalid question number")
