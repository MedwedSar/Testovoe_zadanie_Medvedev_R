
from Configs.Selenium_config import CONF
from models.SeleniumObjectModels.GoogleMainPage import GoogleMainPage
from models.SeleniumObjectModels.RamblerMainPage import RamblerMainPage
from models.SeleniumObjectModels.RamblerLoginMailPage import RamblerLoginMailPage


def test_check_login_rambler(web_rambler):
    """
        Test: Check login in mail Rambler.
    """

    RamblerMainPage(web_rambler).login_mail_get_element().click()
    RamblerLoginMailPage(web_rambler).login(CONF.login_mail, CONF.passwd_mail)

    assert RamblerMainPage(web_rambler).login_mail_get_element().text == 'autotestermr@rambler.ru', \
        'Incorrect value in mail'


def test_check_search_google(web_google):
    """
        Test: Check search value in google
    """

    GoogleMainPage(web_google).search_window().send_keys('купить кофемашину bork c804')
    GoogleMainPage(web_google).search_window().submit()

    text_fined_value = GoogleMainPage(web_google).search_all_result().text
    assert 'https://www.mvideo.ru' in text_fined_value, 'Expected value not founded in results'
    assert len(GoogleMainPage(web_google).search_all_results_list()) == 10, 'Incorrect count founded elements'
    assert GoogleMainPage(web_google).get_results_count() > 10, 'Incorrect count founded values'
