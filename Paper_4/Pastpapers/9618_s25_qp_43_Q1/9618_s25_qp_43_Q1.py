#Created by 4AMAlan

Queue = [-1 for i in range(50)]
HeadPointer = -1
TailPointer = -1
NumberOfElements = 0

def Enqueue(NewInt) -> bool:
	global Queue, HeadPointer, TailPointer, NumberOfElements
	if NumberOfElements == 50:
		return False	
	if HeadPointer == -1:
		Queue[0] = NewInt
		HeadPointer = 0
		TailPointer = 0
		NumberOfElements += 1
		return True
	else:
		Queue[TailPointer + 1] = NewInt
		TailPointer += 1
		return True

def Dequeue() -> int:
	global Queue, HeadPointer, TailPointer, NumberOfElements
	if NumberOfElements == 0:
		return -1
	else:
		HeadPointer += 1
		return Queue[HeadPointer - 1]

def CreateQueue():
	global Queue, HeadPointer, TailPointer, NumberOfElements
	try:
		f = open("QueueData.txt", "r")
	except:
		print("No such file or directory.")
	while True:
		try:
			Content = f.readline().strip()
		except:
			print("Reading Error")
		if Content == "":
			break		
		Enqueue(int(Content))
	if NumberOfElements == 50:
		print("The queue is full.")
	f.close()

CreateQueue()
Sum = 0
while True:
	Result = Dequeue()
	if Result == -1:
		break
	Sum += Result
print(Sum)