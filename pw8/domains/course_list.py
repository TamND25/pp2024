from domains.course import Course

class CoursesList:
    def __init__(self):
        self.__courses = []
    
    def add_course(self, course):
        if isinstance(course, Course):
            self.__courses.append(course)
        else:
            print("Invalid course")
    
    def show_courses_list(self, stdscr):
        stdscr.clear()
        for course in self.__courses:
            stdscr.addstr(f"Name: {course.show_name()}, ID: {course.show_id()}, Credit: {course.show_credit()}\n")
        stdscr.addstr("Press any key to close!")
        stdscr.getch()    
        stdscr.clear()

    def get_course_by_name(self, name):
        for course in self.__courses:
            if course.show_name() == name:
                return course
        return None
    
    def serialize(self):
        serialized_data = ""
        for course in self.__courses:
            serialized_data += f"{course.show_id()},{course.show_name()},{course.show_credit()}\n"
        return serialized_data

    def deserialize(self, data):
        self.__courses = []
        lines = data.split("\n")
        for line in lines:
            if line.strip():  # Ensure line is not empty
                parts = line.split(",")
                if len(parts) == 3:
                    c_id, c_name, c_credit = parts
                    course = Course(c_id, c_name, int(c_credit))
                    self.__courses.append(course)
                else:
                    print(f"Skipping invalid data: {line}")