NumberArray = [100, 85, 644, 22, 15, 8, 1]

LastTerm = 0        #type: INTEGER
CheckItem = 0       #type: INTEGER
LoopAgain = True    #type: BOOLEAN

def RecursiveInsertion(IntegerArray, NumberElements):         #Returns ARRAY OF INTEGER
	'''
	IntegerArray: type: ARRAY OF INTEGER
	NumberElements: type: INTEGER
	'''
	if NumberElements <= 1:
		return IntegerArray
	else:
		RecursiveInsertion(IntegerArray, NumberElements - 1)
		LastTerm = IntegerArray[NumberElements - 1]
		CheckItem = NumberElements - 2
	
	LoopAgain = True
	if CheckItem < 0:
		LoopAgain = False
	else:
		if IntegerArray[CheckItem] <= LastTerm:
			LoopAgain = False

	while LoopAgain:
		IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
		CheckItem -= 1
		if CheckItem < 0:
			LoopAgain = False
		else:
			if IntegerArray[CheckItem] <= LastTerm:
				LoopAgain = False

	IntegerArray[CheckItem + 1] = LastTerm
	return IntegerArray

print("Recursive")
print(RecursiveInsertion(NumberArray, len(NumberArray)))

def IterativeInsetion(ListToBeSorted):
	for i in range(0, len(ListToBeSorted)):
		ItemToBeSorted = ListToBeSorted[i]
		CurrentItem = i
		while ItemToBeSorted < ListToBeSorted[CurrentItem] and CurrentItem > -1:
			ListToBeSorted[CurrentItem] = ListToBeSorted[CurrentItem + 1]
			CurrentItem -= 1
		ListToBeSorted[CurrentItem] = ItemToBeSorted
		CurrentItem -= 1
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
		if First > Last:
			return -1
		else:
			if ToFind < IntegerArray[Middle]:
				return BinarySearch(IntegerArray, First, Middle - 1, ToFind)
			else:
				return BinarySearch(IntegerArray, Middle + 1, Last, ToFind)


try:
	print(BinarySearch(NumberArray, 0, 6, 644))
except:
	print("Not Found")