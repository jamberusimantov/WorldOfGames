import math
import requests
from random import random
from Utils import get_currency_rate
import interval

# This game will use the free currency api to get the current exchange rate from USD to ILS, will
# generate a new random number between 1-100 a will ask the user what he thinks is the value of
# the generated number from USD to ILS, depending on the user’s difficulty his answer will be
# correct if the guessed value is between the interval surrounding the correct answer
class CurrencyRouletteGame:
    # set prop
    difficulty = 0

    # construct an instance with difficulty as param
    def __init__(self, difficulty):
        self.difficulty = difficulty

    # get the current currency rate from USD to ILS
    # generate an interval as follows:
    # for given difficulty d, and total value of money t the interval will be: (t - (5 - d), t + (5 - d))
    def get_money_interval(self, usd_amount):
        il = interval.Interval(0, 0)
        try:
            rate = get_currency_rate()
            ils_total = math.floor(usd_amount * rate)
            if ils_total == 0:
                return il
            else:
                return interval.Interval(ils_total - (5 - self.difficulty), ils_total + (5 - self.difficulty))
        except BaseException:
            print(BaseException)
            return il

    # prompt a guess from the user to value a given amount of USD in ILS
    def get_guess_from_user(self, usd_amount):
        guess = ''
        while not guess.isdigit() or int(guess) < 0:
            guess = input(f"Please guess the value of {str(usd_amount)}$ in ILS: ")
        return float(guess)

    # call the functions above and play the game.
    # Will return True / False if the user lost or won.
    def play(self):
        print("\nCurrency Roulette - Game")
        usd_amount = int((random() * 100) + 1)
        ils_interval = self.get_money_interval(usd_amount)
        guess = self.get_guess_from_user(usd_amount)
        return guess in ils_interval
