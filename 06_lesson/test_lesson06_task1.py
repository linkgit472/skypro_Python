# Ожидание динамической загрузки данных

# Шаги:
# Откройте страницу https://the-internet.herokuapp.com/dynamic_loading/2.
# Найдите и нажмите на кнопку Start.
# Дождитесь появления текста Hello World!
# Сделайте скриншот страницы.
# Проверьте, что появившийся текст равен Hello World!

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_hello_world(driver, wait):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')

    driver.find_element(By.CSS_SELECTOR, "div[id='start'] button").click()

    text_hello_world = wait.until(EC.visibility_of_element_located(
        (By.ID, 'finish')))
    driver.save_screenshot('06_lesson/screenshot/text_hello_world.png')

    assert text_hello_world.text == 'Hello World!', 'Текст на экране не Hello World!'
