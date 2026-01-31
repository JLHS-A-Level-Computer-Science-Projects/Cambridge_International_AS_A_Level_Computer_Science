class Tree:
	def __init__(self, n, g, h, w, e):
		self.__TreeName = n              #Private attribute, type: STRING
		self.__HeightGrowth = g          #Private attribute, type: INTEGER
		self.__MaxHeight = h             #Private attribute, type: INTEGER
		self.__MaxWidth = w              #Private attribute, type: INTEGER
		self.__Evergreen = e             #Private attribute, type: STRING

	def GetTreeName(self):
		return self.__TreeName
	
	def GetGrowth(self):
		return self.__HeightGrowth
	
	def GetMaxHeight(self):
		return self.__MaxHeight
	
	def GetMaxWidth(self):
		return self.__MaxWidth
	
	def GetEvergreen(self):
		return self.__Evergreen
	
def ReadData():
	TreeArray = []                       #type: Tree

	try:
		f = open("Trees.txt", "r")
	except:
		print("No such file or directory.")
	
	for i in range(9):
		TreeInfo = f.readline().strip().split(",")
		TreeArray.append(Tree(TreeInfo[0], int(TreeInfo[1]), int(TreeInfo[2]), int(TreeInfo[3]), TreeInfo[4]))
	
	f.close()
	
	return TreeArray

def PrintTrees(TreeObj):
	if TreeObj.GetEvergreen() == "Yes":
		print(TreeObj.GetTreeName(), "has a maximum height", TreeObj.GetMaxHeight(), "a maximum width", TreeObj.GetMaxWidth(), "and grows", TreeObj.GetGrowth(), "cm a year. It does not lose leaves.")
	else:
		print(TreeObj.GetTreeName(), "has a maximum height", TreeObj.GetMaxHeight(), "a maximum width", TreeObj.GetMaxWidth(), "and grows", TreeObj.GetGrowth(), "cm a year. It loses its leaves each year.")

Trees = ReadData()
PrintTrees(Trees[0])

def ChooseTree(TreeList):
	HeightRequirement = int(input("Please input your height requirement of the tree:"))
	WidthRequirement = int(input("Please input your width requirement of the tree:"))
	WhetherEvergreen = input("Is the tree evergreen? (Yes/No):")
	
	TreeMeetRequirements = []

	for i in range(0, len(TreeList)):
		if TreeList[i].GetMaxHeight() <= HeightRequirement and TreeList[i].GetMaxWidth() <= WidthRequirement and TreeList[i].GetEvergreen() == WhetherEvergreen:
			TreeMeetRequirements.append(TreeList[i])
	
	for i in range(0, len(TreeMeetRequirements)):
		PrintTrees(TreeMeetRequirements[i])

	NameWantToBuy = input("Please input the tree name you want to buy:")
	HeightWhenBought = int(input("Please input the height of the tree when you buy:"))
	for i in range(0, len(TreeMeetRequirements)):
		if TreeMeetRequirements[i].GetTreeName().strip() == NameWantToBuy:
			print("It takes", ((TreeMeetRequirements[i].GetMaxHeight() - HeightWhenBought) // TreeMeetRequirements[i].GetGrowth()), "years to grow to the maxmum height.")

ChooseTree(Trees)