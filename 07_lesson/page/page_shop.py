from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ShopPage:
    BACKPACK_ADD = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    BOLT_TSHIRT_ADD = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIZE_ADD = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
    SHOPPING_CART = (By.CSS_SELECTOR, ".shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_item(self):
        self.driver.find_element(*self.BACKPACK_ADD).click()
        self.driver.find_element(*self.BOLT_TSHIRT_ADD).click()
        self.driver.find_element(*self.ONESIZE_ADD).click()

        self.driver.find_element(*self.SHOPPING_CART).click()
