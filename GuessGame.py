# The purpose of guess game is to start a new game, cast a random number between 1 to a
# variable called difficulty. The game will get a number input from the user.
from random import random


class GuessGame:
    difficulty = 0
    secret_number = 0

    def __init__(self, difficulty):
        self.difficulty = difficulty

    def generate_number(self):
        self.secret_number = int((random() * self.difficulty) + 1)

    def get_guess_from_user(self):
        guess = ''
        while not guess.isdigit() or not 1 <= int(guess) <= self.difficulty:
            guess = input("Please choose number from 1 to " + str(self.difficulty) + ": ")
        return int(guess)

    def compare_results(self, user_number):
        return self.secret_number == user_number

    def play(self):
        print("\nGuess - Game")
        self.generate_number()
        return self.compare_results(self.get_guess_from_user())
