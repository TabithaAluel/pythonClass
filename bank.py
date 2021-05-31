from datetime import datetime
class Bank:

    def __init__(self,name,phoneNumber):
        self.name=name
        self.phoneNumber=phoneNumber
        self.balance=0
        self.statement=[]

    def show_balance(self):
        return f"Hello {self.name},your balance is {self.balance}."

    def deposit(self,amount):
        if(amount<0):
            return f"You cannot deposit money less than 0"
        else:
            self.balance+=amount
            now=datetime.now()
            transaction={"amount":amount,"time":now,"narration":"You deposited"}
            self.statement.append(transaction)


            return self.show_balance()


    def show_statement(self):
        for transaction in self.statement:
            amount=transaction["amount"]
            narration=transaction["narration"]
            time=transaction["time"]
            date=time.strftime("%d/ %m / %y")
            print(f"{date}:{narration}:{amount}")


    def withdraw(self,amount):
        if(amount>self.balance):
            return f"Your balance is {self.balance}.You cannot withdraw {amount}"
        else:
            self.balance-=amount
            now=datetime.now()
            transaction={"amount":amount,"time":now,"narration":"You have withdrawn"}
            self.statement.append(transaction)

            return self.show_balance()

    def borrow(self,amount):
        self.amount=amount
        if (amount>0):
            return f"You can borrow{amount}"
        else:
            return f"You cannot borrow another"
    
    def repay_loan(self,amount):
        self.amount=amount
        if(amount>0):
            return f"Please repay your loan of{amount}"
        else:
            return f"Your loan has been  paid!"
