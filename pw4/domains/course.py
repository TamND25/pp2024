class Course:
    def __init__(self, id, name, credit):
        self.__name = name
        self.__id = id
        self.__credit = credit

    def show_name(self):
        return self.__name
    
    def show_id(self):
        return self.__id
    
    def show_credit(self):
        return self.__credit