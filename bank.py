from datetime import datetime
class Bank:

    def __init__(self,name,phoneNumber):
        self.name=name
        self.phoneNumber=phoneNumber
        self.balance=0
        self.statement=[]
        self.loan=0

    def show_balance(self):
        return f"Hello {self.name},your balance is {self.balance}."

    def deposit(self,amount):
        if(amount<0):
            return f"You   cannot deposit money less than 0"
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
        if amount<0:
            return f"You are not qualified"    
        elif self.loan < 0 :
            return f"You are not qualified"
        elif amount<0.1 * self.balance:
            return f"You are qualified"
        else:   
            
            loan=amount*1.05
            self.loan=loan
            self.balance+=amount
            now=datetime.now()
            transaction1={"amount":amount,"time":now,"narration":"You have withdrawn"}
            self.statement.append(transaction1)
            return f"You have borrowed {amount}"
           
            
              
    def repay_loan(self,amount):
        self.amount=amount
        if amount<0:
            return f"You cannot borrow loan"
        elif amount<=self.loan:
            self.loan==amount
            return f"You have paid your loan"
        else:
            diff=amount-self.loan
            self.loan=0
            self.deposit(diff)   
        
            now=datetime.now()
            transaction2={"amount":amount,"time":now,"narration":"You have withdrawn"}
            self.statement.append(transaction2)
            return f"Your have paid {amount} and {self.loan} is left"



  
         

