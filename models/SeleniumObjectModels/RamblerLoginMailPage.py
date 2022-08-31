from metods.BaseMethods import BaseMethods
from selenium.webdriver.common.by import By


css = By.CSS_SELECTOR


class RamblerLoginMailLocators:
    login_str = (css, '[id="login"]')
    password_str = (css, '[id="password"]')
    enter_button = (css, '[class="rui-Button-content"]')
    iframe = (css, '[data-id-frame="own"] iframe')


class RamblerLoginMailPage(BaseMethods):

    def login(self, login, password):
        self.switch_to_iframe(RamblerLoginMailLocators.iframe)
        element = self.find_element(RamblerLoginMailLocators.login_str)
        element.send_keys(login)
        element = self.find_element(RamblerLoginMailLocators.password_str)
        element.send_keys(password)
        element = self.find_element(RamblerLoginMailLocators.enter_button)
        element.click()
        self.default_content_iframe()
        self.wait_disappear_element(RamblerLoginMailLocators.iframe)
