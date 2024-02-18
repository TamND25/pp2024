number_students = 0
number_courses = 0

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
        for _ in range(number_students):
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
        for _ in range(number_courses):
            if isinstance(course, Course):
                self.__courses.append(course)
            else:
                print("Invalid course")
    
    def showStudentsList(self):
        for course in self.__courses:
            print(f"Name: {course.showname()}, ID: {course.showid()}")

student_list = StudentsList()
course_list = CoursesList()

def set_number_of_student():
    global number_students
    number_students = int(input("Number of students: "))
    return number_students

def set_number_of_courses():
    global number_courses
    number_courses = int(input("Number of courses: "))
    return number_courses

def main():

    while(True):
        print("""
    0. Exit
    1. Input the total number of students.    
    2. Input the total number of courses.          
    3. Input student information. 
    4. Input course information.
    5. Input mark for student for a course.
    6. Show the students.
    7. Show the courses.
    8. Show the students' mark.
    """)
        option = input("Your choice: ")
        if option == '0':
            break

        elif option == '1':
            

        elif option == '2':
            

        elif option == '3':
            

        elif option == '4':
            

        elif option == '5':
            

        elif option == '6':
            

        elif option == '7':
            

        elif option == '8':
            

        else:
            print("Invalid input. Please try again!")