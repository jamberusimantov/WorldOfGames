from Utils import SCORES_FILE, BAD_RETURN_CODE

# package that is in charge of managing the scores file.
# The scores file at this point will consist of only a number.
# That number is the accumulation of the winnings of the user.
# Amount of points for winning a game is as follows: (DIFFICULTY X 3) + 5
# Each time the user is winning a game, the points he one will be added to his current amount of point saved in a file.
class Score:
    def __init__(self):
        pass

    # The function’s input is a variable called difficulty.
    # The function will try to read the current score in the scores file,
    # if it fails it will create a new one and will use it to save the current score.
    @staticmethod
    def add_score(difficulty):
        points_of_winning = (difficulty * 3) + 5
        current_points = 0
        try:
            f = open(SCORES_FILE, "a+")
            f.seek(0, 0)
            score = f.readline()
            if score.isdigit():
                current_points = int(score)
            with open(SCORES_FILE, "w") as f:
                f.write(str(points_of_winning + current_points))
        except BaseException:
            print(BaseException.args)
            return BAD_RETURN_CODE