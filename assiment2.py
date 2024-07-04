'''WAP to create a list with at least five items, and perform the following operations:
Create a system to check whether the entered item is present in the list or not. 
Pop an element
Insert an element at index 3
Append an element
Delete the element of index 2
Check the number of items on the list
Replace the item of index 4 with “Mango”
Clear the list
'''

list = ["apple", "orange", "jackfruit", "banana","dragonfruit"]

user = input("Enter the name of fruit that exist or not:")
if user in list:
    print(f"there is a fruit{user}")
else:
    print(f"there is no fruit{user}")    

kii=int(input("Enter the fruit index to pop: "))
de = list.pop(kii)
print(list)

ol = input("Enter the fruit to insert index 3: ")
print(list.insert(3,ol))

kl = input("Enter the fruit to append in index 3:")
fr = list.append(3,kl)
print(fr)

print(list.pop(3))

print(len(list))

list[4] = "Mango"
print(list)
list.clear()