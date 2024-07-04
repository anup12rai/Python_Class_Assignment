# WAP in Python uses the function to take the marks of 5 subjects as parameters in the function and calculate the GPA.
def student_gpa(user_input,user_input1,user_input2):
    sum = user_input+user_input1+user_input2/3
    return sum


for i in range(2):
    user_input = int(input("Enter the marks of Mathematical: "))  
    user_input1 =   int(input("Enter the marks of Computer: "))
    user_input2 = int(input("Enter the marks of English: "))
    
for j in range(2):    
    print("The GPA of the students: ",student_gpa(user_input,user_input1,user_input2)) 
       
        