import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class AuthPage:
    USERNAME_INPUT = (By.CSS_SELECTOR, "#user-name")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")
    LOGIN_BTN = (By.CSS_SELECTOR, "#login-button")

    def __init__(self, driver):
        """
        Инициализирует драйвер и открывает страницу авторизации.

        :param driver : WebDriver - объект драйвера Selenium.
        """
        self.driver = driver
        with allure.step("Открыть страницу авторизации"):
            driver.get("https://www.saucedemo.com/")
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Авторизация пользователя {username} с паролем {password}")
    def auth_form(self, username, password):
        """
        Заполняет форму авторизации и нажимает кнопку входа.

        :param username: str - имя пользователя для авторизации
        :param password: str - пароль для авторизации
        """
        with allure.step(f"Ввести в поле логина {username}"):
            self.driver.find_element(*self.USERNAME_INPUT
                                     ).send_keys(username)
        with allure.step(f"Ввести в поле пароля {password}"):
            self.driver.find_element(*self.PASSWORD_INPUT
                                     ).send_keys(password)
        with allure.step("Нажать на кнопку авторизации"):
            self.driver.find_element(*self.LOGIN_BTN).click()
