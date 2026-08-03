def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 / num2

def main():
    while True:
        print("\nWelcome to the calculator!")
        print("""Select an operation:
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
        5. Exit""")

        choice = input("Enter the number of the operation you want to perform: ")

        if choice == "5":
            print("Goodbye!")
            break

        if choice in ["1", "2", "3", "4"]:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == "1":
                print("The result is: ", add(num1, num2))
            elif choice == "2":
                print("The result is: ", subtract(num1, num2))
            elif choice == "3":
                print("The result is: ", multiply(num1, num2))
            elif choice == "4":
                try:
                    print("The result is: ", divide(num1, num2))
                except ValueError as e:
                    print(e)
        else:
            print("Invalid selection. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
