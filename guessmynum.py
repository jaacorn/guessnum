# jaacorn - December 10, 2017 - Project Conception
# jaacorn - December 10, 2017 - Ongoing Development
# guessmynum.py

import random
import sys

# Begin program UI
print("Welcome to \"Guess My Number\"!")
print("")
print("1 - Begin")
print("2 - Help")
print("3 - Exit")

mminput = input("::")

if int(mminput) == 1:
    num = random.randint(0,101)
    print("Guess a number between 1 and 100")
    print("")
    while True:
        guessinput = input("::")
        # check for 'quit game' command
        if str(guessinput) == ("quit"):
            print("")
            print("Game quit")
            sys.exit()
        # check if above or below guess range
        elif (int(guessinput) < 1 ) or (int(guessinput) > 100):
            print("Guess too high or low")
            print("Guess again")
            print("")
        # check if matches the randint
        elif int(guessinput) == int(num):
            print("Congratulations! You win!")
            break
        else:
            print("Incorrect guess")
            # Uncomment below for debugging purposes
            # print(num)
            print("")
    print("Game Over")
elif int(mminput) == 2:
    print("")
    print("Help Menu:\n")
    print("")
    print("   Guess My Number is a basic terminal game developed in Python.\n")
    print("The game is currently in alpha, and does not have a public release date.\n")
    print("All inquiries can be directed to jacorn812@gmail.com")
elif int(mminput) == 3:
    print("Goodbye")
    sys.exit()
else:
    print("Invalid input")
    print("Game closing")
