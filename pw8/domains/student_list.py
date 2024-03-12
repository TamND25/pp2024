from domains.student import Student
class StudentsList:
    def __init__(self):
        self.__students = []
    
    def add_student(self, student):
        if isinstance(student, Student):
            self.__students.append(student)
        else:
            print("Invalid student")
    
    def show_students_list(self, stdscr):
        stdscr.clear()
        for student in self.__students:
            stdscr.addstr(f"Name: {student.show_name()}, ID: {student.show_id()}, DOB: {student.show_dob()}\n")
        stdscr.addstr("Press any key to close!")
        stdscr.getch()    
        stdscr.clear()

    def serialize(self):
        serialized_data = ""
        for student in self.__students:
            serialized_data += f"{student.show_id()},{student.show_name()},{student.show_dob()}\n"
        return serialized_data

    def deserialize(self, data):
        self.__students = []
        lines = data.split("\n")
        for line in lines:
            if line.strip():  # Ensure line is not empty
                parts = line.split(",")
                if len(parts) == 3:
                    s_id, s_name, s_dob = parts
                    student = Student(s_id, s_name, s_dob)
                    self.__students.append(student)
                else:
                    print(f"Skipping invalid data: {line}")