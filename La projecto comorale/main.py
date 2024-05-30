from functions import *

def main():
    while True:
        menu = ["1. Create bank account", "2. Control balance", "3. Transfer money", "4. Account details", "5. Account history", "6. Loan calculator", "7. Exit"]
        for i in menu:
            print(i)
        choice = int(input("Enter number: "))

        if choice == 1:
            name = input("To create account, enter your name: ")
            while True:
                amount = int(input("Enter initial balance (0 -> 100): "))
                if amount > 100:
                    print("Initial balance should not be more than 100 GEL")
                else:
                    break
            unique_IBAN = generate_unique_IBAN()
            add_account(name, amount, unique_IBAN)
            print(f"Account added successfully with IBAN: {unique_IBAN}")

        elif choice == 2:
            iban = input("Enter your IBAN: ")
            get_account_details(iban)

        elif choice == 3:
            # Add code for transfer money functionality
            pass

        elif choice == 4:
            iban = input("Enter your IBAN: ")
            get_account_details(iban)

        elif choice == 5:
            # Add code for account history functionality
            pass

        elif choice == 6:
            iban = input("Enter your IBAN: ")
            loan_amount = float(input("Enter loan amount: "))
            calculate_loan(iban, loan_amount)

        elif choice == 7:
            break

if __name__ == "__main__":
    main()