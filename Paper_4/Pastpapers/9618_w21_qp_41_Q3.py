NULLPOINTER = -1

ArrayNodes = [[0 for i in range(3)] for i in range(20)] #inner is each node, outer is tree
RootPointer = NULLPOINTER
FreeNode = 0

def AddNode(arrayNodes, rootPointer, freeNode):
	global ArrayNodes, RootPointer, FreeNode
	NodeData = int(input("Please input data:"))
	if FreeNode <= 19:
		ArrayNodes[FreeNode][0] = -1
		ArrayNodes[FreeNode][1] = NodeData
		ArrayNodes[FreeNode][2] = -1
		if RootPointer == NULLPOINTER:
			RootPointer = 0
		else:
			Placed = False
			CurrentNode = RootPointer
			while Placed == False:
				if NodeData < ArrayNodes[CurrentNode][1]:
					if ArrayNodes[CurrentNode][0] == -1:
						ArrayNodes[CurrentNode][0] = FreeNode
						Placed = True
					else:
						CurrentNode = ArrayNodes[CurrentNode][0]
				else:
					if ArrayNodes[CurrentNode][2] == -1:
						ArrayNodes[CurrentNode][2] = FreeNode
						Placed = True
					else:
						CurrentNode = ArrayNodes[CurrentNode][2]
		FreeNode = FreeNode + 1
	else:
		print("Tree is full")

def PrintAll():
	for i in range(20):
		print(ArrayNodes[i][0], "  ", ArrayNodes[i][1], "  ", ArrayNodes[i][2])

def InOrder(CurrentNode):
	global ArrayNodes
	if CurrentNode != NULLPOINTER:
		InOrder(ArrayNodes[CurrentNode][0])
		print(ArrayNodes[CurrentNode][1], end = " ")
		InOrder(ArrayNodes[CurrentNode][2])

for i in range(10):
	AddNode(ArrayNodes, RootPointer, FreeNode)

PrintAll()
print()
InOrder(RootPointer)