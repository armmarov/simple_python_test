from model import Account

all_accounts = {}

account1 = Account("Ammar", 50)
account2 = Account("Aalif", 25)
account3 = Account("Abuya", 39)

all_accounts[account1.id] = account1
all_accounts[account2.id] = account2
all_accounts[account3.id] = account3

print("1st Account")
print(all_accounts[account1.id].__str__())

print("")
print("2nd Account")
print(all_accounts[account2.id].__str__())

print("")
print("3rd Account")
print(all_accounts[account3.id].__str__())

print("")
print("Deposit 70 to account 1")
all_accounts[account1.id].deposit(70)
print(all_accounts[account1.id].__str__())

print("")
print("Withdraw 100 from account 1")
all_accounts[account1.id].withdraw(100)
print(all_accounts[account1.id].__str__())

print("")
print("Withdraw 50 from account 1")
print(all_accounts[account1.id].withdraw(100))
print(all_accounts[account1.id].__str__())
