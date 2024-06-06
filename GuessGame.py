from random import random

# The purpose of guess game is to start a new game, cast a random number between 1 to a
# variable called difficulty. The game will get a number input from the user.
class GuessGame:
    # set props
    difficulty = 0
    secret_number = 0

    # construct an instance with difficulty as param
    def __init__(self, difficulty):
        self.difficulty = difficulty

    # generate number between 1 and difficulty and save it to prop
    def generate_number(self):
        self.secret_number = int((random() * self.difficulty) + 1)

    # prompt the user for a number between 1 and difficulty and return the number
    def get_guess_from_user(self):
        guess = ''
        while not guess.isdigit() or not 1 <= int(guess) <= self.difficulty:
            guess = input(f"Please choose number from 1 to {str(self.difficulty)}: ")
        return int(guess)

    # compare the secret generated number to the one prompted by the get_guess_from_user
    def compare_results(self, user_number):
        return self.secret_number == user_number

    # call the functions above and play the game.
    # Will return True / False if the user lost or won.
    def play(self):
        print("\nGuess - Game")
        self.generate_number()
        return self.compare_results(self.get_guess_from_user())
