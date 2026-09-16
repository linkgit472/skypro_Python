from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class AuthPage:
    USERNAME_INPUT = (By.CSS_SELECTOR, "#user-name")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")
    LOGIN_BTN = (By.CSS_SELECTOR, "#login-button")

    def __init__(self, driver):
        self.driver = driver
        driver.get("https://www.saucedemo.com/")
        self.wait = WebDriverWait(driver, 10)

    def auth_form(self, username, password):
        self.driver.find_element(*self.USERNAME_INPUT
                                 ).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT
                                 ).send_keys(password)
        self.driver.find_element(*self.LOGIN_BTN).click()
