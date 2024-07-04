# Write a Python function that takes a list as input and returns the reverse of that list. Do not use the built-in reverse() method. 
list = []
list1 = []
for i in range(5):
    user_input = int(input("Enter the number: "))
    list.append(user_input)

for i in range(5, 0, -1):
    at = list[i-1]
    #print(i)
    
    list1.append(at)
     
print(list1)
 
