from random import random
from urllib3 import PoolManager
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
        apikey = 'fca_live_Uy5FqISqz4ThsvVDSsyN62mgRKgL6ZsoUiaTS3u3'
        try:
            url = f"http://api.freecurrencyapi.com/v1/latest?apikey={apikey}&currencies={target_currency}&base_currency={base_currency}"
            response = PoolManager().request("GET", url)
            if response.status != 200:
                raise(BaseException(response.reason))
            interval = []
            for i in range((5 - self.difficulty) * 2 + 1):
                interval.append(int(response.json()['data'][target_currency] * base_amount) + i - (5 - self.difficulty))
            return interval
        
        except BaseException as e:
            print(f"An error occurred: {e}")
            exit(BAD_RETURN_CODE)


    def get_guess_from_user(self, base_amount):
        guess = ''
        while not guess.isnumeric() or int(guess) < 1:
            guess = input(f"\nPlease guess the value of {str(base_amount)}$ in ILS: ")
        return float(guess)


    def play(self):
        print("\nCurrency Roulette - Game")
        base_amount = int((random() * 100) + 1)
        return self.get_guess_from_user(base_amount) in self.get_money_interval(base_amount)
