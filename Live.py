from GuessGame import GuessGame
from MemoryGame import MemoryGame
from CurrencyRouletteGame import CurrencyRouletteGame
from Score import Score
from Utils import screen_cleaner

# This function has a person name as an input and returns a greeting string
def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.\n"

# This function prints out the instructions,
# gets an input from the user about the game he chose.
# get the level of difficulty
# check the input of the chosen game (number between 1 and 3),
# check the input of level of difficulty (input should be a number between 1 and 5).
def load_game():
    print(
        "Please choose a game to play:\n" +
        "\t1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n" +
        "\t2. Guess Game - guess a number and see if you chose like the computer\n" +
        "\t3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"
    )
    # declare game vars
    chosen_game = ''
    chosen_difficulty = ''
    # loop to get game in range 1-3
    while not chosen_game.isdigit() or not 1 <= int(chosen_game) <= 3:
        chosen_game = input("Please choose game from 1 to 3: ")
    # loop to get difficulty in range 1-5
    while not chosen_difficulty.isdigit() or not 1 <= int(chosen_difficulty) <= 5:
        chosen_difficulty = input("Please choose game difficulty from 1 to 5: ")
    # set game vars
    game = int(chosen_game)
    difficulty = int(chosen_difficulty)
    # play and add score
    if game == 1:
        is_won = MemoryGame(difficulty).play()
    elif game == 2:
        is_won = GuessGame(difficulty).play()
    else:
        is_won = CurrencyRouletteGame(difficulty).play()
    if is_won:
        Score.add_score(difficulty)
    screen_cleaner()
