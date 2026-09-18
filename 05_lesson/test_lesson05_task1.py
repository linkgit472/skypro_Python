# Шаги:
# Откройте страницу https://httpbin.qa-territory.online.
# Найдите и кликните на ссылку HTML Form.
# Проверьте, что URL изменился на /forms/post.
# Вернитесь назад на главную страницу.
# Проверьте, что вернулись на исходный URL.

from time import sleep
from selenium.webdriver.common.by import By


def test_new_url(driver):
    driver.get('https://httpbin.qa-territory.online')
    sleep(3)
    driver.find_element(By.LINK_TEXT, "HTML Form").click()
    sleep(3)

    expected_url = 'https://httpbin.qa-territory.online/forms/post'

    assert driver.current_url == expected_url


def test_current_url(driver):
    driver.back()
    sleep(3)

    expected_url = 'https://httpbin.qa-territory.online/'

    assert driver.current_url == expected_url
