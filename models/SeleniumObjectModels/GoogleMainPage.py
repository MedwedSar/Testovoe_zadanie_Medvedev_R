import re

from metods.BaseMethods import BaseMethods
from selenium.webdriver.common.by import By


css = By.CSS_SELECTOR


class GoogleMainLocators:
    search_window = (css, '[name="q"]')
    all_result_search = (css, '[id="rso"]')
    result_search = (css, '[class="MjjYud"]')
    result_count = (css, '[id="result-stats"]')


class GoogleMainPage(BaseMethods):

    def search_window(self) -> object:
        return self.find_element(GoogleMainLocators.search_window)

    def search_all_result(self) -> object:
        return self.find_element(GoogleMainLocators.all_result_search)

    def search_all_results_list(self) -> list:
        return self.find_elements(GoogleMainLocators.result_search)

    def get_results_count(self) -> int:
        element = self.find_element(GoogleMainLocators.result_count)
        value = element.text
        value = re.findall('\d+', value.replace(' ', ''))
        return int(value[0])



