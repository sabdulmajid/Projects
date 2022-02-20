# Polymorphism.py
# Define superclass shape, with hidden attributes and public methods 
class shape:
    def __init__(self):
        self.__areaValue = 0
        self.__perimeterValue = 0
    def area(self):
        print("Area ", self.__areaValue)
    def perimeter(self):
        print("Perimeter ", self.__areaValue)

# Define derived class rectangle, with inherited attributes
class rectangle(shape):
    def __init__(self, length, breadth):
        shape.__init__(self)
        self.__length = length
        self.__breadth = breadth
    
    # The method area() is polymorphed to suit a rectangle.
    def area (self):
        self.__areaValue = self.__length * self.__breadth
        print("Area ", self.__areaValue)

class circle(shape):
    def __init__(self, radius):
        shape.__init__(self)
        self.__radius = radius
    # The method area() is polymorphed here to suit a circle.
    def area (self):
        self.__areaValue = self.__radius * self.__radius * 3.142
        print("Area ", self.__areaValue)



# Call the instance of the class (object) for circle - area is a specific method for circle (1 parameter)
myCircle = circle(10)
myCircle.area()

# Call the instance of the class (object) for a rectangle - area is a changed method for rectangle (2 parameters)
myRectangle = rectangle (10,17)
myRectangle.area()