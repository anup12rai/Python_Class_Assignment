
# Write a Python function that takes a list of integers as input and returns the count of even and odd numbers in the list.
# Use a parameterized function to take the list as input.
list = []
no_of_even=0
no_of_odd=0
list3 = []
list2 = []
def count_even_odd(num):
   
   no_of_even=0
   no_of_odd=0
   for i in range(len(list)):
    if list[i]%2==0:
       
       no_of_even +=1
       
       list2.append(list[i])
    elif list[i]%2!=0:
          
        no_of_odd+=1
        
        list3.append(list[i])
    print(f"there is {no_of_odd}, {no_of_even}") 
  
for i in range(5):
    num = int(input("Enter a number: "))
    list.append(num)
    
print(list)
count_even_odd(num)  
print("there are",len(list2),"Even") 
print("there are",len(list3),"odds")

# list = [1,2,3,4,5,6]
# for i in range(len(list)):
#     if list[i]%2==0:
#        print(list[i], "is even")
#     elif list[i]%2!=0:
#         print(list[i], "is odd")   