'''
ASSIGNMENT 1:
Task: Make an exponent function that takes base and power as input parameters.
Assignment 2: 
Task: Make a guess game, with random integers between 1 and 10.

'''

def square(base, power):
        sum = base**power
        return sum
        
    
base = int(input("Enter the base: "))
power = int(input("Enter the power: "))
print(square(base, power))

