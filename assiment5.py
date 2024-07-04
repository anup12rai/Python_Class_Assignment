#  Write a Python program that takes a list of numbers as input. Find and print the following:
# The sum of all the numbers in the list.
# The largest number in the list.
# # The smallest number in the list.
empty_list = []
sum = 0
for i in range(1,5):
    ppo = int(input("Enter the number: "))
    empty_list.append(ppo)
print(empty_list)

for i in range(0, len(empty_list)):
   
    sum+=empty_list[i]
print(f"the sum is {sum}")

'''for(i=1;i<=10;i++)
    sum+=i'''  
    
nurf = empty_list[0]
for i in empty_list[1:]:
    if i >   nurf:
        nurf = i
        
print(f"the largest number is {nurf}")      


vf = empty_list[0]
if i in empty_list[1:]:
    if i < vf:
        vf = i
print(f"the lower number is {vf}")        
    
    
      
    
