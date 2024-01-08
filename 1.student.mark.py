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

# Show courses
def show_courses():
    for i in range(numberOfCourses):
        print(coursesList[i])

# Show students
def show_students():
    for i in range(numberOfStudents):
        print(studentsList[i])

# Show marks
def show_marks():
    for i in range(numberOfStudents):
        print(studentMarkList[i])

def main():

    while(True):
        print("""
    0. Exit
    1. Input the total number of students.              
    2. Input student information.
    3. Input the total number of courses.
    4. Input course information.
    5. Input mark for student for a course.
    6. Show the courses.
    7. Show the students.
    8. Show the student mark of a course.
    """)
        option = input("Your choice: ")
        if option == '0':
            break

        elif option == '1':
            input_number_of_students()

        elif option == '2':
            input_student_information()

        elif option == '3':
            input_number_of_courses()

        elif option == '4':
            input_course_information()

        elif option == '5':
            input_mark()

        elif option == '6':
            show_courses()

        elif option == '7':
            show_students()

        elif option == '8':
            show_marks()

        else:
            print("Invalid input. Please try again!")


if __name__ == "__main__":
    main()