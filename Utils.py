from os import system, name
import urllib3

# A string representing a file name. By default, “Scores.txt”
SCORES_FILE = "/Scores.txt"
SCORES_HTML = "Scores.html"
# url path for presented score
SCORES_UI = 'http://127.0.0.1:5000'
# A number representing a bad return code for a function
BAD_RETURN_CODE = -1

# clear the screen (useful when playing memory game or before a new game starts).
def screen_cleaner():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# loop and verify digits and in range of start to end
def verify_arr_of_ranged_int(arr, start, end):
    if len(arr) < 1:
        return False
    for i in range(len(arr)):
        if not arr[i].isdigit() or not start <= int(arr[i]) <= end:
            return False
    return True

def get_currency_rate():
    try:
        with open("/run/secrets/APIKEY") as f:
            apikey = f.read()
            freecurrencyapi = f"http://api.freecurrencyapi.com/v1/latest?apikey={apikey}&currencies=ILS"
            urllib3.disable_warnings()
            # Creating a PoolManager instance for sending requests.
            http = urllib3.PoolManager()
            # Sending a GET request and getting back response as HTTPResponse object.
            resp = http.request("GET", freecurrencyapi)
            if resp.status == 200:
                return res.data['data']['ILS']
            else:
                print(f"oh no error code {resp.status}")
                return BAD_RETURN_CODE
    except BaseException:
        print(BaseException.args)
        return BAD_RETURN_CODE
