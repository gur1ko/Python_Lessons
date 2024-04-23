# main.py

import database

def register():
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    account_number = input("Enter your account number (format: TB001): ")

    database.register_consumer(name, surname, account_number)

def fill_balance():
    account_number = input("Enter the account number you want to fill: ")
    amount = float(input("Enter the amount you want to transfer: "))

    database.fill_balance(account_number, amount)

def transfer_money():
    sender_account = input("Enter your account number: ")
    recipient_account = input("Enter the recipient's account number: ")
    amount = float(input("Enter the amount you want to transfer: "))

    if not database.validate_account_number(sender_account) or not database.validate_account_number(recipient_account):
        print("Invalid account number format. Please try again.")
        return

    if sender_account not in database.consumer_db:
        print("Sender's account not found. Please try again.")
        return

    if recipient_account not in database.consumer_db:
        print("Recipient's account not found. Please try again.")
        return

    sender_balance = database.consumer_db[sender_account]['balance']
    if sender_balance < amount:
        print("Insufficient balance. Transfer cannot be completed.")
        return

    database.consumer_db[sender_account]['balance'] -= amount
    database.consumer_db[recipient_account]['balance'] += amount
    print(f"Successfully transferred {amount} to account {recipient_account}.")

def main():
    while True:
        print("Choose an option:")
        print("1. Register")
        print("2. Fill balance")
        print("3. Transfer money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            register()
        elif choice == '2':
            fill_balance()
        elif choice == '3':
            transfer_money()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
