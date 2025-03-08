import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    sleep(3)
    driver.quit()

def test_standard_user_login(browser):
    browser.get("https://www.saucedemo.com/")

    username_input_filed = browser.find_element(By.ID,"user-name")
    username_input_filed.clear()
    username_input_filed.send_keys("standard_user")

    password_input_filed = browser.find_element(By.CSS_SELECTOR, '[data-test="password"]')
    password_input_filed.clear()
    password_input_filed.send_keys("secret_sauce")

    browser.find_element(By.NAME, "login-button").click()


current_url = browser.current_url
print(f"{browser.current_url = }")
assert browser.current_url == "https://www.saucedemo.com/inventory.html"

products_page_title = browser.find_element(By.XPATH, '//*[@data-test="title"]').text
print(f"{products_page_title = }")
assert products_page_title == "Products"

