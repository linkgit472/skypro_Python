# Работа с модальными окнами и ожидание
# Шаги:
# Откройте страницу https://the-internet.herokuapp.com/entry_ad.
# Дождитесь появления модального окна.
# Проверьте, что в модальном окне есть текст This is a modal window.
# Закройте модальное окно.
# Проверьте, что модальное окно исчезло.
# Проверьте, что основной контент страницы виден.

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_modal_window_text(driver, wait):
    driver.get("https://the-internet.herokuapp.com/entry_ad")
    modal_window = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "modal"))
    )
    assert modal_window.is_displayed(), "Модальное окно не отобразилось"

    modal_text = driver.find_element(By.CSS_SELECTOR, ".modal-title")
    assert 'this is a modal window' in modal_text.text.lower(), 'В модальном окне нет текста "This is a modal window"'


def test_modal_window_close(driver, wait):
    modal_window_close = driver.find_element(By.CSS_SELECTOR, '.modal-footer p')
    modal_window_close.click()

    modal_is_hidden = wait.until(EC.invisibility_of_element_located(
        (By.CSS_SELECTOR, ".modal")))
    assert modal_is_hidden, "Модальное окно отображается"


def test_content_visibility(wait):
    content = wait.until(EC.visibility_of_element_located((By.ID, 'content')))
    assert content.is_displayed(), 'Контент не виден'
