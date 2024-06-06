from selenium import webdriver
from selenium.webdriver.common.by import By
from Utils import SCORES_UI, BAD_RETURN_CODE

# test our web service.
# get the application URL as an input,
# open a browser to that URL,
# select the score element in our web page,
# check that it is a number between 1 and 1000 and return a boolean value if it’s true or not
def test_scores_service(url):
    d = webdriver.Chrome()
    d.get(url)
    el = d.find_element(By.ID, "score")
    return el.text.isdigit() and 1 <= int(el.text) <= 1000

# call our tests function.
# The main function will return -1 as an OS exit code if the tests failed and 0 if they passed.
def main_function():
    if test_scores_service(SCORES_UI):
        return 0
    else:
        return BAD_RETURN_CODE
