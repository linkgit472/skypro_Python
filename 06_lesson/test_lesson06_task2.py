# Работа с cookie

# Предварительные шаги
# Создано два аккаунта на https://gitflic.ru/.

# Шаги
# Откройте страницу https://gitflic.ru/.
# Установите cookie пользователя 1.
# Обновите страницу.
# Перейдите на страницу пользователя 1.
# Сохраните текущий URL.
# Разлогиньтесь (очистите куки).
# Установите cookie пользователя 2.
# Обновите страницу.
# Перейдите на страницу пользователя 2.
# Сохраните текущий URL.
# Проверьте, что URL для пользователя 1 и пользователя 2 различаются.

from selenium.webdriver.common.by import By


def test_urls(driver):
    driver.get("https://gitflic.ru/")

    driver.add_cookie({
        "name": "SESSION",
        "value": "M2ZiMDQ5Y2ItMTUwNy00NjQ3LThmY2QtMTE4ZTQzZjY2Nzcw",
        "domain": "gitflic.ru"
        })
    driver.refresh()

    user_icon = driver.find_element(By.XPATH, "//img[@class='rounded-circle']")
    user_icon.click()
    url_1 = driver.current_url

    driver.delete_all_cookies()

    driver.get('https://gitflic.ru/')
    driver.add_cookie({
        "name": "SESSION",
        "value": "N2Y5OTBlODQtMTA5My00NDY4LWFlY2ItN2NmYmFhNDg1YTE4",
        "domain": "gitflic.ru"
        })
    driver.refresh()

    url_2 = driver.current_url

    assert url_1 != url_2
