# WAP to create an empty list, and ask the user about the items he/she would like to add to the list. The user should be able to add as many items as he/she wants. 

empty_list = []

sd = int(input("Enter the item size: "))
for i in range(sd):
    ui = input("Enter the list name:")
    sa = empty_list.append(ui)
print(f"you enter this list {empty_list}")   

rt = int(input("Do u want to remove this item from the list if yes then prenn 1 and no then 0:")) 
if rt == 1:
    op = input("Enter the item: ")
    pi = empty_list.remove(op)
    print(empty_list)
elif rt == 0:
    print("thank you")    
