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


import sys
import random
import re


def guessGame(cliArg=None):
    numToGuess = random.randint(1, 100)
    validGuesses = 0
    guesses = False
    lied = False
    toHigh = "{} is too high - please guess again"
    toLow = "{} is too low - please guess again"

    if cliArg == "-u":
        ulamsNum = ulams(numToGuess)
    else:
        ulamsNum = 0

    while True:
        if not guesses:
            print("I'm Thinking of a number from 1 to 100\n"
                  "Try to guess my number", end="")

        try:
            usrInput = input(": ")

            if usrInput.isdigit() and 1 <= int(usrInput) <= 100:
                intInput = int(usrInput)
                validGuesses += 1
                guesses = True
            else:
                print("{} is not a valid guess - please guess again".
                      format(usrInput), end="")
                continue

        except (KeyboardInterrupt, EOFError):
            usrInput = input("\nWould you like to quit [y]es|[n]o: ")
            
            if usrInput.lower() in ["y", "yes"]:
                exit()
            elif usrInput.lower() in ["n", "no"]:
                guesses = False
                continue
            else:
                print("Seriously... I quit...")
                exit()

        if intInput == numToGuess:
            print("{} is correct! You guessed my number in {} guesses.".
                  format(usrInput, validGuesses))
            if lied:
                pass
            elif cliArg == "-u":
                print("I did not lie this game.")
            break
        elif intInput < numToGuess:
            if ulamsNum == numToGuess:
                print(toHigh.format(usrInput), end="")
            else:
                print(toLow.format(usrInput), end="")
        elif intInput > numToGuess:
            if ulamsNum == numToGuess:
                print(toLow.format(usrInput), end="")
            else:
                print(toHigh.format(usrInput), end="")

def ulams(defaultRandInt):
    eqNum = True
    while eqNum:
        randNum = random.randint(1, 100)
        if not randNum == defaultRandInt:
            eqNum = False

    return randNum


def main():
    if "-u" in sys.argv and len(sys.argv) < 3:
        guessGame(sys.argv[1])
    elif len(sys.argv) == 1:
        guessGame()
    else:
        print("Improper use of CLI arguments\n"
              "No arguments for default.\n"
              "-u for Ulam's game.\n")


if __name__ == "__main__":
    main()
