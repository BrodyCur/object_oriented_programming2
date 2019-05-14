class BankAccount:

    interest_rate = 0.01
    accounts = []

    def __init__(self):
        self.balance = 0

    def deposit(self, num):
        self.balance += num
        return self.balance

    def withdraw(self, num):
        self.balance -= num
        return self.balance

    @classmethod
    def create(cls):
        bank_account = BankAccount()
        cls.accounts.append(bank_account)
        return bank_account

    @classmethod
    def total_funds(cls):
        total = 0
        for account in cls.accounts:
            total += account.balance
        return total

    @classmethod
    def interest_time(cls):
        for account in cls.accounts:
            account.balance += account.balance * cls.interest_rate
        return account.balance


my_account = BankAccount.create()
your_account = BankAccount.create()

print(my_account.balance) 
print(BankAccount.total_funds()) 

my_account.deposit(200)
your_account.deposit(1000)

print(my_account.balance) 
print(your_account.balance) 
print(BankAccount.total_funds()) 

BankAccount.interest_time()

print(my_account.balance) 
print(your_account.balance) 
print(BankAccount.total_funds()) 

my_account.withdraw(50)

print(my_account.balance) 
print(BankAccount.total_funds()) 