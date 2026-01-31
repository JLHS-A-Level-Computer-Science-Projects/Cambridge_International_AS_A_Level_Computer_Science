# 初始化一个全局列表，用于模拟队列，大小为20个元素
QueueData = ["" for i in range(20)]   #global list
# 全局变量，指向队列头部元素的索引
QueueHead = -1                        #global variable
# 全局变量，指向队列尾部元素的索引
QueueTail = -1                        #global variable

# 将数据项添加到队列尾部的函数
def Enqueue(DataToBeInserted):
	global QueueData, QueueHead, QueueTail
	# 检查队列是否已满 (当尾部指针到达数组最后一个位置时)
	if QueueTail == 19:
		return False
	# 如果队列为空 (Head为-1表示队列初始或为空)
	elif QueueHead == -1:
		# 将队列头部指针设置为0
		QueueHead = 0
	# 队列尾部指针向后移动一位
	QueueTail += 1
	# 在队列尾部插入新数据
	QueueData[QueueTail] = DataToBeInserted
	# 返回True表示插入成功
	return True

# 从队列头部移除并返回一个数据项的函数
def Dequeue():
	global QueueData, QueueHead, QueueTail
	# 检查队列是否为空 (Head小于0表示空，Head大于Tail也表示空，Head超过数组范围也无效)
	if QueueHead < 0 or QueueHead > 20 or QueueHead > QueueTail:
		# 队列为空则返回False
		return False
	else:
		# 队列头部指针向后移动一位，逻辑上移除头部元素
		QueueHead += 1
		# 返回被移除的元素 (即原头部元素)
		return QueueData[QueueHead - 1]

# 获取用户输入的字符串，验证其有效性，并将有效数据存入队列的子程序
def StoreItems():
	global QueueData, QueueHead, QueueTail
	# 用于累计计算校验位的总和
	Total = 0
	# 计数器，记录无效输入的数量
	Count = 0
	# 循环获取10次输入
	for i in range(10):
		# 提示用户输入一个7字符的字符串
		String = input("Please input a 7-character string:")
		# 根据题目描述的算法计算校验位：
		# (位置0 * 1) + (位置1 * 3) + (位置2 * 1) + (位置3 * 3) + (位置4 * 1) + (位置5 * 3)
		Total = int(String[0]) + (3 * int(String[1])) + int(String[2]) + (3 * int(String[3])) + int(String[4]) + (3 * int(String[5]))
		# 将总和除以10并向下取整，得到校验数字
		Total = Total // 10
		# 验证输入的字符串是否有效：
		# 1. 如果计算出的校验数字是10，且字符串第7位（索引6）是'X'
		# 2. 或者计算出的校验数字等于字符串第7位（索引6）的实际数字
		if (Total == 10 and String[6] == "X") or Total == int(String[6]):
			# 输入有效，调用Enqueue函数将前6位数字（去掉校验位）加入队列
			Result = Enqueue(String[0:6])
			# 检查入队操作是否成功
			if Result == True:
				print("Inserted item")
			else:
				print("Queue full")
		else:
			# 输入无效，计数器加一
			Count += 1

	# 输出本次操作中发现的无效输入总数
	print(Count, "invalid items found")

# 调用StoreItems子程序开始执行主要功能
StoreItems()
# 调用Dequeue函数尝试从队列中取出一个数据项
Value = Dequeue()
# 检查Dequeue的返回值，如果为False说明队列为空
if Value == False:
	print("No data items")
else:
	# 否则，输出取出的数据项及其说明
	print("Item code", Value)
