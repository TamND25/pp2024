import curses
from input import set_number_of_student, set_number_of_courses, input_students_information, input_courses_information, add_mark
from output import show_mark, round_down_mark, sort_gpa
from domains.student_list import StudentsList
from domains.course_list import CoursesList


def main(stdscr):

    student_list = StudentsList()
    course_list = CoursesList()

    stdscr.clear()

    while True:
        stdscr.addstr("""
    0. Exit
    1. Input the total number of students.    
    2. Input the total number of courses.          
    3. Input student information. 
    4. Input course information.
    5. Input mark for student for a course.
    6. Show the students.
    7. Show the courses.
    8. Show the students' mark.
    9. Round-down students' mark.
    10. Sort GPA
    Input your option: 
    """)
        stdscr.refresh()
        option_str = stdscr.getstr().decode()
        option = int(option_str)
        curses.echo()
            
        if option == 0:
            break
        elif option == 1:
            set_number_of_student(stdscr)
        elif option == 2:
            set_number_of_courses(stdscr)
        elif option == 3:
            input_students_information(stdscr, student_list)
        elif option == 4:
            input_courses_information(stdscr, course_list)
        elif option == 5:
            add_mark(stdscr, student_list, course_list)
        elif option == 6:
            student_list.show_students_list(stdscr)
        elif option == 7:
            course_list.show_courses_list(stdscr)
        elif option == 8:
            show_mark(stdscr, student_list)
        elif option == 9:
            round_down_mark(stdscr, student_list)
        elif option == 10:
            sort_gpa(stdscr, student_list)
        else:
            stdscr.addstr("\nInvalid input. Please try again!")
            stdscr.addstr("Press any key to close!")
            stdscr.getch()    
            stdscr.clear()
        
        curses.noecho()

if __name__ == "__main__":
    curses.wrapper(main)