import csv
import os
class BankAccount:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance!")
    def to_list(self):
        return [self.acc_no, self.name, self.balance]
class BankSystem:
    FILE_NAME = "D:\\PYTHON\\ACCOUNTS.csv "
    def __init__(self):
        # Create file with header if not exists
        if not os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Account No", "Name", "Balance"])
    def create_account(self):
        acc_no = input("Enter Account Number: ")
        name = input("Enter Name: ")
        balance = float(input("Enter Initial Balance: "))
        account = BankAccount(acc_no, name, balance)
        with open(self.FILE_NAME, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(account.to_list())
        print("Account Created Successfully!")
    def display_accounts(self):
        with open(self.FILE_NAME, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    def deposit(self):
        acc_no = input("Enter Account Number: ")
        amount = float(input("Enter Amount to Deposit: "))
        self.update_balance(acc_no, amount, "deposit")
    def withdraw(self):
        acc_no = input("Enter Account Number: ")
        amount = float(input("Enter Amount to Withdraw: "))
        self.update_balance(acc_no, amount, "withdraw")
    def update_balance(self, acc_no, amount, action):
        rows = []
        with open(self.FILE_NAME, 'r') as f:
            reader = csv.reader(f)
            rows = list(reader)
        for i in range(1, len(rows)):
            if rows[i][0] == acc_no:
                balance = float(rows[i][2])
                if action == "deposit":
                    balance += amount
                elif action == "withdraw":
                    if amount <= balance:
                        balance -= amount
                    else:
                        print("Insufficient Balance!")
                        return
                rows[i][2] = str(balance)
                print("Transaction Successful!")
                break
        else:
            print("Account Not Found!")
            return
        # Rewrite file
        with open(self.FILE_NAME, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
# 🔹 Menu Driven Program
bank = BankSystem()
while True:
    print("\n--- BANK MENU ---")
    print("1. Create Account")
    print("2. Display Accounts")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Exit")
    choice = input("Enter Choice: ")
    if choice == '1':
        bank.create_account()
    elif choice == '2':
        bank.display_accounts()
    elif choice == '3':
        bank.deposit()
    elif choice == '4':
        bank.withdraw()
    elif choice == '5':
        print("Thank you!")
        break
    else:
        print("Invalid Choice!")





