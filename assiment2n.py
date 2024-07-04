# WAP in Python asks the user for the height and base, take them as parameters and find the area of the triangle.
def area_of_triangle(h,b):
    area_of_triangle = 1/2*h*b
    return area_of_triangle

h = int(input("Input the height of the triangle: "))    
b = int(input("Input the base of the triangle: "))

print("The area of the triangle is: ",area_of_triangle(h,b))