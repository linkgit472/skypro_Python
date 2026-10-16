# Тест 1. Функциональность поиска
# Цель: написать автотест для проверки функциональности поиска на
# сайте https://www.google.com/, используя паттерн Page Object.

# Шаги
# Создать класс Page Object для главной страницы сайта,
# который будет содержать методы для взаимодействия с элементами поиска
# и получения результатов.
# Написать тест, который использует Page Object для выполнения поиска
# и проверки результатов.
from page_main import GoogleMainPage


def test_search(driver):
    page = GoogleMainPage(driver)
    page.enter_search_query('кошки')
    results = page.get_search_result()

    assert len(results) > 0, 'Результаты поиска не найдены'
