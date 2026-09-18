# Откройте страницу:
# https://bonigarcia.dev/selenium-webdriver-java/data-types.html
# в браузере Edge.
# Заполните форму значениями.
# Нажмите кнопку Submit.
# Проверьте, что поле Zip code подсвечено красным.
# Проверьте, что остальные поля подсвечены зеленым.

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_field_is_red(driverEdge):
    driverEdge.get(
        'https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
    WebDriverWait(driverEdge, 10).until(EC.visibility_of_element_located(
        (By.CLASS_NAME, 'display-4')))

    driverEdge.find_element(By.CSS_SELECTOR,
                            "input[name='first-name']").send_keys('Иван')
    driverEdge.find_element(By.CSS_SELECTOR,
                            "input[name='last-name']").send_keys('Петров')
    driverEdge.find_element(By.CSS_SELECTOR,
                            "input[name='address']").send_keys('Ленина, 55-3')
    driverEdge.find_element(By.CSS_SELECTOR,
                            "input[name='zip-code']").send_keys('')
    driverEdge.find_element(By.CSS_SELECTOR,
                            "input[name='city']").send_keys('Москва')
    driverEdge.find_element(By.CSS_SELECTOR,
                            "input[name='country']").send_keys('Россия')
    driverEdge.find_element(By.CSS_SELECTOR,
                            "input[name='e-mail']").send_keys(
                                'test@skypro.com')
    driverEdge.find_element(By.CSS_SELECTOR,
                            "input[name='phone']").send_keys('+7985899998787')
    driverEdge.find_element(By.CSS_SELECTOR,
                            "input[name='job-position']").send_keys('QA')
    driverEdge.find_element(By.CSS_SELECTOR,
                            "input[name='company']").send_keys('SkyPro')

    driverEdge.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    zip_code_error = WebDriverWait(driverEdge,
                                   10).until(EC.presence_of_element_located(
                                       (By.ID, 'zip-code')))
    zip_code_classes = zip_code_error.get_attribute("class")
    assert 'alert-danger' in zip_code_classes.split(), (
        "Поле Zip Code не красное")


def test_green_field(driverEdge):
    success_fields = [
        "first-name", "last-name", "address", "city",
        "country", "e-mail", "phone", "job-position", "company"
    ]

    for field_id in success_fields:
        element = WebDriverWait(driverEdge,
                                10).until(EC.presence_of_element_located(
                                    (By.ID, f"{field_id}")))

        element_classes = element.get_attribute("class")
        assert 'alert-success' in element_classes.split(), (
            f"Поле {field_id} не зеленое")
