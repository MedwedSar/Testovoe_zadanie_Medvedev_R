from metods.BaseMethods import BaseMethods
from selenium.webdriver.common.by import By


css = By.CSS_SELECTOR


class RamblerMainLocators:
    enter_to_mail = (css, '[class="rui__2FTrL"]')


class RamblerMainPage(BaseMethods):

    def login_mail_get_element(self) -> object:
        return self.find_element(RamblerMainLocators.enter_to_mail)
