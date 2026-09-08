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


def test_urls(driver):
    driver.get("https://gitflic.ru/")

    driver.add_cookie({
        "name": "SESSION",
        "value": "MmJiZTBjNzUtNmVmOC00MzRhLWI4MjgtYWNkYWQ4NDU2MWEw",
        "domain": "gitflic.ru"
        })
    driver.refresh()

    driver.get('https://gitflic.ru/user/karina-hanmun')
    url_1 = driver.current_url

    driver.delete_all_cookies()

    driver.add_cookie({
        "name": "SESSION",
        "value": "MDUzNGY4NTctOTZlNi00NTJjLTkwZDEtOGJmMDFiMWYwOTFj",
        "domain": "gitflic.ru"
        })
    driver.refresh()

    driver.get('https://gitflic.ru/user/link-gensh')
    url_2 = driver.current_url

    assert url_1 != url_2
