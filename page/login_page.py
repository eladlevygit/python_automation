from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, browser):
        self.browser = browser

    def open_home_page(self):
        self.browser.get("https://www.saucedemo.com/")


    def type_username(self, username):
         username_input_filed = self.browser.find_element(By.ID, "user-name")
         username_input_filed.clear()
         username_input_filed.send_keys(username)

    def type_password(self, password):
        password_input_filed = self.browser.find_element(By.CSS_SELECTOR, '[data-test="password"]')
        password_input_filed.clear()
        password_input_filed.send_keys(password)

    def click_login_button(self):
        self.browser.find_element(By.NAME, "login-button").click()
        