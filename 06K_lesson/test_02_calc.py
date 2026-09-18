# Откройте страницу:
# https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
# в Google Chrome.
# В поле ввода по локатору #delay введите значение 45.
# Нажмите на кнопки:7+8=
# Проверьте, что в окне отобразится результат 15 через 45 секунд.

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_delay_45(driverChrome):
    driverChrome.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    WebDriverWait(driverChrome, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".display-4")))

    driverChrome.find_element(By.CSS_SELECTOR, '#delay').clear()
    driverChrome.find_element(By.CSS_SELECTOR, '#delay').send_keys('45')
    driverChrome.find_element(By.XPATH,
                              "//span[normalize-space()='7']").click()
    driverChrome.find_element(By.CSS_SELECTOR, "span:nth-child(4)").click()
    driverChrome.find_element(By.XPATH,
                              "//span[normalize-space()='8']").click()
    driverChrome.find_element(By.XPATH,
                              "//span[@class='btn btn-outline-warning']"
                              ).click()

    assert WebDriverWait(driverChrome,
                         45).until(EC.text_to_be_present_in_element(
                             (By.XPATH, "//div[@class='screen']"), "15"))
