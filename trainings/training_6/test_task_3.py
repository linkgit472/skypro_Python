# Ожидание AJAX-контента и выполнение JavaScript
# Шаги:
# Откройте страницу https://the-internet.herokuapp.com/dynamic_loading/2.
# Нажмите кнопку Start.
# Дождитесь появления текста Hello World!
# Используйте JavaScript для получения текста элемента.
# Проверьте, что текст равен Hello World!
# Проверьте, что элемент видим и содержит правильный текст.

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_text_visible(driver, wait):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    start_bt = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "div[id='start'] button")))
    start_bt.click()

    hello_world = wait.until(EC.visibility_of_element_located(
        ((By.ID, 'finish'))))
    text_hello_world = driver.execute_script("return arguments[0].textContent;", hello_world)

    assert text_hello_world == "Hello World!", "Текст не 'Hello World!'"


def test_hello_world_visible(wait):
    hello_world = wait.until(EC.visibility_of_element_located(
        ((By.ID, 'finish'))))

    assert hello_world.is_displayed(), 'Текст не виден на экране'
    assert 'Hello World!' in hello_world.text, 'Видимый элемент не содержит текст "Hello World!"'
