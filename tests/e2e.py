from selenium import webdriver
from selenium.webdriver.common.by import By
from Utils import SCORES_UI


def test_scores_service(url):
    d = webdriver.Chrome()
    d.get(url)
    el = d.find_element(By.ID, "score")
    if el.text.isdigit():
        return 1 <= int(el.text) <= 1000
    return False


def main_function():
    if test_scores_service(SCORES_UI):
        return 0
    else:
        return -1
