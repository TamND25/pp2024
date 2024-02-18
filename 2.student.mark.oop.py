number_students = 0
number_courses = 0

class Student:
    def __init__(self, name, id, dob):
        self.__name = name
        self.__id = id
        self.__dob = dob
        self.__marks = {}
    
    def showname(self):
        return self.__name
    
    def showid(self):
        return self.__id
    
    def showdob(self):
        return self.__dob
    
    def add_mark(self, course, mark):
        self.__marks[course] = mark

    def show_mark(self):
        return self.__marks
        
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
    
    def show_students_list(self):
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
    
    def show_courses_list(self):
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

def input_students_information():
    for _ in range(number_students):
        s_id = input("Student ID: ")
        s_name = input("Student Name: ")
        s_dob = input("Student's Date of Birth: ")
        print("\n")
        standard_student = Student(s_id, s_name, s_dob)
        student_list.add_student(standard_student)

def input_courses_information():
    for _ in range(number_courses):
        c_id = input("Course ID: ")
        c_name = input("Course Name: ")
        print("\n")
        standard_course = Course(c_id, c_name)
        course_list.add_course(standard_course)

def add_mark():
        for student in student_list._StudentsList__students:
            for course in course_list._CoursesList__courses:
                mark = float(input(f"Enter the mark of {student.show_name()} for {course.show_name()}: "))
                student.add_mark(course, mark)

def show_mark():
    for student in student_list._StudentsList__students:
        print(f"\nStudent: {student.show_name}")
        marks = student.show_mark()
        for course_name, mark in marks.items():
            print(f"{course_name}: {mark}")

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
            set_number_of_student()

        elif option == '2':
            set_number_of_courses()

        elif option == '3':
            input_students_information()

        elif option == '4':
            input_students_information()

        elif option == '5':
            add_mark()

        elif option == '6':
            student_list.show_students_list()

        elif option == '7':
            course_list.show_courses_list()

        elif option == '8':
            show_mark()

        else:
            print("Invalid input. Please try again!")

if __name__ == "__main__":
    main()