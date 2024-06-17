from GuessGame import GuessGame
from MemoryGame import MemoryGame
from CurrencyRouletteGame import CurrencyRouletteGame
from Score import Score
from Utils import screen_cleaner, BAD_RETURN_CODE
from time import sleep
from sys import exit

# This function has a person name as an input and returns a greeting string
def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG).\n\nHere you can find many cool games to play.\n"


# This function prints out the instructions,
# gets an input from the user about the game he chose.
# get the level of difficulty
# check the input of the chosen game (number between 1 and 3),
# check the input of level of difficulty (input should be a number between 1 and 5).
def load_game():
    while True:
        print(
            "Please choose a game to play:\n\n" +
            "\t1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n\n" +
            "\t2. Guess Game - guess a number and see if you chose like the computer\n\n" +
            "\t3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"
        )
        chosen_game = ''
        chosen_difficulty = ''
        
        while not chosen_game.isdigit() or not 1 <= int(chosen_game) <= 3:
            chosen_game = input("Please choose game from 1 to 3: ")
        print("\n")
        while not chosen_difficulty.isdigit() or not 1 <= int(chosen_difficulty) <= 5:
            chosen_difficulty = input("Please choose game difficulty from 1 to 5: ")
        
        games = [MemoryGame, GuessGame, CurrencyRouletteGame]
        is_won = games[int(chosen_game)-1](int(chosen_difficulty)).play()

        if is_won:
            print(f"\nSUPER COMBO !!!")
            if Score.add_score(int(chosen_difficulty)) == BAD_RETURN_CODE:
                print(f"An error occurred while accumulating score")
                exit(BAD_RETURN_CODE)
        else:
            print(f"\nTRY AGAIN !!!")

        sleep(2)
        if input("\nWould you like to keep playing? enter y to continue: ").lower() == "y":
            screen_cleaner()
        else:
            print("\nGAME OVER !!!")
            if Score.reset_score() == BAD_RETURN_CODE:
                print(f"An error occurred while resetting score")
                exit(BAD_RETURN_CODE)
            return
