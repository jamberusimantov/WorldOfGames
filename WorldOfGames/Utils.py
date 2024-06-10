from os import system, name

SCORES_FILE = "/Scores.txt"
SCORES_HTML = "Scores.html"
SCORES_UI = 'http://127.0.0.1:8777'
BAD_RETURN_CODE = -1

def screen_cleaner():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
