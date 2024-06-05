# This game will use the free currency api to get the current exchange rate from USD to ILS, will
# generate a new random number between 1-100 a will ask the user what he thinks is the value of
# the generated number from USD to ILS, depending on the user’s difficulty his answer will be
# correct if the guessed value is between the interval surrounding the correct answer
import math
import requests
from random import random
import interval
import urllib3

urllib3.disable_warnings()


def get_currency_rate():
    apikey = "fca_live_Uy5FqISqz4ThsvVDSsyN62mgRKgL6ZsoUiaTS3u3"
    freecurrencyapi = "http://api.freecurrencyapi.com/v1/latest?apikey=" + apikey + "&currencies=ILS"
    res = requests.get(freecurrencyapi, verify=False)
    if res.status_code == 200:
        return res.json()['data']['ILS']
    else:
        print(f"oh no error code {res.status_code}")
        return 0


class CurrencyRouletteGame:
    difficulty = 0

    def __init__(self, difficulty):
        self.difficulty = difficulty

    def get_money_interval(self, usd_amount):
        ils_total = math.floor(usd_amount * get_currency_rate())
        return interval.Interval(ils_total - (5 - self.difficulty), ils_total + (5 - self.difficulty))

    def get_guess_from_user(self, usd_amount):
        guess = ''
        while not guess.isdigit():
            guess = input("Please guess the value of " + str(usd_amount) + "$ in ILS: ")
        return int(guess)

    def play(self):
        print("\nCurrency Roulette - Game")
        usd_amount = int((random() * 100) + 1)
        ils_interval = self.get_money_interval(usd_amount)
        guess = self.get_guess_from_user(usd_amount)
        return guess in ils_interval

