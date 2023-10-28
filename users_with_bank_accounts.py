class Bank_account:
    all_accounts = []
    
    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance
        Bank_account.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        print('===========')
        print(f'Your new balance is: ${self.balance}.')
        return self
        
    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= 5
            print(f'Your new balance is: ${self.balance}')
        return self
    
    def display_account_info(self):
        print('===========')
        print(f'Your available balance to use is: ${self.balance}')
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.interest_rate)
        return self
    @classmethod
    def print_bank_accounts(cls):
        for account in cls.all_accounts:
            account.display_account_info()

# Create a User class with an __init__ method
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = Bank_account(int_rate=0.02, balance=0)
    
    # Add a make_deposit method to the User class that calls on its bank account's instance methods.

    # Add a make_withdrawal method to the User class that calls on its bank account's instance methods.

    # Add a display_user_balance method to the User class that displays user's account balance

    # SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to

    # SENPAI BONUS: Add a transfer_money(self, amount, other_user) method to the user class that takes an amount and a different User instance, and transfers money from the user's account into another user's account.

