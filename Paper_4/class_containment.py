#Created by 4AMAlan
class Lesson:
	def __init__(self, t, d, r):
		# Initialize Lesson with title, duration in minutes, and whether lab is required
		self.__LessonTitle = t        #Private attribute, type: STRING
		self.__DurationMinutes = d    #Private attribute, type: INTEGER
		self.__RequiresLab = r        #Private attribute, type: Boolean

	def OutputLessonDetails(self):
		# Output the current lesson's detailed information
		print("Lesson Details")
		print("Lesson Title:", self.__LessonTitle)
		print("Duration Minutes:", self.__DurationMinutes)
		print("Requires Lab:", self.__RequiresLab)
		print("End Lesson Details")
		return ""

# Create Assessment class, used to represent assessments in the course
class Assessment:
	def __init__(self, at, m):
		# Initialize Assessment with assessment title and maximum marks
		self.__AssessmentTitle = at   #Private attribute, type: STRING
		self.__MaxMarks = m           #Private attribute, type: INTEGER

	def OutputAssessmentDetails(self):
		# Output the current assessment's detailed information
		print("Assessment Details")
		print("Assessment Title:", self.__AssessmentTitle)
		print("MaxMarks:", self.__MaxMarks)
		print("End Assessment Details")
		return ""

# Create Course class, used to represent a complete course
class Course:
	def __init__(self, t, m):
		# Initialize Course with course title, maximum students, initialize lesson count and assessment
		self.__CourseTitle = t
		self.__MaxStudents = m
		self.__NumberOfLessons = 0  # Record the number of lessons in the course
		self.__CourseLesson = []    # Store a list of lessons in the course
		self.__CourseAssessment = Assessment  # Store assessment Note: should be None initially, not Assessment instance

	def AddLesson(self, t, d, r):
		# Add a new lesson to the course
		self.__NumberOfLessons += 1  # Increment lesson count
		self.__CourseLesson.append(Lesson(t, d, r))  # Create Lesson object and add to list

	def AddAssessment(self, t, m):
		# Add assessment to the course
		self.__CourseAssessment = Assessment(t, m)  # Create Assessment object and assign to course assessment

	def OutputCourseDetails(self):
		# Output detailed course information including course info, lesson info, and assessment info
		print("Course Details")
		print("Course Title:", self.__CourseTitle)
		print("Max Students:", self.__MaxStudents)
		print()
		# Output detailed information for all lessons in the course
		for i in range(self.__NumberOfLessons):
			print(self.__CourseLesson[i].OutputLessonDetails())
		# Output assessment detailed information
		print(self.__CourseAssessment.OutputAssessmentDetails())

# Main function to demonstrate usage
def Main():
	# Create a course named "Computing" with maximum students of 10
	MyCourse = Course("Computing", 10)
	
	# Add assessment to the course named "Programming" with maximum marks of 100
	MyCourse.AddAssessment("Programming", 100)
	
	# Add lessons to the course
	MyCourse.AddLesson("Problem Solving", 60, False)  # Problem Solving: 60 minutes, does not require lab
	MyCourse.AddLesson("Programming", 120, True)     # Programming: 120 minutes, requires lab
	MyCourse.AddLesson("Theory", 60, False)          # Theory: 60 minutes, does not require lab

	# Output detailed course information
	MyCourse.OutputCourseDetails()

# Run the main program
Main()
