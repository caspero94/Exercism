import uuid

class BankAccount:
    def __init__(self):
        self.active = False
        self.saldo = 0
        self.id = str(uuid.uuid4())


    def get_balance(self):
        if self.active:
            return self.saldo
        else:
            raise ValueError('account not open')

    def open(self):
        if not self.active:
            self.active = True
        else:
            raise ValueError('account already open')

    def deposit(self, amount):
        if not self.active:
            raise ValueError('account not open')
        if amount <= 0:
            raise ValueError('amount must be greater than 0')
        else:
            self.saldo += amount

    def withdraw(self, amount):
        if not self.active:
            raise ValueError('account not open')
        if amount <= 0:
            raise ValueError('amount must be greater than 0')        
        if self.saldo < amount:
            raise ValueError('amount must be less than balance')
        else:
            self.saldo -= amount

    def close(self):
        if self.active:
            self.active = False
            self.saldo = 0
        else:
            raise ValueError('account not open')


