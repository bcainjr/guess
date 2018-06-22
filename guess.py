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
import shelve   # Using shelve for possible expansion of project.
import os.path


class Stats:
    """
        The Stats class is used to keep track of player statistics and
        can be possibly implemented to handle several players.
    """

    def __init__(self, gamesPlayed=0, validGuesses=0, invalidGuesses=0):
        """
            __init__ can create a default Stats object or accept
            gamesPlayed - total number of games played
            validGuesses - total number of valid guesses
            invalidGuesses - total number of invalid guesses
        """

        self.gamesPlayed = gamesPlayed
        self.validGuesses = validGuesses
        self.invalidGuesses = invalidGuesses

    @property
    def gamesPlayed(self):
        """Returns the value of total games played"""

        return self._gamesPlayed

    @gamesPlayed.setter
    def gamesPlayed(self, gamesPlayed):
        """Assigns the total games played"""

        self._gamesPlayed = gamesPlayed

    @property
    def validGuesses(self):
        """Returns the total valid guesses"""

        return self._validGuesses

    @validGuesses.setter
    def validGuesses(self, validGuesses):
        """Assigns the total valid guesses"""

        self._validGuesses = validGuesses

    @property
    def invalidGuesses(self):
        """Returns total invalid guesses"""

        return self._invalidGuesses

    @invalidGuesses.setter
    def invalidGuesses(self, invalidGuesses):
        """Assigns total invalid guesses"""

        self._invalidGuesses = invalidGuesses

    def load(self):
        """
            The load method loads the players statistics.
        """

        with shelve.open("guessGameStats.save", "c") as aFile:
            player = aFile.get("player")

        return player

    def save(self):
        """
            The save method saves the players statistics.
        """

        with shelve.open("guessGameStats.save", "c") as aFile:
            aFile["player"] = self

    def __str__(self):
        """
            The __str__ method enables the Stats class to be used in the
            print function.
        """

        statOutput =  (
            "{:^50}\n{}\n".format("Player Statistics", 50 * "*")
            + "Games Played: {}\n".format(self.gamesPlayed)
            + "Valid Guesses: {}\n".format(self.validGuesses)
            + "Invalid Guesses: {}\n".format(self.invalidGuesses)
            + "Average: {:.2f}%\n".format(self.gamesPlayed / self.validGuesses * 100)
        )

        return statOutput


def guessGame(cliArg=None):
    """
        The guessGame function is used to handle the games functionality.
        The game will pick a random number 1 to 100 and prompt the user
        to guess it. It will tell the user if the guess is right,
        to low or to high.
    """

    playerStats = Stats()

    # Check if the user has played before loading stats
    if os.path.exists("guessGameStats.save"):
        playerStats = playerStats.load()


    numToGuess = random.randint(1, 100)
    playerStats.gamesPlayed += 1
    guesses = False
    lied = False
    toHigh = "{} is too high - try again"
    toLow = "{} is too low - try again"

    if cliArg == "-u":
        ulamsNum = ulams(numToGuess)
    else:
        ulamsNum = 0

    while True:
        if not guesses:
            print("I'm Thinking of a number from 1 to 100\n"
                  "Try to guess my number", end="")
            guesses = True

        try:
            usrInput = input(": ")

            if usrInput.isdigit() and 1 <= int(usrInput) <= 100:
                intInput = int(usrInput)
                playerStats.validGuesses += 1
            else:
                print("{} is not a valid guess - try again".
                      format(usrInput), end="")
                playerStats.invalidGuesses += 1
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
            print("{} is correct! You guessed my number in {} guess(es).".
                  format(usrInput, playerStats.validGuesses))
            if lied:
                print(iLied.format(ulamsNum))
            elif cliArg == "-u":
                print("I did not lie this game.")

            # Save the player Stats
            playerStats.save()
            break
        elif intInput < numToGuess:
            if intInput == ulamsNum:
                print(toHigh.format(usrInput), end="")
                iLied = "I lied about {} being to high."
                lied = True
            else:
                print(toLow.format(usrInput), end="")
        elif intInput > numToGuess:
            if intInput == ulamsNum:
                print(toLow.format(usrInput), end="")
                iLied = "I lied about {} being to low"
                lied = True
            else:
                print(toHigh.format(usrInput), end="")

    print(playerStats)


def ulams(defaultRandInt):
    """
        ulams function is used when the -u option is used on the
        command line. It will pick a random number not equal to the
        numberToGuess in the guessGame function.
    """

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
