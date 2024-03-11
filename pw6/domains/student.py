class Student:
    def __init__(self, id, name, dob):
        self.__name = name
        self.__id = id
        self.__dob = dob
        self.__marks = {}
    
    def show_name(self):
        return self.__name
    
    def show_id(self):
        return self.__id
    
    def show_dob(self):
        return self.__dob
    
    def add_mark(self, course, mark):
        self.__marks[course] = mark

    def show_mark(self):
        return self.__marks