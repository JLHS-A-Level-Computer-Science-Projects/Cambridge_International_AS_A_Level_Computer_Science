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

# 迭代实现的插入排序函数
def IterativeInsetion(ListToBeSorted):
	# 遍历列表中的每个元素（从第二个开始）
	for i in range(0, len(ListToBeSorted)):
		# 当前要排序的元素
		ItemToBeSorted = ListToBeSorted[i]
		# 当前元素的位置索引
		CurrentItem = i
		# 在已排序的部分中找到正确的插入位置
		while ItemToBeSorted < ListToBeSorted[CurrentItem] and CurrentItem > 0:
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
    IntegerArray: type: ARRAY OF INTEGERS  # 待搜索的已排序整数数组
    First: type: INTEGER                   # 搜索范围的起始索引
    Last: type: INTEGER                    # 搜索范围的结束索引
    ToFind: INTEGER                        # 要查找的目标值
    '''
    # 计算中间索引：这里用 (First + Last) // 2 + 1
    Middle = (First + Last) // 2 + 1
    
    # 基本情况：如果中间元素正好等于目标值，返回中间索引
    if ToFind == IntegerArray[Middle]:
        return Middle
    else:
        # 如果搜索范围无效（起始索引大于等于结束索引），说明未找到，返回-1
        if First >= Last:
            return -1
        else:
            # 如果目标值小于中间元素，说明目标值可能在左半部分
            # 递归调用二分查找，搜索范围缩小为 [First, Middle-1]
            if ToFind < IntegerArray[Middle]:
                return BinarySearch(IntegerArray, First, Middle - 1, ToFind)
            # 否则目标值大于中间元素，说明目标值可能在右半部分
            # 递归调用二分查找，搜索范围缩小为 [Middle-1, Last]
            # 注意：这里用了 Middle-1 而非 Middle+1，可能导致搜索范围重叠或漏掉元素
            else:
                return BinarySearch(IntegerArray, Middle - 1, Last, ToFind)

# 异常处理：如果二分查找过程中发生错误（如索引越界），则打印"Not Found"
try:
    # 在数组 NumberArray 的索引 0 到 6 范围内查找值 644
    print(BinarySearch(NumberArray, 0, 6, 644))
except:
    # 如果发生异常，捕获并输出提示信息
    print("Not Found")