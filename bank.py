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
        try:
            10+amount
        except TypeError:
            return f'The amount must be in figures'    
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
        try:
            12+amount
        except TypeError:
            return f'The amount must be in figures' 


        if(amount>self.balance):
            return f"Your balance is {self.balance}.You cannot withdraw {amount}"
        else:
            self.balance-=amount
            now=datetime.now()
            transaction={"amount":amount,"time":now,"narration":"You have withdrawn"}
            self.statement.append(transaction)

            return self.show_balance()
        
    
    def borrow(self,amount):
        try:
         12+amount

        except TypeError:
            return f'The amount must be in figures' 

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
        try:
         12+amount
        except TypeError:
            return f'The amount must be in figures' 

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



    def transfer(self,account,amount):
        try:
         12+amount
        except TypeError:
            return f'The amount must be in figures' 
          
        fee=amount*0.05
        total=amount+fee
        if amount<0:
            return f'your balance is {self.balance}'
        elif total>self.balance:
            return f'your balance is {self.balance} and you need atleast {total} for the tranfer '    
        else:
            account.deposit(amount)
            self.balance=total
            return f'The amount has been transferred'

class mobile_money(Bank):
    def __init__(self, name, phoneNumber,service_provider):
        Bank .__init__(name,phoneNumber)
        service_provider=service_provider

        
    def buy_airtime(self,amount):
        try:
            10+amount
        except TypeError:
            return f"The the amount must be figures"
        if amount<0:
            return f" {self.name} your amount {amount} is too low"
        elif self.balance<amount:
            return f"your {self.balance} is too low you can't buy airtime"
        else:
            self.balance-=amount
            return f"you have bought airtime of {amount}, your new balance is {self.balance}"

          




        

  
         

