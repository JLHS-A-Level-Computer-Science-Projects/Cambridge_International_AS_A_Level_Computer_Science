#Created by 4AMAlan

# 声明并初始化一个整数数组 NumberArray
NumberArray = [100, 85, 644, 22, 15, 8, 1]
# 定义变量用于存储当前要处理的元素值
LastTerm = 0        #type: INTEGER
# 定义变量用于存储当前比较的元素索引
CheckItem = 0       #type: INTEGER
# 定义布尔变量控制内层插入循环是否继续
LoopAgain = True    #type: BOOLEAN

# 递归实现的插入排序函数
def RecursiveInsertion(IntegerArray, NumberElements):         # Returns ARRAY OF INTEGER
	'''
	IntegerArray: type: ARRAY OF INTEGER - 待排序的数组
	NumberElements: type: INTEGER - 数组中需要排序的元素个数
	'''
	# 递归基础情况：如果数组只有一个或零个元素，则已经有序，直接返回
	if NumberElements<= 1:
		return IntegerArray
	else:
		# 递归调用，先将前 NumberElements-1 个元素排序
		RecursiveInsertion(IntegerArray, NumberElements - 1)
		# 取出最后一个元素（未排序部分的第一个），作为待插入的元素
		LastTerm = IntegerArray[NumberElements - 1]
		# 设置检查位置为已排序部分的最后一个元素的索引
		CheckItem = NumberElements - 2
		# 初始化循环标志
		LoopAgain = True
		# 检查边界和条件，确定是否需要移动元素
		if CheckItem < 0:
			# 如果检查项索引小于0，说明待插入元素应放在数组开头，无需移动
			LoopAgain = False
		else:
			# 如果检查项的值小于等于待插入值，说明找到了正确位置，无需移动
			if IntegerArray[CheckItem] <= LastTerm:
				LoopAgain = False

		# while 循环：向后移动所有大于待插入元素的值，为待插入元素腾出空间
		while LoopAgain:
			# 将较大的元素向右移动一位
			IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
			# 检查项索引向左移动一位
			CheckItem -= 1
			# 再次检查边界和条件，决定是否继续移动
			if CheckItem < 0:
				# 如果检查项索引小于0，说明待插入元素应放在数组开头
				LoopAgain = False
			else:
				# 如果检查项的值小于等于待插入值，说明找到了正确位置
				if IntegerArray[CheckItem] <= LastTerm:
					LoopAgain = False

		# 将待插入元素放入找到的正确位置
		IntegerArray[CheckItem + 1] = LastTerm
		# 返回排序后的数组
		return IntegerArray

# 调用递归插入排序函数，并打印结果
print("Recursive")
print(RecursiveInsertion(NumberArray, len(NumberArray)))

# 迭代实现的插入排序函数 (注意：原代码存在逻辑错误，此处保留原样)
def IterativeInsetion(ListToBeSorted):
	# 遍历列表中的每个元素（从第二个开始）
	for i in range(0, len(ListToBeSorted)):
		# 当前要排序的元素
		ItemToBeSorted = ListToBeSorted[i]
		# 当前元素的位置索引
		CurrentItem = i
		# 在已排序的部分中找到正确的插入位置
		# 注意：这里的条件 `CurrentItem > -1` 应该是 `CurrentItem > 0` 以避免访问 ListToBeSorted[-1]
		# 注意：赋值语句 `ListToBeSorted[CurrentItem] = ListToBeSorted[CurrentItem + 1]` 是错误的，应该是向左移动元素
		while ItemToBeSorted < ListToBeSorted[CurrentItem] and CurrentItem > 0:
			# 错误的赋值逻辑，会导致数据丢失和索引越界
			ListToBeSorted[CurrentItem] = ListToBeSorted[CurrentItem - 1]
			CurrentItem -= 1
		# 将元素放到找到的位置
		ListToBeSorted[CurrentItem] = ItemToBeSorted
		CurrentItem -= 1
		# 返回排序后的
		return ListToBeSorted

print("iterative")
print(IterativeInsetion(NumberArray))

def BinarySearch(IntegerArray, First, Last, ToFind):
	'''
	IntegerArray: type: ARRAY OF INTEGERS
	First: type: INTEGER
	Last: type: INTEGER
	ToFind: INTEGER
	'''
	Middle = (First + Last) // 2 + 1
	if ToFind == IntegerArray[Middle]:
		return Middle
	else:
		if First >= Last:
			return -1
		else:
			if ToFind < IntegerArray[Middle]:
				return BinarySearch(IntegerArray, First, Middle - 1, ToFind)
			else:
				return BinarySearch(IntegerArray, Middle - 1, Last, ToFind)

try:
	print(BinarySearch(NumberArray, 0, 6, 644))
except:
	print("Not Found")