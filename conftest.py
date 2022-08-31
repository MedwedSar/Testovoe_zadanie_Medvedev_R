import pytest
from selenium import webdriver
from Configs.Selenium_config import CONF


@pytest.fixture(scope="session")
def web_rambler():
    """
        This fixture open web driver chrome end go to start page Rambler.
    """
    driver = webdriver.Chrome(executable_path=CONF.chrome_driver_locate)
    driver.get(CONF.start_url_Rambler)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def web_google():
    """
        This fixture open web driver chrome end go to start page Google.
    """
    driver = webdriver.Chrome(executable_path=CONF.chrome_driver_locate)
    driver.get(CONF.start_url_Google)
    yield driver
    driver.quit()
