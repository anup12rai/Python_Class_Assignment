# Create a class named Car with attributes make, model, and year.
# Implement methods to initialize these attributes, display car details, 
# and calculate the car's age. (For eg: if the car’s year is 2020, the car age is 4 years)
from datetime import datetime
class car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def display(self): 
        print(self.make)
        print(self.model)
        print(self.year)
    def yearse(self):
        
        current_year = datetime.now().year
        age = current_year - self.year
        return age

car1 = car("Toyota","Carmy",2020)  
car1.display()      
print(car1.yearse()) 
