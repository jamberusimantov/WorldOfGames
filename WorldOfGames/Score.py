from .Utils import SCORES_FILE, BAD_RETURN_CODE

# package that is in charge of managing the scores file.
# The scores file at this point will consist of only a number.
# That number is the accumulation of the winnings of the user.
# Amount of points for winning a game is as follows: (DIFFICULTY X 3) + 5
# Each time the user is winning a game, the points he one will be added to his current amount of point saved in a file.
class Score:

    def __init__(self):
        pass


    @staticmethod
    def add_score(difficulty):
        points_of_winning = (difficulty * 3) + 5
        current_points = 0
        try:
            with open(SCORES_FILE, "a+") as f:
                f.seek(0, 0)
                score = f.readline()
                if score.isnumeric():
                    current_points = int(score)
            with open(SCORES_FILE, "w") as f:
                f.write(str(points_of_winning + current_points))
        except BaseException as e:
            print(f"An error occurred: {e}")
            return BAD_RETURN_CODE


    @staticmethod
    def reset_score():
        try:
            with open(SCORES_FILE, "a") as f:
                pass
            with open(SCORES_FILE, "w") as f:
                f.write('0')
        except BaseException as e:
            print(f"An error occurred: {e}")
            return BAD_RETURN_CODE