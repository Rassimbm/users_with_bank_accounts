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
        
    def withdrawal(self, amount):
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

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = Bank_account(interest_rate = 0.02, balance = 0)
    
    def user_account_infos(self):
        self.account.display_account_info()
        return self
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdrawal(amount)
        return self

user_1 = User('Rassim Benmhamed', 'rassimb@codingdojo.com')
user_1.make_deposit(100).make_withdrawal(50).user_account_infos()

