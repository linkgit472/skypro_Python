# Ожидание появления динамического контента
# Шаги:
# Откройте страницу https://the-internet.herokuapp.com/dynamic_controls.
# Нажмите кнопку Remove.
# Дождитесь появления текста It's gone!
# Нажмите кнопку Enable.
# Дождитесь, когда поле ввода станет активным.
# Проверьте, что поле действительно стало активным.

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_remove_bt(driver, wait):
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")

    remove_bt = driver.find_element(By.CSS_SELECTOR,
                                    '[onclick="swapCheckbox()"]')
    remove_bt.click()

    execpted_text = "It's gone!"
    result = wait.until(EC.visibility_of_element_located((By.ID, 'message')))
    assert result.text == execpted_text, "Сообщение 'It's gone! не появилось"


def test_enble_field(driver, wait):
    enable_bt = driver.find_element(By.CSS_SELECTOR, '[onclick="swapInput()"]')
    enable_bt.click()

    text_field = wait.until(EC.element_to_be_clickable
                            ((By.CSS_SELECTOR, '[type="text"]')))
    assert text_field.is_enabled(), 'Поле неактивно'

    expected_text = 'Текст написался'
    text_field.send_keys(expected_text)
    assert text_field.get_attribute
    ('value') == expected_text, 'Текст не ввелся в поле'
