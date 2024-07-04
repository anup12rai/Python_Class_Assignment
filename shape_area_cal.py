# Create a base class Shape with a method area(). 
# Then, create two derived classes Circle and square that
# override the area() method to calculate the area of a circle and a square, respectively.
# Demonstrate polymorphism by creating a list of shapes and calculating their areas using a loop.
import math
class Shape():
    def area():
         pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self): 
        areaa = math.pi*self.radius**2  
        print(f"the area of the circle is {areaa}")
class Square(Shape):
    def __init__(self, side):   
        self.side = side
    def area(self):
        areaa = self.side**2
        print(f"the area of the square is {areaa}")

value1 = Circle(12)
value2 = Square(3)
shape = [value1,value2]
for i in shape:
    i.area()        