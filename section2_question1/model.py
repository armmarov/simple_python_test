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
        return self.balance

    def __str__(self):
        return f"{self.name}'s account ({self.id}). Balance: {self.balance}"
