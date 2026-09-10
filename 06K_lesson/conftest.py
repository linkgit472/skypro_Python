import pytest
from selenium import webdriver


@pytest.fixture(scope='module')
def driverEdge():
    driver = webdriver.Edge()

    yield driver
    driver.quit()


@pytest.fixture(scope='module')
def driverChrome():
    driver = webdriver.Chrome()

    yield driver
    driver.quit()


@pytest.fixture(scope='module')
def driverFireFox():
    driver = webdriver.Firefox()

    yield driver
    driver.quit()
