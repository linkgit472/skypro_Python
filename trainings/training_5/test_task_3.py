# Откройте страницу: demoqa.com/radio-button
# Проверьте состояние радиокнопки Yes:
# Что она отображается на странице.
# Что она доступна для взаимодействия.

from time import sleep
from selenium.webdriver.common.by import By


def test_displayed_radio_button(driver):
    driver.get('https://demoqa.com/radio-button')
    sleep(5)

    displayed = driver.find_element(By.ID, "yesRadio").is_displayed()

    assert displayed is True


def test_enabled_radio_button(driver):
    driver.get('https://demoqa.com/radio-button')
    sleep(5)

    enabled = driver.find_element(By.ID, "yesRadio").is_enabled()

    assert enabled is True
