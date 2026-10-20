import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session')
def driver():
    options = Options()

    options.add_experimental_option("prefs", {
        "profile.password_manager_enabled": False,
        "credentials_enable_service": False
    })

    driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()
