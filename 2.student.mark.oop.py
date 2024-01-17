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
        if isinstance(student, Student):
            self.__students.append(student)
        else:
            print("Invalid student")
    
    def showStudentsList(self):
        for student in self.__students:
            print(f"Name: {student.showname()}, ID: {student.showid()}, DOB: {student.showdob()}")