class Bank:
    def __init__(self,accNo,name,accType,balance=0):
        self.acc=accNo
        self.na=name
        self.accType=accType
        self.bal=balance
    def deposit(self,amount):
        if amount>0:
            self.bal+=amount
            print(f"Deposit successfull! New balance:{self.bal}")
        else:
            print(f"Invalid deposit amount.please enter a positive value,")
    def withdraw(self,amount):
        if amount>0:
            if amount<=self.bal:
                self.bal-=amount
                print(f"Withdrawal successfull New balance:{self.bal}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount.Please enter a positive value.")
    def display(self):
        print(f"\n Account Number:{self.acc}\n Account Holder Name:{self.na}")
        print(f"Account Type:{self.accType}\n Balance:{self.bal}")
        print("\n***Menu***")
        print("1.Deposit\n2.Withdraw\n3.Display\n4.Exit")
b1=Bank(1002,"Nidhi","Savings",0)
b1.display()
while True:
    #b1.display()
    choice=int(input("\nEnter your choice(1-4)"))
    if choice==1:
        d=int(input("Enter amount to be deposited:"))
        b1.deposit(d)
    elif choice==2:
        w=int(input("Enter amount to be withdraw:"))
        b1.withdraw(w)
    elif choice==3:
        b1.display()
    elif choice==4:
        print("Exiting...Thank you!")
        break
    else:
        print("Enter a valid choice")
         
