class teacher:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name} age: {self.age}")
class student(teacher):
    pass

value = student("Anuiuddha",18)
value.display()       