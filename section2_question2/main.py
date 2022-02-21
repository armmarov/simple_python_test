from model import DevAccount

all_accounts = {}

account1 = DevAccount("Ammar", 0)
account2 = DevAccount("Aalif", 0)
account3 = DevAccount("Abuya", 0)

all_accounts[account1.id] = account1
all_accounts[account2.id] = account2
all_accounts[account3.id] = account3

print("Set balance for 1st DevAccount")
all_accounts[account1.id].set_balance(50)
print(all_accounts[account1.id].__str__())

print("")
print("Set balance for 2nd DevAccount")
all_accounts[account2.id].set_balance(20)
print(all_accounts[account2.id].__str__())

print("")
print("Set balance for 3rd DevAccount")
all_accounts[account3.id].set_balance(90)
print(all_accounts[account3.id].__str__())

print("")
print("Transfer 30 from account 1 to account 2")
all_accounts[account1.id].transfer(all_accounts[account2.id], 30)

print("")
print("Balance for account 1")
print(all_accounts[account1.id].get_balance())

print("")
print("Balance for account 2")
print(all_accounts[account2.id].get_balance())
