# Create a class named Student with attributes name, roll_number, and marks.
# Implement methods to initialize these attributes, display student details, and calculate the average marks.class
class Student:
    def __init__(self,name,roll_number):
        self.name = name
        self.roll_number = roll_number
     
    def students(self):
       
        mark1 = int (input("Mark in math: "))
        mark2 = int (input("Mark in com: "))
        mark3 = int (input("Mark in english: "))  
        sum = mark1 + mark2 + mark3/3
        return sum
    def details(self):
        print(self.students())
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        

obj = Student("Anup",12) 
print(obj.students()) 
print(obj.details())  