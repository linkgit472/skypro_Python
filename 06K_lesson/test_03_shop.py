# Откройте сайт магазина: https://www.saucedemo.com/ в FireFox.
# Авторизуйтесь как пользователь standard_user.
# Добавьте в корзину товары:
# Sauce Labs Backpack.
# Sauce Labs Bolt T-Shirt.
# Sauce Labs Onesie.
# Перейдите в корзину.
# Нажмите Checkout.
# Заполните форму своими данными.
# Нажмите кнопку Continue.
# Прочитайте со страницы итоговую стоимость ( Total).
# Закройте браузер.
# Проверьте, что итоговая сумма равна $58.29.

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_total(driverFireFox):
    driverFireFox.get("https://www.saucedemo.com/")
    WebDriverWait(driverFireFox, 15)
    driverFireFox.find_element(By.CSS_SELECTOR,
                               "#user-name").send_keys("standard_user")
    driverFireFox.find_element(By.CSS_SELECTOR,
                               "#password").send_keys("secret_sauce")
    driverFireFox.find_element(By.CSS_SELECTOR, "#login-button").click()

    driverFireFox.find_element(By.CSS_SELECTOR,
                               "#add-to-cart-sauce-labs-backpack").click()
    driverFireFox.find_element(By.CSS_SELECTOR,
                               "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driverFireFox.find_element(By.CSS_SELECTOR,
                               "#add-to-cart-sauce-labs-onesie").click()

    driverFireFox.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
    driverFireFox.find_element(By.CSS_SELECTOR, "#checkout").click()

    driverFireFox.find_element(By.ID, "first-name").send_keys("Karina")
    driverFireFox.find_element(By.ID, "last-name").send_keys("Egelman")
    driverFireFox.find_element(By.ID, "postal-code").send_keys("235300")
    driverFireFox.find_element(By.ID, "continue").click()

    total = WebDriverWait(driverFireFox,
                          10).until(EC.presence_of_element_located(
                              (By.CSS_SELECTOR, ".summary_total_label")))
    assert '$58.29' in total.text, f"Ошибка! {total.text}"
