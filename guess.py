#!/usr/bin/env python3
#
# Python
# Project 2
#
# UMBC TDQC5
# Bruce Cain
#
# Create a Guessing game.
# The game will pick a number between 1 and 100.
# Prompt the user for a number and if its the correct number the user won.
# If its higher or lower the the computer will indicate as so.


import random
import re


def guessGame():
    print("I'm Thinking of a number from 1 to 100")
    usrInput = input("Try to guess my number: ")

    while True:
        usrValidation = re.search(regexInput, usrInput)
        validGuesses += 1

        if usrValidation:
            if int(usrInput) == numToGuess:
                print("{} is correct! You guessed my number in {} guesses.".
                      format(usrInput, validGuesses))
                break
            elif 1 <= int(usrInput) < numToGuess:
                usrInput = input("{} is too low - please guess again: ".
                                 format(usrInput))
            elif numToGuess < int(usrInput) <= 100:
                usrInput = input("{} is too high - please guess again: ".
                                 format(usrInput))
            else:
                usrInput = input("{} is not a valid guess - \
                                 please guess again: ".format(usrInput))
        else:
            usrInput = input("{} is not a valid guess - please guess again: ".
                             format(usrInput))


def main():
    regexInput = "^\d+$"
    numToGuess = random.randint(1, 100)
    validGuesses = 0

    try:
        guessGame()
    except (KeyboardInterrupt, EOFError):
        print("\nWorks")


if __name__ == "__main__":
    main()
