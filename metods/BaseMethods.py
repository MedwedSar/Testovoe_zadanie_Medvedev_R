from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Configs.Selenium_config import CONF


class BaseMethods:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=CONF.time_wait):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator),
                                                      message=f"Locator with name={locator} not found")

    def switch_to_iframe(self, locator, time=CONF.time_wait):
        return WebDriverWait(self.driver, time).until(ec.frame_to_be_available_and_switch_to_it(locator),
                                                      message=f"Locator with name={locator} not found")

    def wait_disappear_element(self, locator, time=CONF.time_wait):
        return WebDriverWait(self.driver, time).until(ec.invisibility_of_element_located(locator),
                                                      message=f'Locator with name={locator} present in page')

    def find_elements(self, locator, time=CONF.time_wait):
        return WebDriverWait(self.driver, time).until(ec.presence_of_all_elements_located(locator),
                                                      message=f"Locators with name={locator} present in page")

    def default_content_iframe(self):
        self.driver.switch_to.default_content()
