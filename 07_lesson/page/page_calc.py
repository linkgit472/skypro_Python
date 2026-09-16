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
        self.driver = driver
        driver.get(
            "https://bonigarcia.dev/\n"
            "selenium-webdriver-java/slow-calculator.html")
        WebDriverWait(driver, 10)

    def delay_field(self, value):
        self.driver.find_element(*self.DELAY_INPUT).clear()
        self.driver.find_element(*self.DELAY_INPUT).send_keys(value)

    def sum_7_8(self):
        self.driver.find_element(*self.INPUT_7).click()
        self.driver.find_element(*self.SUM).click()
        self.driver.find_element(*self.INPUT_8).click()
        self.driver.find_element(*self.EQUALS).click()

    def get_result(self):
        WebDriverWait(self.driver, 45).until(
            EC.text_to_be_present_in_element(
                             self.RESULT, "15"))

        return self.driver.find_element(*self.RESULT).text
