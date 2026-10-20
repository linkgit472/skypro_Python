import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShoppingCartPage:

    CART_ITEMS = (By.CLASS_NAME, 'cart_item')
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "#checkout")

    def __init__(self, driver):
        """
        Инициализирует драйвер.

        :param driver: WebDriver - объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Проверить, что в корзину добавлено "
                 "{expected_count} товара(ов)")
    def check_items(self, expected_count: int):
        """
        Находит все элементы товаров в корзине и проверяет их количество.

        :param expected_count: int - ожидаемое количество товаров в корзине.
        """
        with allure.step("Дождаться загрузки списка товаров в корзине"):
            self.wait.until(EC.presence_of_element_located(self.CART_ITEMS))
            items = self.driver.find_elements(*self.CART_ITEMS)
            actual_count = len(items)

        with allure.step(f"Сверить количество: ожидается {expected_count},"
                         f"фактически {actual_count}"):
            allure.attach(str(actual_count),
                          name="Фактическое количество товаров",
                          attachment_type=allure.attachment_type.TEXT)
            assert actual_count == expected_count, (
                f"Ошибка: ожидалось {expected_count} товаров в корзине, "
                f"но обнаружено {actual_count}"
            )

    @allure.step("Нажать на кнопку перехода к оформлению заказа")
    def checkout_btn(self):
        """
        Нажимает на кнопку начала оформления заказа (Checkout).
        """
        with allure.step("Кликнуть на кнопку 'Checkout'"):
            self.wait.until(
                EC.element_to_be_clickable(self.CHECKOUT_BUTTON)).click()
