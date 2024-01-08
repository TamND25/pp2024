numberOfStudents = 0
studentsList = []

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