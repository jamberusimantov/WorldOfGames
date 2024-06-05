from os import system, name
SCORES_FILE = "/Scores.txt"
SCORES_UI = 'http://127.0.0.1:5000/scores'
BAD_RETURN_CODE = 1


def screen_cleaner():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
