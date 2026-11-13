user_data={}
def new_acc():
    print("\n >>> You're all set to Save & Grow <<< \n'")
    name=input('Enter New Account Name:')
    pin=int(input('Choose your 4-digit Pin:'))
    if len(str(pin)) > 4 or len(str(pin)) < 4:
        print("Please Enter Valid 4-digit Pin \n")
        return
    else:
        pass
    deposit_amt=float(input("Enter your opening deposit amount:"))
    user_data[name]={'pin':pin,'Balance':deposit_amt}
    #user_data.update({'Name':name,'Pin':pin,'Amount':deposit_amt})
    #user_data.update({'Pin':pin})
    #user_data.update({'Amount':deposit_amt})a
    print(f'\n Hey! {name} Your Money Got a New Home \n')
def withdraw():
    print("\n^^^^ Withdrawal mode: ON ^^^^\n")
    name=input("Enter Account Name:")
    pin=int(input("Enter your Pin:"))
    if name in user_data and user_data[name]['pin'] == pin:
        withdrawal_amt=float(input("Enter Your withdrawal amount:"))
        if withdrawal_amt <= user_data[name]['Balance']:
            user_data[name]['Balance']-=withdrawal_amt
            print("\n >>>>> Cash out loud! <<<<< \n")
            print(f'After Withdrawal Balance Rs.{user_data[name]['Balance']} \n')
        else:
            print("Insufficient fund \n")
    else:
        print("Invalid name or incorret pin \n")
def deposit():
    print("\n^^^^ New deposit, New energy ^^^^ \n")
    name=input("Enter Your Name:")
    pin=int(input("Enter your Pin:"))
    if name in user_data and user_data[name]['pin'] == pin:
        dep_amt=float(input("Enter your deposit amount: \n"))
        user_data[name]['Balance'] += dep_amt
        print(">>>> Deposited. Secured. Leveled up💰 <<<< \n")
        print(f'After Deposited Balance Rs.{user_data[name]['Balance']} \n')
    else:
        print("Invalid name or incorrect pin \n")
def check_balance():
    print("\n^^^^ Let’s see what’s in the Wallet Today! ^^^^")
    name=input("\nEnter your name:")
    pin=int(input("Enter you pin:"))
    if name in user_data and user_data[name]['pin'] == pin:
        if user_data[name]['Balance'] >= 5000:
            print("\n>>>> Checked the numbers.It’s looking good!💰 <<<< \n")
        else:
            print("\n>>>> Checked the numbers.It’s looking Low Fund!💰 <<<< \n")
        print(f'Account Holder:{name}')
        print(f'Available Balance: {user_data[name]['Balance']} \n')
    else:
        print("Invalid name or incorrect pin \n")   
def show_customers():
    print("\n ^^^ Customer list loaded.Ready to Roll! ^^^ \n")
    for name,info in user_data.items():
        print(f'Name:{name},Balance:{info['Balance']} \n')
def main_menu():
    while True:
        print("$$$$   Welcome to RCB Bank   $$$$")
        print("$$$$-------------------------$$$$")
        print("$$$$  1. Open a new account  $$$$")
        print("$$$$  2. Withdraw Money      $$$$")
        print("$$$$  3. Deposit Money       $$$$")
        print("$$$$  4. Check Balance       $$$$")
        print("$$$$  5. Show Customers      $$$$")
        print("$$$$  6. Exit/Quit           $$$$")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
        choice=int(input("Choose Your Operation:"))        
        if choice == 1:
            new_acc()
        elif choice ==2:
            withdraw()
        elif choice ==3:
            deposit()
        elif choice ==4:
            check_balance()
        elif choice ==5:
            show_customers()
        elif choice ==6:
            print("\n > > We're Grateful for you! Thanks for choosing us < < \n")
            break
main_menu()
