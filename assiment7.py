import random
sum = 0
choose = input("Enter the game you want to play:\n1. Guess number\n2. Dice\n")

if choose == "1":
    print("You chose guess number")
    iny = int(input("Enter a number between 1-5: "))
    ds = random.randint(1, 5)
    
    if iny == ds:
        print("You guessed the correct number!")
    else:
        print(f"Wrong guess. The number was {ds}")
        
        
        

elif choose == "2":
    print("You chose dice")
    def anup():
        we = random.randint(1,6)
        return we 
    while True:
        for i in range(1):
            nuo = anup()
            nop = anup()
            total_sum = nuo + nop
            print(f"Sum of {nuo} and {nop} is: {total_sum}")
            if total_sum == 12:
                ch = input("press 1 to roll dice again: ")
                if ch !=1:
                    break
            else:
                input("another person turn press enter..")    
            
        
            

else:
    print("Invalid choice. Please enter 1 or 2.")


