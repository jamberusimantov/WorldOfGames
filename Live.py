from GuessGame import GuessGame
from MemoryGame import MemoryGame
from CurrencyRouletteGame import CurrencyRouletteGame
from Score import Score

def welcome(name):
    return ("Hello " + name + " and welcome to the World of Games (WoG).\n" +
            "Here you can find many cool games to play.\n")


def load_game():
    print(
        "Please choose a game to play:\n" +
        "\t1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n" +
        "\t2. Guess Game - guess a number and see if you chose like the computer\n" +
        "\t3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"
    )
    chosen_level = ''
    chosen_game = ''
    while not chosen_game.isdigit() or not 1 <= int(chosen_game) <= 3:
        chosen_game = input("Please choose game from 1 to 3: ")
    while not chosen_level.isdigit() or not 1 <= int(chosen_game) <= 5:
        chosen_level = input("Please choose game difficulty from 1 to 5: ")
    game = int(chosen_game)
    level = int(chosen_level)
    isWon = False
    if game == 1:
        isWon = MemoryGame(level).play()
    elif game == 2:
        isWon = GuessGame(level).play()
    else:
        isWon = CurrencyRouletteGame(level).play()
    if isWon:
        Score.add_score(level)
