numberOfStudents = 0
studentsList = []
numberOfCourses = 0
coursesList = []
studenMark ={}
studentMarkList = []

# Input the total number of students
def input_number_of_students():
    global numberOfStudents
    numberOfStudents = int(input("Number of students: "))
    return numberOfStudents

# Input student infomation
def input_student_information():
    for _ in range(numberOfStudents):
        s_id = input("Enter student ID: ")
        s_name = input("Enter student name: ")
        s_dob = input("Enter student date of birth: ")
        studentsList.append({"ID": s_id, "Name": s_name, "Date of Birth": s_dob})
    return studentsList

# Input the total number of courses
def input_number_of_courses():
    global numberOfCourses
    numberOfCourses = int(input("Number of courses: "))
    return numberOfCourses

# Input course information
def input_course_information():
    for _ in range(numberOfCourses):
        c_id = input("Enter course ID: ")
        c_name = input("Enter course name: ")
        coursesList.append({"ID": c_id, "Name": c_name})
    return coursesList

# Input mark
def input_mark():
    course_name = input("Enter course name: ")
    for student in studentsList:
        student_mark = {'Name': student['Name']}
        for course in coursesList:
            if course_name == course['Name']:
                marks = float(input(f"Enter marks for {student['Name']} in {course_name}: "))
                student_mark.setdefault(course_name)
                student_mark[course_name] = marks
                studentMarkList.append(student_mark)