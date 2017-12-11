# jaacorn - December 10, 2017 - Project Conception
# jaacorn - December 10, 2017 - Ongoing Development
# guessmynum.py

import random
import sys

# Begin program UI
print("Welcome to \"Guess My Number\"!")
print("")
print("1 - Begin")
print("2 - Exit")

mminput = input("::")

if int(mminput) == 1:
    num = random.randint(0,101)
    print("Guess a number between 1 and 100")
    print("")
    while True:
        guessinput = input("::")
        if int(guessinput) == int(num):
            print("Congratulations! You win!")
            break
        else:
            print("Incorrect guess")
            # Uncomment below for debugging purposes
            # print(num)
            print("")
    print("Game Over")
else:
    print("Goodbye")
    sys.exit()
