#Created by 4AMAlan
class Lesson:
	def __init__(self, t, d, r):
		# ��ʼ��Lesson�������ÿ�ʱ�ı��⡢ʱ�����Ƿ���Ҫʵ����
		self.__LessonTitle = t        #Private attribute, type: STRING
		self.__DurationMinutes = d    #Private attribute, type: INTEGER
		self.__RequiresLab = r        #Private attribute, type: Boolean

	def OutputLessonDetails(self):
		# �����ǰ��ʱ����ϸ��Ϣ
		print("Lesson Details")
		print("Lesson Title:", self.__LessonTitle)
		print("Duration Minutes:", self.__DurationMinutes)
		print("Requires Lab:", self.__RequiresLab)
		print("End Lesson Details")
		return ""

# ����Assessment�࣬���ڱ�ʾ�γ��е�����
class Assessment:
	def __init__(self, at, m):
		# ��ʼ��Assessment�������������ı����������
		self.__AssessmentTitle = at   #Private attribute, type: STRING
		self.__MaxMarks = m           #Private attribute, type: INTEGER

	def OutputAssessmentDetails(self):
		# �����ǰ��������ϸ��Ϣ
		print("Assessment Details")
		print("Assessment Title:", self.__AssessmentTitle)
		print("MaxMarks:", self.__MaxMarks)
		print("End Assessment Details")
		return ""

# ����Course�࣬���ڱ�ʾ�����Ŀγ�
class Course:
	def __init__(self, t, m):
		# ��ʼ��Course�������ÿγ̱�������ѧ����������ʼ�������������
		self.__CourseTitle = t
		self.__MaxStudents = m
		self.__NumberOfLessons = 0  # ��¼�γ��п�ʱ������
		self.__CourseLesson = []    # �洢�γ������п�ʱ���б�
		self.__CourseAssessment = Assessment  # �洢�γ���������ע�⣺����Ӧ����None��ʵ�ʵ�Assessment����

	def AddLesson(self, t, d, r):
		# ��γ�������һ���µĿ�ʱ
		self.__NumberOfLessons += 1  # ���ӿ�ʱ����
		self.__CourseLesson.append(Lesson(t, d, r))  # ����Lesson�������ӵ��б���

	def AddAssessment(self, t, m):
		# Ϊ�γ���������
		self.__CourseAssessment = Assessment(t, m)  # ����Assessment���󲢸�ֵ���γ���������

	def OutputCourseDetails(self):
		# ��������γ̵���ϸ��Ϣ�������γ̻�����Ϣ�����п�ʱ��Ϣ��������Ϣ
		print("Course Details")
		print("Course Title:", self.__CourseTitle)
		print("Max Students:", self.__MaxStudents)
		print()
		# ������������п�ʱ����ϸ��Ϣ
		for i in range(self.__NumberOfLessons):
			print(self.__CourseLesson[i].OutputLessonDetails())
		# ����γ���������ϸ��Ϣ
		print(self.__CourseAssessment.OutputAssessmentDetails())

# ��������������ʾ���ʹ��
def Main():
	# ����һ����Ϊ"Computing"�Ŀγ̶������ѧ����Ϊ10
	MyCourse = Course("Computing", 10)
	
	# Ϊ�γ���������������Ϊ"Programming"��������Ϊ100
	MyCourse.AddAssessment("Programming", 100)
	
	# Ϊ�γ�����������ʱ
	MyCourse.AddLesson("Problem Solving", 60, False)  # �������Σ�60���ӣ�����Ҫʵ����
	MyCourse.AddLesson("Programming", 120, True)     # ��̿Σ�120���ӣ���Ҫʵ����
	MyCourse.AddLesson("Theory", 60, False)          # ���ۿΣ�60���ӣ�����Ҫʵ����

	# ��������γ̵���ϸ��Ϣ
	MyCourse.OutputCourseDetails()

# ����������ִ�г���
Main()
