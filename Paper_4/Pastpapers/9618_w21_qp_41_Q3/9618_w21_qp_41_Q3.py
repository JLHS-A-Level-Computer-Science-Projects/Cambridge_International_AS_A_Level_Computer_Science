#Created by 4AMAlan

NULLPOINTER = -1  # 定义空指针值，用于表示树中没有子节点的位置

# 创建一个20行3列的二维数组，用于模拟静态二叉树
# 每行代表一个节点，三列分别表示：左子节点索引、数据值、右子节点索引
ArrayNodes = [[0 for i in range(3)] for i in range(20)]
RootPointer = NULLPOINTER  # 根节点指针，初始为-1表示树为空
FreeNode = 0  # 空闲节点指针，指向下一个可用的数组位置

def AddNode(arrayNodes, rootPointer, freeNode):
	"""
	向二叉搜索树中添加新节点的函数
	参数：
	- arrayNodes: 存储节点的二维数组
	- rootPointer: 根节点指针
	- freeNode: 空闲节点指针
	"""
	global ArrayNodes, RootPointer, FreeNode
	# 获取用户输入的数据
	NodeData = int(input("Please input data:"))
	# 检查是否有空闲空间（数组未满）
	if FreeNode <= 19:
		# 初始化新节点：左子节点指针设为-1，数据值设为输入值，右子节点指针设为-1
		ArrayNodes[FreeNode][0] = -1  # 左子节点指针
		ArrayNodes[FreeNode][1] = NodeData  # 数据值
		ArrayNodes[FreeNode][2] = -1  # 右子节点指针
		# 如果树为空（根节点指针为-1），则将新节点设为根节点
		if RootPointer == NULLPOINTER:
			RootPointer = 0
		else:
			# 如果树不为空，则遍历树找到合适位置插入新节点
			Placed = False  # 标记节点是否已放置
			CurrentNode = RootPointer  # 从根节点开始遍历
			# 循环直到找到合适位置
			while Placed == False:
				# 如果新数据小于当前节点的数据，则向左子树查找
				if NodeData < ArrayNodes[CurrentNode][1]:
					# 如果当前节点的左子节点为空，则将新节点插入此处
					if ArrayNodes[CurrentNode][0] == -1:
						ArrayNodes[CurrentNode][0] = FreeNode
						Placed = True
					# 否则继续向左子树遍历
					else:
						CurrentNode = ArrayNodes[CurrentNode][0]
				# 如果新数据大于等于当前节点的数据，则向右子树查找
				else:
					# 如果当前节点的右子节点为空，则将新节点插入此处
					if ArrayNodes[CurrentNode][2] == -1:
						ArrayNodes[CurrentNode][2] = FreeNode
						Placed = True
					# 否则继续向右子树遍历
					else:
						CurrentNode = ArrayNodes[CurrentNode][2]
		# 更新空闲节点指针，指向下一个可用位置
		FreeNode = FreeNode + 1
	else:
		# 如果数组已满，输出错误信息
		print("Tree is full")

def PrintAll():
	"""
	打印所有节点信息的函数
	按行打印每个节点的左子节点指针、数据值和右子节点指针
	"""
	for i in range(20):
		print(ArrayNodes[i][0], "  ", ArrayNodes[i][1], "  ", ArrayNodes[i][2])

def InOrder(CurrentNode):
	"""
	中序遍历二叉搜索树的函数
	按照左子树-根节点-右子树的顺序遍历并打印节点数据
	参数：
	- CurrentNode: 当前遍历的节点索引
	"""
	global ArrayNodes
	# 如果当前节点不是空节点，则继续遍历
	if CurrentNode != NULLPOINTER:
		# 递归遍历左子树
		InOrder(ArrayNodes[CurrentNode][0])
		# 打印当前节点的数据
		print(ArrayNodes[CurrentNode][1], end = " ")
		# 递归遍历右子树
		InOrder(ArrayNodes[CurrentNode][2])

# 主程序：循环添加10个节点到二叉搜索树
for i in range(10):
	AddNode(ArrayNodes, RootPointer, FreeNode)

# 打印所有节点信息
PrintAll()
print()
# 中序遍历并打印树中的数据
InOrder(RootPointer)