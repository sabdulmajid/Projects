# Classes.py
class student:
    def __init__(self, name, dateOfBirth, examMark):
        self.__name = name
        self.__dateOfBirth = dateOfBirth
        self.__examMark = examMark

    def displayExamMark(self):
        print("This student received a:", self.__examMark)

myStudent = student("Shaikh Ayman Abdul-Majid", "12/20/04", "100%")
myStudent.displayExamMark()

