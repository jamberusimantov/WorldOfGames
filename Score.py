from Utils import SCORES_FILE, BAD_RETURN_CODE

class Score:
    @staticmethod
    def add_score(difficulty):
        points_of_winning = (difficulty * 3) + 5
        try:
            f = open(SCORES_FILE, "a")
            f.close()
            f = open(SCORES_FILE)
            current_score = f.readline()
            if current_score.isdigit():
                current_score = str(points_of_winning + int(current_score))
            else:
                current_score = str(points_of_winning)
            f.close()
            f = open(SCORES_FILE, "w")
            f.write(current_score)
            f.close()
        except BaseException:
            print(BaseException.args)
            return BAD_RETURN_CODE
