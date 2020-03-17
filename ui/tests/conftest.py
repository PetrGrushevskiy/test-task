import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ui.pages.app import Application


@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(120)
    yield driver
    driver.close()


@pytest.fixture(scope="session")
def app(driver):
    return Application(driver)
