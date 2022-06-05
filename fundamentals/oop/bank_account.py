class BankAccount:
    all_accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    @classmethod
    # class method to get all instances of BankAccount
    def get_all_accounts(cls):
        for account in cls.all_accounts:
            print(f"Balance: ${account.balance}, interest rate: {account.int_rate}%")

    # deposit
    def deposit(self, amount):
        self.balance += amount
        return self

    # withdraw
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    # display account info
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    # yield interest
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

account_1 = BankAccount(4, 200)
account_2 = BankAccount(6, 300)

account_1.deposit(100).deposit(150).deposit(220).withdraw(200).yield_interest().display_account_info()
account_2.deposit(120).deposit(250).withdraw(110).withdraw(40).withdraw(60).withdraw(80).yield_interest().display_account_info()

BankAccount.get_all_accounts()
