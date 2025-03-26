import pytest
from selenium import webdriver
from time import sleep

@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    sleep(3)