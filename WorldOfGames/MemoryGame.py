from time import sleep
from random import random

def verify_int_arr_in_range(arr, start, end):
    if len(arr) < 1:
        return False
    for i in range(len(arr)):
        if not arr[i].isdigit() or not start <= int(arr[i]) <= end:
            return False
    return True


# The purpose of memory game is to display an amount of random numbers to the users for 0.7 seconds,
# prompt the user for the numbers that he remember.
# If he was right with all the numbers the user will win otherwise he will lose.
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
        while not verify_int_arr_in_range(guess, 1, 101) or len(guess) < self.difficulty:
            guess = input(f"Please insert sequence of {str(self.difficulty)} numbers from 1 to 101: ").split(sep=" ")
        for i in range(self.difficulty):
            guess[i] = int(guess[i])
        return guess


    def is_list_equal(self, list1, list2):
        if not len(list1) == len(list2) or not len(list1) == self.difficulty :
            return False
        for i in range(len(list1)):
            if not list1[i] == list2[i]:
                return False
        return True


    def play(self):
        print("\nMemory - Game")
        sequence = self.generate_sequence()
        print(f"\n{sequence}", end="\r")
        sleep(0.7)
        user_sequence = self.get_list_from_user()
        return self.is_list_equal(user_sequence, sequence)
