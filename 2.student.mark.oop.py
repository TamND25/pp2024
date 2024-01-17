numberOfStudents = 0
numberOfCourses = 0

def set_number_of_student():
    global numberOfStudents
    numberOfStudents = int(input("Number of students: "))
    return numberOfStudents

def input_number_of_courses():
    global numberOfCourses
    numberOfCourses = int(input("Number of courses: "))
    return numberOfCourses

class Student:
    def __init__(self, name, id, dob):
        self.__name = name
        self.__id = id
        self.__dob = dob
    
    def showname(self):
        return self.__name
    
    def showid(self):
        return self.__id
    
    def showdob(self):
        return self.__dob
        
class Course:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id

    def showname(self):
        return self.__name
    
    def showid(self):
        return self.__id
    
class StudentsList:
    def __init__(self):
        self.__students = []
    
    def add_student(self, student):
        for _ in range(numberOfStudents):
            if isinstance(student, Student):
                self.__students.append(student)
            else:
                print("Invalid student")
    
    def showStudentsList(self):
        for student in self.__students:
            print(f"Name: {student.showname()}, ID: {student.showid()}, DOB: {student.showdob()}")

class CoursesList:
    def __init__(self):
        self.__courses = []
    
    def add_student(self, course):
        for _ in range(numberOfCourses):
            if isinstance(course, Course):
                self.__courses.append(course)
            else:
                print("Invalid course")
    
    def showStudentsList(self):
        for course in self.__courses:
            print(f"Name: {course.showname()}, ID: {course.showid()}")