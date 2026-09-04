# Открыть страницу: httpbin.qa-territory.online
# Проверить что заголовок содержит: httpbin

from time import sleep
from selenium.webdriver.common.by import By


def test_httpbun(driver):
    driver.get('https://httpbin.qa-territory.online/')
    sleep(10)
    title = driver.find_element(By.CSS_SELECTOR,
                                "div[class='container'] h1").text
    assert title == 'httpbin'
