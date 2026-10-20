import allure
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
        """
        Инициализирует драйвер.

        :param driver : WebDriver - объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step(
        "Заполнение формы значениями "
        "{name}, {lastname}, {postal_code}"
    )
    def fill_form(self, name, lastname, postal_code):
        """
        Заполняет форму отправки информацией о покупателе.

        :param name : str - имя покупателя
        :param lastname : str - фамилия покупателя
        :param postal_code : str - почтовый индекс.
        """
        with allure.step(f"Ввести в поле имени {name}"):
            self.driver.find_element(*self.FIRST_NAME_FIELD).send_keys(name)
        with allure.step(f"Ввести в поле фамилии {lastname}"):
            self.driver.find_element(*self.LAST_NAME_FIELD).send_keys(lastname)
        with allure.step(f"Ввести в поле почтового индекса {postal_code}"):
            self.driver.find_element(*self.POSTAL_CODE_FIELD).send_keys(
                postal_code)
        with allure.step("Кликнуть на кнопку подтверждения оформления"):
            self.driver.find_element(*self.CONTINUE_BTN).click()

    @allure.step("Получение итоговой суммы заказа")
    def get_total(self):
        """
        Ожидает появление итоговой суммы на экране
        и возвращает ее текст.

        :return: str - текст итоговой суммы.
        """

        with allure.step("Дождаться появления итоговой суммы на экране"):
            total_element = self.wait.until(
                EC.presence_of_element_located(self.TOTAL))

        with allure.step("Считать текст итоговой стоимости"):
            total_text = total_element.text
            allure.attach(total_text, name="Итоговая сумма в отчете",
                          attachment_type=allure.attachment_type.TEXT)
            return total_text
