# database.py

consumer_db = {
    "TB001": {"name": "John", "surname": "Doe", "balance": 100},
    "TB002": {"name": "Alice", "surname": "Smith", "balance": 100},
    "TB003": {"name": "Bob", "surname": "Johnson", "balance": 100}
}

def register_consumer(name, surname, account_number):
    while not validate_account_number(account_number):
        print("Invalid account number format. Please enter an account number in the format TB#SOMETHREEDIGITS.")
        account_number = input("Enter your account number (format: TB001): ")

    consumer_db[account_number] = {'name': name, 'surname': surname, 'balance': 100}  # Assign starting balance of 100
    print("You registered successfully.")

def fill_balance(account_number, amount):
    if account_number in consumer_db:
        consumer_db[account_number]['balance'] += amount
        print("Balance filled successfully.")
    else:
        print("Account number not found.")

def transfer_money(sender_account, recipient_account, amount):
    if sender_account not in consumer_db:
        print("Sender's account not found.")
        return False

    if recipient_account not in consumer_db:
        print("Recipient's account not found.")
        return False

    sender_balance = consumer_db[sender_account]['balance']
    if sender_balance < amount:
        print("Insufficient balance.")
        return False

    consumer_db[sender_account]['balance'] -= amount
    consumer_db[recipient_account]['balance'] += amount
    print(f"Successfully transferred {amount} to account {recipient_account}.")
    return True

def validate_account_number(account_number):
    if len(account_number) != 5:
        return False
    if account_number[:2] != 'TB':
        return False
    if not account_number[2:].isdigit():
        return False
    return True
