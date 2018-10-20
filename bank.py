#create two accounts a)current account
                    #b) savings account
#each account has deposit and withdraw method and print statement
#each account had different minimum limit 
    #current account - overdraft of 1000
    #savings account - no overdraft


# create abstract parent account called Account
class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount):
        self.balance += amount
        # self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance - amount >= min_balance:
            self.balance -= amount
            # self.balance = self.balance - amount
        else:
            print("Sorry, not enough funds!")

    def statement(self):
        print("Account Balance: ${}".format(self.balance))

# create current account inherit from parent account
class Current(Account):
    def __init__(self, name, balance):
        # when I use x=Current("Zein, 500, -1000) - self.name="Zein", self.balance=500, self.min_balance = -1000
        super().__init__(name, balance, min_balance = -1000)

class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 0)
    def __str__(self):
        # without this when I print(x) it looks like <__main__.Current obect at 0x035..>
        # to improve this I use __str__
        return "{}'s Savings Account: Balance ${}".format(self, name, self.balance)    


x = Current("Zein", 500)
x.statement()
