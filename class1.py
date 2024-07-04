# Create a class named BankAccount with attributes account_number, account_holder, and balance. 
# Implement deposit methods, withdraw, and display balance.
# Also, include a method to calculate interest on the balance.
class BankAccount:
    def __init__(self, account_number, account_holder, balance,time,rate):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.time = time
        self.rate = rate
        
    def deposit(self, balance):
        
        balance+=self.balance
        print("Successfully deposit") 
        print(f"the total amount is {balance}")
         
    def withdraw_amount(self,balance):
         
         balance = self.balance-balance
         print(f"the blc is {balance}")
    def calcintresh(self):
        we = self.balance*self.time*self.rate/100
        print(f"the intrest on the balance is {we}")
             
    
                

# def maiin():
            
#     p1 = BankAccount(1246,"Aniruddha",2000,2,3) 
#     p1.deposit(200) 
#     p1.withdraw_amount(500) 
#     p1.calcintresh(2000,2,3)
#     we = p1.deposit(2000),p1.withdraw_amount(500) , p1.calcintresh(2000,2,3)
#     return we
# maiin()    
def time_rate(time,rate):
    time = int (input("Enter the time: "))
    rate = int (input("Enter the rate: "))
    p1 = BankAccount(1246,"Aniruddha",2000,2,3)
    p1.deposit(200)
    p1.withdraw_amount(500) 
    p1.calcintresh(2000,time,rate)
time_rate()    