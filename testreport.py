'''Important Task: Pre-PCR test for COVID :
WAP in Python that asks the user his/her name, age, address, gender, body temperature, ask if they have visited public places in the past week. Make a diagnosis report based on the following details:
-If he/she has a fever(temp in Celsius>38) AND he/she has visited public places in the past week, she needs a PCR test as he/she may have covid. Label his/her case as “HIGH RISK”
-If he/she has visited public places but does not have a fever, he/she may conduct a PCR test but is in “MEDIUM RISK”
-If he/she has a fever but has not visited public places, he/she may conduct a PCR test, and label his/her case as “Medium RISK”
-If he/she neither has a fever nor has visited public places, he/she need not conduct a PCR test and is under “LOW RISK”
Rainbow Tip: You need to use IF-ELSE statement, AND, NOT, and 
You can use the following sample as a reference:
'''
from datetime import datetime
today = datetime.today()
dater = today.strftime("Date: %A %d/%m/%Y")
def report(yi,ui,io,oi,rt,yu):
        print("\n\n\t------Report-----")
        print(f"\t\t\t\t{dater}")
        print("\n--------------------------------") 
        print(f"Name: {yi}")
        print(f"Age: {ui}")
        print(f"Address: {io}")
        print(f"Gender: {oi}")
        print("------------------------------------")
        print(f"BodyTem: {rt}")
        print(f"Visit in the public place: {yu}")
    
print("\n\n\n\t\t\t------------------------------Pre-PCR test for COVID--------------------------------\n")
while True:
    yi = input("Name: ")
    ui = int(input("Age: "))
    io = input("Address: ")
    oi = input("Gender: ")
    rt = int(input("BodyTem. : "))
    print("Thanks for enter the data")
    yu = input("Do you visit in the public place: 'yes' or 'no':")
    if rt > 38 and yu == "yes":  
        report(yi,ui,io,oi,rt,yu)
        print("Stay safe and take a medicine and checkup")
        print("Comment: High Risk\n")
    elif rt < 38 and yu == "no":
        report(yi,ui,io,oi,rt,yu)
        print("Comment: loe risk")
    elif rt < 38 and yu == "yes\n": 
        report(yi,ui,io,oi,rt,yu)  
        print("Comment: Medium Risk\n")
    
    
    ty = int (input("Enter 1 to store data:: "))
    if ty != 1:
        print("Thank you")
        break

