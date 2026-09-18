# Задание:
# Откройте страницу https://httpbin.qa-territory.online/links/10.
# Найдите все ссылки на странице (тег <a>).
# Проверьте, что количество ссылок равно 9.
# Проверьте, что все ссылки отображаются на странице.
# Проверьте, что текст первой ссылки содержит "1".

from time import sleep
from selenium.webdriver.common.by import By


def test_links_count(driver):
    driver.get("https://httpbin.qa-territory.online/links/10")
    sleep(3)

    links = driver.find_elements(By.TAG_NAME, "a")

    assert len(links) == 9


def test_links_displayed(driver):
    links = driver.find_elements(By.TAG_NAME, "a")
    visible_link = 0

    for i in links:
        if i.is_displayed():
            visible_link += 1

    assert visible_link == len(links)


def test_first_links(driver):
    first_link_text = driver.find_element(By.TAG_NAME, "a").text
    expected_text = "1"

    assert expected_text in first_link_text
