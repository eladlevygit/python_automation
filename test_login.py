import pytest
from selenium import webdriver
from time import sleep


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    sleep(10)

def test_standard_user_login(browser):
    browser.get("https://www.saucedemo.com/")
     #setattr(test_standard_user_login()

