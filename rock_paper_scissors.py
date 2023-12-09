import random
import sys

while True:
    print("Rock, Paper, Scissors Game")
    print("\n")
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.randint(0, 2)

    user_number = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
    if user_number != 0 and user_number != 1 and user_number != 2:
        print(f"You chose an invalid option({user_number}), You lose!")
    else:
        print(f"Computer chose {options[computer_choice]}")

    if user_number == 0 and computer_choice == 2:
        print("You Win!")
    elif computer_choice == 0 and user_number == 2:
        print("You Lose!")
    elif computer_choice > user_number:
        print("You Lose!")
    elif user_number > computer_choice:
        print("You Win!")
    elif computer_choice == user_number:
        print("Draw!")
    else:
        print("There was an error. Try again")
