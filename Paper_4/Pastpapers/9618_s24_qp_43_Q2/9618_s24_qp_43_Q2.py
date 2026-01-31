# 定义 Tree 类，用于存储树木信息
class Tree:
	# 构造函数，初始化 Tree 对象的各个属性
	def __init__(self, n, g, h, w, e):
		# 私有属性，类型: 字符串
		self.__TreeName = n              
		# 私有属性，类型: 整数
		self.__HeightGrowth = g          
		# 私有属性，类型: 整数
		self.__MaxHeight = h             
		# 私有属性，类型: 整数
		self.__MaxWidth = w              
		# 私有属性，类型: 字符串
		self.__Evergreen = e             

	# 获取方法：返回树的名字
	def GetTreeName(self):
		return self.__TreeName

	# 获取方法：返回树每年的高度增长量
	def GetGrowth(self):
		return self.__HeightGrowth

	# 获取方法：返回树的最大高度
	def GetMaxHeight(self):
		return self.__MaxHeight

	# 获取方法：返回树的最大宽度
	def GetMaxWidth(self):
		return self.__MaxWidth

	# 获取方法：返回树是否为常绿树
	def GetEvergreen(self):
		return self.__Evergreen

# 从 "Trees.txt" 文件中读取数据，并创建 Tree 对象数组
def ReadData():
	# 类型: Tree
	TreeArray = []                       
	
	# 尝试打开文件 "Trees.txt" 进行读取
	try:
		f = open("Trees.txt", "r")
	# 如果文件不存在，则打印错误信息
	except:
		print("No such file or directory.")

	# 循环 9 次，因为文件中有 9 行数据
	for i in range(9):
		# 读取一行数据，去除首尾空白字符并按逗号分割
		TreeInfo = f.readline().strip().split(",")
		# 使用分割后的数据创建新的 Tree 对象，并添加到 TreeArray 列表中
		TreeArray.append(Tree(TreeInfo[0], int(TreeInfo[1]), int(TreeInfo[2]), int(TreeInfo[3]), TreeInfo[4]))

	# 关闭文件
	f.close()

	# 返回包含 Tree 对象的列表
	return TreeArray

# 打印单个 Tree 对象的信息
def PrintTrees(TreeObj):
	# 检查树是否为常绿树 ("Yes")
	if TreeObj.GetEvergreen() ==  "Yes ":
		# 如果是常绿树，打印这条消息
		print(TreeObj.GetTreeName(),  "has a maximum height ", TreeObj.GetMaxHeight(),  "a maximum width ", TreeObj.GetMaxWidth(),  "and grows ", TreeObj.GetGrowth(),  "cm a year. It does not lose leaves. ")
	else:
		# 如果不是常绿树 (即 "No")，打印这条消息
		print(TreeObj.GetTreeName(),  "has a maximum height ", TreeObj.GetMaxHeight(),  "a maximum width ", TreeObj.GetMaxWidth(),  "and grows ", TreeObj.GetGrowth(),  "cm a year. It loses its leaves each year. ")

# 主程序部分开始
# 调用 ReadData 函数，获取包含 Tree 对象的列表，并赋值给变量 Trees
Trees = ReadData()
# 调用 PrintTrees 函数，打印列表中第一个 Tree 对象的信息
PrintTrees(Trees[0])

# 根据用户输入的要求选择合适的树木
def ChooseTree(TreeList):
	# 提示用户输入对树的最大高度要求
	HeightRequirement = int(input("Please input your height requirement of the tree:"))
	# 提示用户输入对树的最大宽度要求
	WidthRequirement = int(input("Please input your width requirement of the tree:"))
	# 提示用户输入是否需要常绿树
	WhetherEvergreen = input("Is the tree evergreen? (Yes/No):")
	
	# 创建一个空列表，用于存储符合要求的树木对象
	TreeMeetRequirements = []

	# 遍历输入的 TreeList 列表
	for i in range(0, len(TreeList)):
		# 检查当前树是否满足所有条件：
		# 1. 最大高度 <= 用户要求的最大高度
		# 2. 最大宽度 <= 用户要求的最大宽度
		# 3. 是否常绿与用户要求一致
		if TreeList[i].GetMaxHeight() <= HeightRequirement and TreeList[i].GetMaxWidth() <= WidthRequirement and TreeList[i].GetEvergreen() == WhetherEvergreen:
			# 如果满足条件，将该树对象添加到 TreeMeetRequirements 列表中
			TreeMeetRequirements.append(TreeList[i])

	# 遍历所有符合条件的树木对象列表
	for i in range(0, len(TreeMeetRequirements)):
		# 打印每个符合条件的树木对象的信息
		PrintTrees(TreeMeetRequirements[i])

	# 提示用户输入想要购买的树名
	NameWantToBuy = input("Please input the tree name you want to buy:")
	# 提示用户输入购买时树的高度
	HeightWhenBought = int(input("Please input the height of the tree when you buy:"))
	
	# 遍历所有符合条件的树木对象列表
	for i in range(0, len(TreeMeetRequirements)):
		# 检查当前树名是否与用户输入的树名匹配（去除树名可能存在的空白字符）
		if TreeMeetRequirements[i].GetTreeName().strip() == NameWantToBuy:
			# 计算并打印这棵树长到最大高度所需的年数
			# 年数 = (最大高度 - 购买时高度) / 每年生长高度
			print("It takes", ((TreeMeetRequirements[i].GetMaxHeight() - HeightWhenBought) // TreeMeetRequirements[i].GetGrowth()), "years to grow to the maxmum height.")

# 调用 ChooseTree 函数，并传入 Trees 列表作为参数
ChooseTree(Trees)