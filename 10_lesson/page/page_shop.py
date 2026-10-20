import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ShopPage:
    BACKPACK_ADD = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    BOLT_TSHIRT_ADD = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIZE_ADD = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
    SHOPPING_CART = (By.CSS_SELECTOR, ".shopping_cart_link")

    def __init__(self, driver):
        """Инициализирует драйвер.

        :param driver: WebDriver - объект драйвера Selenium."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Добавление товаров в корзину и переход к оформлению")
    def add_item(self):
        """
        Последовательно добавляет рюкзак, футболку и боди в корзину,
        после чего кликает на иконку корзины для перехода к списку покупок.
        """
        with allure.step("Добавить в корзину рюкзак 'Sauce Labs Backpack'"):
            self.driver.find_element(*self.BACKPACK_ADD).click()
        with allure.step("Добавить в корзину футболку "
                         "'Sauce Labs Bolt T-Shirt'"):
            self.driver.find_element(*self.BOLT_TSHIRT_ADD).click()
        with allure.step("Добавить в корзину боди 'Sauce Labs Onesie'"):
            self.driver.find_element(*self.ONESIZE_ADD).click()

        with allure.step("Нажать на иконку корзины для перехода "
                         "на страницу списка покупок"):
            self.driver.find_element(*self.SHOPPING_CART).click()
