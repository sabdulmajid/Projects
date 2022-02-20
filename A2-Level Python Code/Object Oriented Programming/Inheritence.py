# Inheritence.py

# Define the class employee, with private attributes and public methods
class employee:
    def __init__(self, name, staffno):
        self.__name = name
        self.__staffno = staffno
        self.__fullTimeStaff = True
    def showDetails(self):
        print("Employee Name " + self.__name)
        print("Employee Number", self.__staffno)

# Define the derived partTime class from employee, with the similar inherited attributes.
class partTime(employee):
    def __init__(self, name, staffno):
        employee.__init__(self, name, staffno)
        self.__fullTimeStaff = False
        self.__hoursWorked = 0
    def getHoursWorked(self):
        return(self.__hoursWorked)

# Define the derived fullTime class from employee, with other similar inherited attributes.
class fullTime(employee):
    def __init__(self, name, staffno):
        employee.__init__(self, name, staffno)
        self.__fullTimeStaff = True
        self.__yearlySalary = 0
    def getYearlySalary(self):
        return(self.__yearlySalary)

# Create an instance of the class fullTime (an object)
permenantStaff = fullTime("Shaikh Ayman Abdul-Majid", 2618)
permenantStaff.showDetails()

# Create an instance of the class partTime (an object)
temporaryStaff = partTime("Laith Alnajjar", 2781)
temporaryStaff.showDetails()