Jobs = [[0 for i in range(2)] for i in range(100)]
NumberOfJobs = 0

def Initialise():
	global Jobs, NumberOfJobs
	for i in range(100):
		for j in range(2):
			Jobs[i][j] = -1
	NumberOfJobs = 0

def AddJob(JobNumber,Priority):
	global Jobs, NumberOfJobs
	AddFlag = False
	for i in range(100):
		if Jobs[i][0] == -1:
			Jobs[i][0] = JobNumber
			Jobs[i][1] = Priority
			AddFlag = True
			NumberOfJobs += 1
			break
	if AddFlag == True:
		print("Added")
	else:
		print("Not added")


def InsertionSort():
	global Jobs, NumberOfJobs
	for i in range(NumberOfJobs):
		CurrentItem1 = Jobs[i][0]
		CurrentItem2 = Jobs[i][1]
		while i > 0 and Jobs[i - 1][1] > CurrentItem2:
			Jobs[i][0] = Jobs[i - 1][0]
			Jobs[i][1] = Jobs[i - 1][1]
			i -= 1
		Jobs[i][0] = CurrentItem1
		Jobs[i][1] = CurrentItem2

def PrintArray():
	global Jobs, NumberOfJobs
	for i in range(100):
		if Jobs[i][0] != -1:
			print(Jobs[i][0], "priority", Jobs[i][1])

Initialise()
AddJob(12,10)
AddJob(526,9)
AddJob(33,8)
AddJob(12,9)
AddJob(78,1)
InsertionSort()
PrintArray()