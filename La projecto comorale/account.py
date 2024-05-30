class Transaction:
    def __init__(self, type, amount, description):
        self.type = type
        self.amount = amount
        self.description = description

    def __str__(self):
        return f"{self.type}: {self.amount} GEL - {self.description}"

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

class Account:
    LOAN_INTEREST_RATE = 0.082  # Fixed loan interest rate (8.2%)

    def __init__(self, owner, initial_balance):
        self.owner = owner
        self.balance = initial_balance
        self.iban = None
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        transaction = Transaction("Deposit", amount, "Deposit to account")
        self.transactions.append(transaction)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            transaction = Transaction("Withdrawal", amount, "Withdrawal from account")
            self.transactions.append(transaction)
            return True
        else:
            print("Insufficient balance")
            return False

    def transfer(self, recipient, amount):
        if self.withdraw(amount):
            recipient.deposit(amount)
            transaction = Transaction("Transfer", amount, f"Transfer to {recipient.iban}")
            self.transactions.append(transaction)
            recipient_transaction = Transaction("Transfer", amount, f"Transfer from {self.iban}")
            recipient.transactions.append(recipient_transaction)
            print("Transfer successful")
        else:
            print("Transfer failed due to insufficient balance")

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return [str(transaction) for transaction in self.transactions]

    def get_owner_name(self):
        return self.owner.get_full_name()