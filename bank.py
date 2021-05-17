class Bank:
    car_name="KCB"
    def __init__ (self,name,balance):
            self.name=name
            self.balance=balance
    def amount(self):
        return f"The remaining amount is{self.balance}"

    def name(self):
        return f"{self.name} bank is where I pay my lil sis school fees"

    

