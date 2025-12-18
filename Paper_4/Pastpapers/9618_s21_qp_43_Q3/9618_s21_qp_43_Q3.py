#Created by 4AMAlan
class TreasureChest:
	def __init__(self, q, a, p):
		self.__question = q      #Private attribute, type: STRING
		self.__answer = a        #Private attribute, type: INTEGER
		self.__points = p        #Private attribute, type: INTEGER

	def getQuestion(self):
		return self.__question

	def checkAnswer(self, ua):
		if ua == int(self.__answer):
			return True
		else:
			return False
	
	def getPoints(self, noa):
		if noa == 1:
			return self.__points
		elif noa == 2:
			return self.__points // 2
		elif noa == 3 or noa == 4:
			return self.__points // 4
		else:
			return 0

arrayTreasure = []

def readData():
	global arrayTreasure
	
	try:
		f = open("TreasureChestData.txt", "r")
	except:
		print("No such file or directory")

	while True:
		QuestionLine = f.readline().strip()
		AnswerLine = f.readline().strip()
		Points = f.readline().strip()
		Question = TreasureChest(QuestionLine, AnswerLine, Points)
		arrayTreasure.append(Question)
		if not QuestionLine or not AnswerLine or not Points:
			break
	
	f.close()

readData()
QuestionNumber = int(input("Please enter question number:"))

if 1 <= QuestionNumber <= 5:
	result = False
	NumberOfAttempts = 0
	
	while result == False:
		print(arrayTreasure[QuestionNumber - 1].getQuestion())
		UserAnswer = int(input("Please enter answer:"))
		result = arrayTreasure[QuestionNumber - 1].checkAnswer(UserAnswer)
		NumberOfAttempts += 1
	print(arrayTreasure[QuestionNumber - 1].getPoints(NumberOfAttempts))

else:
	print("Invalid question number")
