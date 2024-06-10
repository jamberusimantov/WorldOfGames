from Live import welcome, load_game
from Utils import screen_cleaner

screen_cleaner()
user = input("Please enter a name: ")
print(f"\n{welcome(user or 'Guy')}")
load_game()
      