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

    # get account balance
    def get_account_balance(self):
        return self.balance

    # yield interest
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

# User of a bank account
class User:
    def __init__(self, name, email):
        self.name = name  # User name
        self.email = email # User email
        self.accounts = {
            'checking': BankAccount(int_rate=0.02, balance=0),
            'savings': BankAccount(int_rate=0.02, balance=0)
        }
        #self.account = BankAccount(int_rate=0.02, balance=0) # User BankAccount

    # deposit method
    def make_deposit(self, account, amount):
        self.accounts[account].deposit(amount)
        return self
    # withdrawal method
    def make_withdrawal(self, account, amount):
        self.accounts[account].withdraw(amount)
        return self
    # display User name and account balance
    def display_user_balance(self, account):
        print(f"User: {self.name}, {account.title()}: Balance: ${self.accounts[account].get_account_balance()}")
        return self
    # yield interest for User BankAccount
    def yield_interest(self, account):
        self.accounts[account].yield_interest()
        return self
    # transfer amount from User self to User other_user
    def transfer_money(self, account, other_user, other_account, amount):
        self.make_withdrawal(account, amount) # withdrawl amount from User self
        other_user.make_deposit(other_account, amount) # deposit amount to User other_user
        return self

Mark = User('Mark', 'mark@gmail.com')
Jim = User('Jim', 'jim@yahoo.com')

Mark.make_deposit('checking', 50).make_deposit('checking', 125).make_deposit('checking', 85).make_withdrawal('checking', 120).display_user_balance('checking')
Mark.make_deposit('savings', 110).make_deposit('savings', 150).make_withdrawal('savings', 65).make_withdrawal('savings', 90).display_user_balance('savings')

Jim.make_deposit('checking', 240).make_deposit('checking', 105).make_withdrawal('checking', 120).display_user_balance('checking')
Jim.make_deposit('savings', 60).make_deposit('savings', 90).make_withdrawal('savings', 65).make_withdrawal('savings', 10).display_user_balance('savings')

Mark.transfer_money('checking', Jim, 'savings', 90).display_user_balance('checking').display_user_balance('savings')
Jim.display_user_balance('checking').display_user_balance('savings')
