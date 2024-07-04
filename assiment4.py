# WAP to create an empty list. Then Enter at least 4 items to the list. Then, print every item of the list 1 by 1 using the loop
list = []
for i in range(0,4):
    rt = input("Enter 4 alphabets: ")
    list.append(rt)
    print(list)
print("Here is the list which is print using loop")
for i in range(len(list)):
    print(list[i])   