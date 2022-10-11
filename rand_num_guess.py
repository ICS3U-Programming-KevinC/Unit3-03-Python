# !/user/bin/env python3

# Created by Kevin Csiffary
# Date: Oct. 10, 2022
# This program asks the user to guess a random number between 0 and 9
# the answer is randomly generated


import random


def main():
    # Pick a random number
    random_number = random.randrange(0, 9)

    # Ask user for their guess
    print("Im thinking of a number between 0 and 9")
    user_guess = int(input("What is your guess? "))

    # Adds an extra line
    print("")

    # Checks if the user guessed correctly
    if user_guess == random_number:
        print("You guessed correctly!")
    else:
        print("You guessed wrong. The correct answer was: " + str(random_number))


if __name__ == "__main__":
    main()
