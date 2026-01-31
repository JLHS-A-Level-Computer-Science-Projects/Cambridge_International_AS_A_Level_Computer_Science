QueueData = ["" for i in range(20)]   #global list
QueueHead = -1                        #global variable
QueueTail = -1                        #global variable

def Enqueue(DataToBeInserted):
	global QueueData, QueueHead, QueueTail
	if QueueTail == 19:
		return False
	elif QueueHead == -1:
		QueueHead = 0
	QueueTail += 1
	QueueData[QueueTail] = DataToBeInserted
	return True


def Dequeue():
	global QueueData, QueueHead, QueueTail
	if QueueHead < 0 or QueueHead > 20 or QueueHead > QueueTail:
		return False
	else:
		QueueHead += 1
		return QueueData[QueueHead - 1]

def StoreItems():
	global QueueData, QueueHead, QueueTail
	Total = 0
	Count = 0
	
	for i in range(10):
		String = input("Please input a 7-character string:")
		Total = int(String[0]) + (3 * int(String[1])) + int(String[2]) + (3 * int(String[3])) + int(String[4]) + (3 * int(String[5]))
		Total = Total // 10
		if (Total == 10 and String[6] == "X") or Total == int(String[6]):
			Result = Enqueue(String[0:6])
			if Result == True:
				print("Inserted item")
			else:
				print("Queue full")
		else:
			Count += 1
	
	print(Count, "invalid items found")

StoreItems()
Value = Dequeue()
if Value == False:
	print("No data items")
else:
	print("Item code", Value)