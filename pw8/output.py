import math
import numpy
from domains.student_list import StudentsList
from domains.course_list import CoursesList
student_list = StudentsList()
course_list = CoursesList()

def show_mark(stdscr, student_list):
    stdscr.clear()
    for student in student_list._StudentsList__students:
        stdscr.addstr(f"\nStudent: {student.show_name()}\n")
        marks = student.show_mark()
        for course, mark in marks.items():
            stdscr.addstr(f"{course.show_name()}: {mark}\n")
        stdscr.addstr("Press any key to show the next student!")
        stdscr.getch()   
        stdscr.clear()
    stdscr.addstr("Press any key to close!")
    stdscr.getch()
    stdscr.clear()

def round_down_mark(stdscr, student_list):
    stdscr.clear()
    for student in student_list._StudentsList__students:
        stdscr.addstr(f"Student: {student.show_name()}\n")
        marks = student.show_mark()
        for course, mark in marks.items():
            stdscr.addstr(f"{course.show_name()}: {math.floor(mark)}\n")
        stdscr.addstr("Press any key to see the next student!")
        stdscr.getch()    
        stdscr.clear()

def sort_gpa(stdscr, student_list):
    stdscr.clear()
    dtype = [('Name', 'U10'), ('GPA', float)]
    students = numpy.array([], dtype=dtype)
    for student in student_list._StudentsList__students:
        marks = student.show_mark()
        total_weighted_marks = 0
        total_credits = 0
        for course, mark in marks.items():
            credits = course.show_credit()
            total_weighted_marks += mark * credits
            total_credits += credits
        if total_credits == 0:
            gpa = 0
        else:
            gpa = total_weighted_marks / total_credits
        students = numpy.append(students, numpy.array([(student.show_name(), gpa)], dtype))
    student_sort = numpy.sort(students, order='GPA')[::-1]
    stdscr.addstr("GPA Leaderboard:\n")
    for student in student_sort:
        stdscr.addstr(f"Name: {student['Name']}, GPA: {student['GPA']:.2f}\n")
    stdscr.addstr("Press any key to close!")
    stdscr.getch()    
    stdscr.clear()