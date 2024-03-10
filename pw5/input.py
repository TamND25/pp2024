import curses
from domains.student import Student
from domains.course import Course
from domains.student_list import StudentsList
from domains.course_list import CoursesList

number_students = 0
number_courses = 0

student_list = StudentsList()
course_list = CoursesList() 

def set_number_of_student(stdscr):
    stdscr.clear()
    global number_students
    stdscr.addstr("\nNumber of students: ")
    stdscr.refresh()
    curses.echo()
    number_students = int(stdscr.getstr().decode())
    curses.noecho()
    stdscr.clear()
    return number_students

def set_number_of_courses(stdscr):
    stdscr.clear()
    global number_courses
    stdscr.addstr("\nNumber of courses: ")
    stdscr.refresh()
    curses.echo()
    number_courses = int(stdscr.getstr().decode())
    curses.noecho()
    stdscr.clear()
    return number_courses

def input_students_information(stdscr, student_list, filename):
    stdscr.clear()
    while len(student_list._StudentsList__students) < number_students:
        stdscr.addstr(f"Student {len(student_list._StudentsList__students) + 1}: ")
        stdscr.addstr("\nStudent ID: ")
        stdscr.refresh()
        curses.echo()
        s_id = stdscr.getstr().decode()
        curses.noecho()

        stdscr.addstr("Student Name: ")
        stdscr.refresh()
        curses.echo()
        s_name = stdscr.getstr().decode()
        curses.noecho()

        stdscr.addstr("Student's Date of Birth: ")
        stdscr.refresh()
        curses.echo()
        s_dob = stdscr.getstr().decode()
        curses.noecho()

        standard_student = Student(s_id, s_name, s_dob)
        student_list.add_student(standard_student)

        with open(filename, 'w') as file_s:
            for student in student_list._StudentsList__students:
                file_s.write(f"ID: {student.show_id()}, Student Name: {student.show_name()}, DoB: {student.show_dob()} \n")
        stdscr.addstr("Input and Write successfully! Press any key to close!")
        stdscr.getch()
        stdscr.clear()

def input_courses_information(stdscr, course_list, filename):
    stdscr.clear()
    while len(course_list._CoursesList__courses) < number_courses:
        while True:
            stdscr.addstr(f"Course {len(course_list._CoursesList__courses)+1}: ")
            stdscr.addstr("\nCourse ID: ")
            stdscr.refresh()
            curses.echo()
            c_id = stdscr.getstr().decode()
            curses.noecho()

            stdscr.addstr("Course Name: ")
            stdscr.refresh()
            curses.echo()
            c_name = stdscr.getstr().decode()
            curses.noecho()

            stdscr.addstr("Course Credit: ")
            stdscr.refresh()
            curses.echo()
            c_credit_str = stdscr.getstr().decode()
            curses.noecho()

            try:
                c_credit = int(c_credit_str)
                break
            except ValueError:
                stdscr.clear()
                stdscr.addstr("Please enter a valid integer for Course Credit!\n")

        standard_course = Course(c_id, c_name, c_credit)
        course_list.add_course(standard_course)

        with open(filename, 'w') as file_c:
            for course in course_list._CoursesList__courses:
                file_c.write(f"ID: {course.show_id()}, Course Name: {course.show_name()}, Credit: {course.show_credit()} \n")

        stdscr.addstr("Input and Write successfully! Press any key to close!")
        stdscr.getch()
        stdscr.clear()

def add_mark(stdscr, student_list, course_list, filename):
    stdscr.clear()
    for student in student_list._StudentsList__students:
        for course in course_list._CoursesList__courses:
            stdscr.addstr(f"Enter the mark of {student.show_name()} for {course.show_name()}: ")
            stdscr.refresh()
            curses.echo()
            mark = float(stdscr.getstr().decode())
            curses.noecho()
            student.add_mark(course, mark)
            stdscr.clear()
    
    with open(filename, 'w') as file_m:
        for student in student_list._StudentsList__students:
            file_m.write(f"\nStudent: {student.show_name()}\n")
            marks = student.show_mark()
            for course, mark in marks.items():
                file_m.write(f"{course.show_name()}: {mark}\n")    
    
    stdscr.addstr("Add and Write successfully! Press any key to close!")
    stdscr.getch()
    stdscr.clear()

    

