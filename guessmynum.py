# jaacorn - December 10, 2017 - Project Conception
# jaacorn - December 10, 2017 - Ongoing Development
# jaacorn - January 6, 2024 - Back in dev
# guessmynum.py

import random
import sys
import time

# GLOBAL VARIABLES
rand_num = 0
user_input = 0
user_guess = 0


def safe_user_input(message):
    while True:
        try:
            userInput = int(input(message))       
        except ValueError:
            print("Not an valid number! Try again.")
            continue
        else:
            return userInput 
            break


def main():
    global rand_num
    global user_input
    rand_num = random.randint(0,101)


    print("Welcome to \"Guess My Number\"!")
    print("")
    print("1 - Begin")
    print("2 - Help")
    print("3 - Exit")

    user_input = safe_user_input(":: ")

    if user_input == 1:
        print("Guess a number between 1-100")
        print("\n")
        game()
    elif user_input == 2:
        game_help()
    elif user_input == 3:
        exit()
    else:
        print("Invalid input")
        print("Please enter one of the above options")
        time.sleep(3)
        main()


def game():
    global user_guess
    global rand_num
    user_guess = safe_user_input(":: ")
    if user_guess == rand_num:
        correct_guess()
    else:
        incorrect_guess()


def incorrect_guess():
    print("\n")
    print("Incorrect! Try again")
    if user_guess > rand_num:
        print("Hint: your guess was too high!")
    else:
        print("Hint: your guess was too low!")
    game()


def correct_guess():
    print("CORRECT!")
    print("You win!!!")
    time.sleep(3)
    main()


def game_help():
    print("\n")
    print("Help Menu:\n")
    print("   Guess My Number is a basic terminal game developed in Python.\n")
    print("The game is currently in alpha, and does not have a public release date.\n")
    print("All inquiries can be directed to jacorn812@gmail.com")
    user_input = input(":: ")
    main()


main()