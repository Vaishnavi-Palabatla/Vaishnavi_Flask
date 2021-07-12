class bankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def withDrawal(self,amount):
        if(amount>self.balance):
            # print("Invalid amount")
            return "Invalid amount"
        else:
            self.balance=self.balance-amount
            return self.owner+" amount withdrawn is "+str(self.balance)
    def deposit(self,amount):
        self.balance=amount+self.balance
        return self.owner+" amount deposited is "+str(amount)
        # print("amount deposited")


details=bankAccount("vaishnavi",5000)
print(details.withDrawal(3000))
print(details.deposit(4000))
print(details.withDrawal(6000))
print(details.withDrawal(2000))
print(details.deposit(10000))
print(details.withDrawal(8000))
print(details.withDrawal(3000))
print(details.deposit(100))
print(details.withDrawal(9000))

details2=bankAccount("vaish",6000)
print(details2.withDrawal(4000))
print(details2.deposit(3000))
print(details2.withDrawal(6000))
print(details2.withDrawal(3000))
print(details2.deposit(100000))
print(details2.withDrawal(60000))
print(details2.withDrawal(3000))
print(details2.deposit(100))
print(details2.withDrawal(9000))


