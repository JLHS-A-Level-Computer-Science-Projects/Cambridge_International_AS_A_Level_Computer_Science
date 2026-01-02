# 定义Lesson类，用于表示课程中的单个课时
class Lesson:
	def __init__(self, t, d, r):
		# 初始化Lesson对象，设置课时的标题、时长和是否需要实验室
		self.__LessonTitle = t        #Private attribute, type: STRING
		self.__DurationMinutes = d    #Private attribute, type: INTEGER
		self.__RequiresLab = r        #Private attribute, type: Boolean

	def OutputLessonDetails(self):
		# 输出当前课时的详细信息
		print("Lesson Details")
		print("Lesson Title:", self.__LessonTitle)
		print("Duration Minutes:", self.__DurationMinutes)
		print("Requires Lab:", self.__RequiresLab)
		print("End Lesson Details")
		return ""

# 定义Assessment类，用于表示课程中的评估
class Assessment:
	def __init__(self, at, m):
		# 初始化Assessment对象，设置评估的标题和最大分数
		self.__AssessmentTitle = at   #Private attribute, type: STRING
		self.__MaxMarks = m           #Private attribute, type: INTEGER

	def OutputAssessmentDetails(self):
		# 输出当前评估的详细信息
		print("Assessment Details")
		print("Assessment Title:", self.__AssessmentTitle)
		print("MaxMarks:", self.__MaxMarks)
		print("End Assessment Details")
		return ""

# 定义Course类，用于表示完整的课程
class Course:
	def __init__(self, t, m):
		# 初始化Course对象，设置课程标题和最大学生数，并初始化其他相关属性
		self.__CourseTitle = t
		self.__MaxStudents = m
		self.__NumberOfLessons = 0  # 记录课程中课时的数量
		self.__CourseLesson = []    # 存储课程中所有课时的列表
		self.__CourseAssessment = Assessment  # 存储课程评估对象（注意：这里应该是None或实际的Assessment对象）

	def AddLesson(self, t, d, r):
		# 向课程中添加一个新的课时
		self.__NumberOfLessons += 1  # 增加课时计数
		self.__CourseLesson.append(Lesson(t, d, r))  # 创建Lesson对象并添加到列表中

	def AddAssessment(self, t, m):
		# 为课程添加评估
		self.__CourseAssessment = Assessment(t, m)  # 创建Assessment对象并赋值给课程评估属性

	def OutputCourseDetails(self):
		# 输出整个课程的详细信息，包括课程基本信息、所有课时信息和评估信息
		print("Course Details")
		print("Course Title:", self.__CourseTitle)
		print("Max Students:", self.__MaxStudents)
		print()
		# 遍历并输出所有课时的详细信息
		for i in range(self.__NumberOfLessons):
			print(self.__CourseLesson[i].OutputLessonDetails())
		# 输出课程评估的详细信息
		print(self.__CourseAssessment.OutputAssessmentDetails())

# 定义主函数，演示类的使用
def Main():
	# 创建一个名为"Computing"的课程对象，最大学生数为10
	MyCourse = Course("Computing", 10)
	
	# 为课程添加评估，标题为"Programming"，最大分数为100
	MyCourse.AddAssessment("Programming", 100)
	
	# 为课程添加三个课时
	MyCourse.AddLesson("Problem Solving", 60, False)  # 问题解决课，60分钟，不需要实验室
	MyCourse.AddLesson("Programming", 120, True)     # 编程课，120分钟，需要实验室
	MyCourse.AddLesson("Theory", 60, False)          # 理论课，60分钟，不需要实验室

	# 输出整个课程的详细信息
	MyCourse.OutputCourseDetails()

# 调用主函数执行程序
Main()
