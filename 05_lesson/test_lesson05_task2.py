# Шаги:
# Откройте страницу https://httpbin.qa-territory.online/forms/post.
# Найдите поле ввода с названием custname.
# Введите в него ваше имя.
# Найдите кнопку Submit и нажмите на нее.
# Проверьте, что после нажатия URL изменился.

from time import sleep
from selenium.webdriver.common.by import By


def test_submit(driver):
    driver.get('https://httpbin.qa-territory.online/forms/post')
    sleep(3)

    driver.find_element(By.NAME, 'custname').send_keys('Karina')

    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    sleep(3)

    expected_url = 'https://httpbin.qa-territory.online/post'

    assert driver.current_url == expected_url
