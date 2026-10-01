import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.google.com/')

    yield driver
    driver.quit()
