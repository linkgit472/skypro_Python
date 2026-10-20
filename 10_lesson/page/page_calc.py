import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:

    DELAY_INPUT = (By.CSS_SELECTOR, '#delay')
    INPUT_7 = (By.XPATH, "//span[normalize-space()='7']")
    INPUT_8 = (By.XPATH, "//span[normalize-space()='8']")
    SUM = (By.XPATH, "(//span[normalize-space()='+'])")
    EQUALS = (By.XPATH, "//span[@class='btn btn-outline-warning']")
    RESULT = (By.XPATH, "//div[@class='screen']")

    def __init__(self, driver):
        """
        Инициализирует драйвер и открывает страницу калькулятора.

        :param driver : WebDriver - объект драйвера Selenium.
        """
        self.driver = driver
        with allure.step("Открыть страницу калькулятора"):
            driver.get(
                "https://bonigarcia.dev/\n"
                "selenium-webdriver-java/slow-calculator.html")
        WebDriverWait(driver, 10)

    @allure.step("Установка задержки в {value} секунд")
    def delay_field(self, value):
        """
        Очищает поле ввода задержки и устанавливает новое значение.

        :param value: int - количество секунд задержки.
        """
        with allure.step("Очистить поле задержки"):
            self.driver.find_element(*self.DELAY_INPUT).clear()

        with allure.step(f"Ввести значение задержки {value}"):
            self.driver.find_element(*self.DELAY_INPUT).send_keys(value)

    @allure.step("Выполнить операцию сложения 7 + 8")
    def sum_7_8(self):
        """
        Последовательно нажимает кнопки '7', '+', '8' и '=' на калькуляторе.
        """
        with allure.step("Нажать кнопку '7'"):
            self.driver.find_element(*self.INPUT_7).click()
        with allure.step("Нажать кнопку '+'"):
            self.driver.find_element(*self.SUM).click()
        with allure.step("Нажать кнопку '8'"):
            self.driver.find_element(*self.INPUT_8).click()
        with allure.step("Нажать кнопку '='"):
            self.driver.find_element(*self.EQUALS).click()

    @allure.step("Получить результат вычисления калькулятора.")
    def get_result(self):
        """
        Ожидает появления результата '15' на экране калькулятора
        и возвращает его текст.

        :return: str - текстовое значение результата с экрана калькулятора.
        """
        with allure.step("Ожидать отображения результата '15' на экране"):
            WebDriverWait(self.driver, 45).until(
                EC.text_to_be_present_in_element(
                                self.RESULT, "15"))

        with allure.step("Считать итоговый текст с экрана"):
            result_text = self.driver.find_element(*self.RESULT).text
            allure.attach(result_text, name="Фактический результат",
                          attachment_type=allure.attachment_type.TEXT)
            return result_text
