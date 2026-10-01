# Откройте страницу: httpbin.qa-territory.online/forms/post
# Заполните поле custname значением «Иван Иванов»
# Нажмите кнопку Submit

from time import sleep
from selenium.webdriver.common.by import By


def test_submit(driver):
    driver.maximize_window()
    driver.get('https://httpbin.qa-territory.online/forms/post')
    sleep(5)

    driver.find_element(By.CSS_SELECTOR, '[name="custname"]'
                        ).send_keys("Иван Иванов")
    sleep(3)

    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    sleep(3)

    result = driver.find_element(By.CSS_SELECTOR, 'p').text

    assert result == 'Form submitted successfully.'
