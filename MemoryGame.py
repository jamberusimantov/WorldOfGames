# The purpose of memory game is to display an amount of random numbers to the users for 0.7
# seconds and then prompt them from the user for the numbers that he remember. If he was right
# with all the numbers the user will win otherwise he will lose.
import time
from random import random
from Utils import screen_cleaner


def verify_arr_of_ranged_int(arr_to_verify, start, end):
    if len(arr_to_verify) < 1:
        return False
    for i in range(len(arr_to_verify)):
        if not arr_to_verify[i].isdigit() or not start <= int(arr_to_verify[i]) <= end:
            return False
    return True


class MemoryGame:
    difficulty = 0

    def __init__(self, difficulty):
        self.difficulty = difficulty

    def generate_sequence(self):
        arr = []
        for i in range(self.difficulty):
            arr.append(int((random() * 101) + 1))
        return arr

    def get_list_from_user(self):
        guess = []
        arr = []
        while not verify_arr_of_ranged_int(guess, 1, 101):
            guess = input("Please insert sequence of " + str(self.difficulty) + " numbers from 1 to 101: ").split()
        while len(arr) < len(guess):
            arr.extend(int(i) for i in guess)
        return arr

    def is_list_equal(self, list1, list2):
        for i in range(self.difficulty):
            if list1[i] != list2[i]:
                return False
        return True

    def play(self):
        print("\nMemory - Game")
        sequence = self.generate_sequence()
        print(sequence)
        time.sleep(0.7)
        screen_cleaner()
        return self.is_list_equal(self.get_list_from_user(), sequence)
