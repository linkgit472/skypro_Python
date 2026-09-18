from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ShoppingCartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def check_item(self):
        self.driver.find_elements(By.CLASS_NAME, 'cart_item')

    def checkout_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()
