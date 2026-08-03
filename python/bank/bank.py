print("Welcome to Lay Bank!\n")

def check_balance(balance):
    print("Your current balance is $" + str((balance)) + ".\n")

def deposit(balance, amount):
    balance += amount
    print("You have deposited $" + str(amount) + ". Your new balance is $" + str(balance) + ".\n")
    return balance

def withdraw(balance, amount):
    if amount > balance:
        print("Insufficient funds. Your current balance is $" + str(balance) + ".\n")
    else:
        balance -= amount
        print("You have withdrawn $" + str(amount) + ". Your new balance is $" + str(balance) + ".\n")
    return balance

def display_menu():
    print("""Select an option:
    1. Check Balance
    2. Deposit Money
    3. Withdraw Money
    4. Exit
    """)

def main():
    balance = 0.0

    while True:
        display_menu()
        option = input("Select your option: " )

        if option == "1":
            check_balance(balance)
        elif option == "2":
            amount = float(input("Enter the amount you would like to deposit: "))
            balance = deposit(balance, amount)
        elif option == "3":
            amount = float(input("Enter the amount you would like to withdraw: "))
            balance = withdraw(balance, amount)
        elif option == "4":
            print("Have a great day!")
            break
        else: 
            print("Invalid response, try again.")

if __name__ == "__main__":
    main()


