class BankAccount:
    all_accounts = []
    def __init__(self, int_rate = .015, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdrawal(self, amount):
        if amount > self.balance:
            self.balance = (self.balance - amount) - 5
            print("Insufficient Funds: Charging a $5 fee")
        else:
            self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Account Balance: {self.balance}")
        return self
    def yield_interest(self):
        self.balance = self.balance * (1 + self.int_rate)
        return self

    @classmethod
    def all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            print("Account Balance:",account.balance,"Interest Rate:",account.int_rate)
        return sum

member_one = BankAccount().deposit(500).deposit(50).deposit(75).withdrawal(100).yield_interest().display_account_info()
member_two = BankAccount().deposit(400).deposit(600).withdrawal(100).withdrawal(200).withdrawal(600).withdrawal(101).yield_interest().display_account_info()

BankAccount.all_balances()