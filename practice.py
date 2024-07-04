def simple_intrest(prin,rate,time):
    sim = prin*rate*time/100
    print(f"the simple intrest is {sim}")
    
def main():
    prin= int (input("Enter the principal: "))
    rate = int (input("Enter the rate: "))
    time = int(input("Enter the time: "))
    paas = simple_intrest(prin,rate,time)
    print(paas)

main()    

   