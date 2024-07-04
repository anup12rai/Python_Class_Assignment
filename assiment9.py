# Write a Python function to convert a temperature from Celsius to Fahrenheit.
def convert_to_fahrenheit(user):
    f = 9/5*user+32
    return f
    
user = int (input("Enter the temperature to convert in fahrenheit:"))   
print(convert_to_fahrenheit(user),"fahrenheit")