from Live import welcome, load_game
from Utils import screen_cleaner

# clear screen be4 games
screen_cleaner()
# greet the user
print(welcome(input("Please enter a name: ")|"Guy"))
# load the game
load_game()
