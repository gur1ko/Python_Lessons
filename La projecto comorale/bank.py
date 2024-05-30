import random
from account import Account

class Bank:
    def __init__(self):
        self.accounts = {}
        self.iban_prefix = "TB"
        self.generated_ibans = set()

    def create_account(self, first_name, last_name, initial_balance):
        iban = self._generate_unique_iban()
        account = Account(first_name, last_name, initial_balance)
        account.iban = iban
        self.accounts[iban] = account
        print(f"Account created successfully with IBAN: {iban}")

        take_loan = input("Do you want to take a loan? (y/n) ")
        if take_loan.lower() == "y":
            loan_amount = float(input("Enter loan amount: "))
            total_payable = loan_amount * (1 + Account.LOAN_INTEREST_RATE)
            print(f"Total payable amount (including interest): {total_payable} GEL")
            confirm_loan = input("Do you want to proceed with the loan? (y/n) ")
            if confirm_loan.lower() == "y":
                account.deposit(loan_amount)
                print("Loan amount added to your account balance.")

        return account

    def _generate_unique_iban(self):
        while True:
            iban = self.iban_prefix + ''.join(random.choices('0123456789', k=5))
            if iban not in self.generated_ibans:
                self.generated_ibans.add(iban)
                return iban

    def get_account(self, iban):
        if iban in self.accounts:
            return self.accounts[iban]
        else:
            print("Invalid IBAN")
            return None