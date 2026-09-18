from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    POSTAL_CODE_FIELD = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    TOTAL = (By.CSS_SELECTOR, ".summary_total_label")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(self, name, lastname, postal_code):
        self.driver.find_element(*self.FIRST_NAME_FIELD).send_keys(name)
        self.driver.find_element(*self.LAST_NAME_FIELD).send_keys(lastname)
        self.driver.find_element(*self.POSTAL_CODE_FIELD).send_keys(
            postal_code)
        self.driver.find_element(*self.CONTINUE_BTN).click()

    def get_total(self):
        self.wait.until(EC.presence_of_element_located(
            (self.TOTAL)))

        return self.driver.find_element(*self.TOTAL).text
