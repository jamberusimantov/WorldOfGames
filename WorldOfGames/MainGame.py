from .Live import welcome, load_game
from .Utils import screen_cleaner

screen_cleaner()
username = input("Please enter a name: ")
print("\n" + welcome(username or 'Guy'))
load_game()
