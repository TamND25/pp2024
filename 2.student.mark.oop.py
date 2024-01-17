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