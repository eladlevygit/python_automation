class LoginPage:

    def open_home_page(self):
        browser.get("https://www.saucedemo.com/")

    def type_username(self):
         username_input_filed = browser.find_element(By.ID, "user-name")
         username_input_filed.clear()
         username_input_filed.send_keys("standard_user")

    def type_password(self):
        password_input_filed = browser.find_element(By.CSS_SELECTOR, '[data-test="password"]')
        password_input_filed.clear()
        password_input_filed.send_keys("secret_sauce")

    def clice_login_button(self):
        browser.find_element(By.NAME, "login-button").click()
        