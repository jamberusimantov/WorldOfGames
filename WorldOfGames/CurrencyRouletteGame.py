from random import random
from interval import Interval
from urllib3 import request
from sys import exit
from Utils import BAD_RETURN_CODE

# This game will use the free currency api to get the current exchange rate from USD to ILS,
# generate a new random number between 1-100
# ask the user what he thinks is the value of the generated number from USD to ILS, 
# depending on the user’s difficulty his answer will be correct if the guessed value is between the interval surrounding the correct answer
class CurrencyRouletteGame:

    def __init__(self, difficulty):
        self.difficulty = difficulty


    def get_money_interval(self, base_amount):
        base_currency = 'USD'
        target_currency = 'ILS'
        try:
            with open("/run/secrets/APIKEY") as f:
                url = f"http://api.freecurrencyapi.com/v1/latest?apikey={f.read()}&currencies={target_currency}&base_currency={base_currency}"
                response = request("GET", url)
                if response.status != 200:
                    raise(BaseException(response.reason))
                add_amount = 5 - self.difficulty
                ils_total = int(base_amount * response.json()['data'][target_currency])
                return Interval(ils_total - add_amount, ils_total + add_amount)
        except BaseException as e:
            print(f"An error occurred: {e}")
            exit(BAD_RETURN_CODE)


    def get_guess_from_user(self, base_amount):
        guess = ''
        while not guess.isdigit() or int(guess) < 1:
            guess = input(f"\nPlease guess the value of {str(base_amount)}$ in ILS: ")
        return float(guess)


    def play(self):
        print("\nCurrency Roulette - Game")
        base_amount = int((random() * 100) + 1)
        money_interval = self.get_money_interval(base_amount)
        guess_from_user = self.get_guess_from_user(base_amount)
        return  guess_from_user in money_interval
