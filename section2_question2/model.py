class Account:
    def __init__(self, name, balance):
        self.id = abs(hash('X80023' + name))
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < 0:
            return "Insufficient funds !!"

        self.balance -= amount

    def __str__(self):
        return f"{self.name}'s account ({self.id}). Balance: {self.balance}"

class DevAccount(Account):
	
    def get_balance(self):
        return self.balance

    def set_balance(self, amount):
        self.balance = amount

    def transfer(self, account_to, amount):
        if self.balance - amount < 0:
            return "Insufficient funds !!"

        account_to.deposit(amount)
        self.withdraw(amount)
        return "Success"
