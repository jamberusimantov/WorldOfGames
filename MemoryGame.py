import time
from random import random
from Utils import screen_cleaner, verify_arr_of_ranged_int

# The purpose of memory game is to display an amount of random numbers to the users for 0.7 seconds,
# prompt the user for the numbers that he remember.
# If he was right with all the numbers the user will win otherwise he will lose.
class MemoryGame:
    # set prop
    difficulty = 0

    # construct an instance with difficulty as param
    def __init__(self, difficulty):
        self.difficulty = difficulty

    # generate a list of random numbers between 1 and 101.
    # The list length will be difficulty.
    def generate_sequence(self):
        arr = []
        for i in range(self.difficulty):
            arr.append(int((random() * 101) + 1))
        return arr

    # return a list of numbers prompted from the user.
    # The list length will be in the size of difficulty.
    def get_list_from_user(self):
        guess = []
        while not verify_arr_of_ranged_int(guess, 1, 101) or len(guess) < self.difficulty:
            guess = input(f"Please insert sequence of {str(self.difficulty)} numbers from 1 to 101: ").split()
        for i in range(self.difficulty):
            guess[i] = int(i)
        return guess

    # compare two lists if they are equal.
    # The function will return True / False.
    def is_list_equal(self, list1, list2):
        if not len(list1) == len(list2) or not len(list1) == self.difficulty :
            return False
        for i in range(list1):
            if not list1[i] == list2[i]:
                return False
        return True

    # call the functions above and play the game.
    # Will return True / False if the user lost or won.
    def play(self):
        print("\nMemory - Game")
        sequence = self.generate_sequence()
        print(sequence)
        time.sleep(0.7)
        screen_cleaner()
        user_sequence = self.get_list_from_user()
        return self.is_list_equal(user_sequence, sequence)
