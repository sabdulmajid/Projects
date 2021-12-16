# Classes.py
class Point:  # A way to define multiple functions in a single 'Class'. This becomes a separate sort of library.
    def move(self):
        print('move')

    def draw(self):
        print('draw')


point1 = Point()

point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()