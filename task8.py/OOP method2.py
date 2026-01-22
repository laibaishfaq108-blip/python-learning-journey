#Create account class with 2 attributes balance & account no.Create method for debit,credit & printing balance.
class Account:
    def __init__(self,balance,acc_no):
        self.balance=balance
        self.account_no=acc_no
    #Debit Method:
    def debit(self,amount):
        self.balance-=amount
        print("Current balance=",self.get_balance())
    #Credit Method:
    def credit(self,amount):
        self.balance+=amount
        print("Current balance=",self.get_balance())
    #Print balance:
    def get_balance(self):
        return self.balance    

acc1=Account(100000,804)
print(acc1.balance)
print(acc1.account_no)
acc1.debit(14000)
acc1.credit(1300)
