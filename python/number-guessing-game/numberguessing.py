import random

number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100. Your goal is to try and guess the number.")
print("You have 5 attempts to guess the correct number.")
print("Let's begin!")

attempts = 0

while attempts < 5:

    user_num = int(input("Guess a number between 1 and 100: "))

    if user_num < 1 or user_num > 100:

        print("Invalid input! Please guess a number between 1 and 100.")
        continue

    attempts += 1

    if user_num < number:

        print("Too low! Try again.")

    elif user_num > number:

        print("Too high! Try again.")

    else:

        print("Congratulations! You've guessed the correct number:", number)
        print("It took you", attempts, "attempts.")
        break

if attempts == 5 and user_num != number:

    print("Sorry, you've run out of attempts. The correct number was:", number)
