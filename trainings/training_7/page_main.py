from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class GoogleMainPage():
    SEARCH_FIELD = (By.NAME, "q")
    RESULTS_SELECTOR = (By.CSS_SELECTOR, "div.A6K0A")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def enter_search_query(self, query):
        search_field = self.wait.until(
            EC.presence_of_element_located(self.SEARCH_FIELD))
        search_field.clear()
        search_field.send_keys(query)
        search_field.send_keys(Keys.RETURN)

    def get_search_result(self):
        self.wait.until(EC.presence_of_element_located(self.RESULTS_SELECTOR))
        return self.driver.find_elements(*self.RESULTS_SELECTOR)
