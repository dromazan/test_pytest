import pytest
from selenium import webdriver
import sys
import time
import pytest_variables
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from PageObject.GoogleForm import GoogleForm
from Resources.resources import __google_form_url
import logging
logging.basicConfig(filename="log.txt", level=logging.INFO)

@pytest.fixture(scope='module')
def run_browser(variables):
    browser = variables['capabilities']['browser']
    print(browser)
    if browser == 'Chrome':
        print('using chrome driver')
        from selenium.webdriver.chrome.options import Options
        options_chrome = Options()
        options_chrome.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        driver = webdriver.Chrome(chrome_options=options_chrome)

    elif browser == 'Firefox':
        print('using firefox driver')
        from selenium.webdriver.firefox.options import Options
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = True
        options_ff = Options()
        options_ff.binary_location = 'C:\\Users\\droma\\Downloads\\firefox\\firefox.exe'
        driver = webdriver.Firefox(capabilities=cap, executable_path="C:\\Users\\droma\\Documents\\geckodriver\\geckodriver.exe", firefox_options=options_ff)

    elif browser == 'Edge':
        print('using edge driver')
        from selenium.webdriver.edge.options import Options
        driver = webdriver.Edge(executable_path="Z:\\edgedriver\\MicrosoftWebDriver.exe")

    # Default browser is Chrome
    else:
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        driver = webdriver.Chrome(chrome_options=options)

    google = GoogleForm(driver)
    google.driver.get(__google_form_url)
    yield google
    driver.close()


@pytest.mark.parametrize('email', ['test@gmail.com', 'quitealongnameofemail@yahoo.com', 'gmail@qc.eu'])
def test_email_field_positive(run_browser, email):
    run_browser.clear_email_field()
    run_browser.fill_email_field(email)
    assert run_browser.email_exception_field().is_displayed() is False


email_data_negative = ['test@gmail', '@gmail', 'gmail.com', '@com.com', '', 'w@test.c']

@pytest.mark.parametrize('email', email_data_negative)
def test_email_field_negative(run_browser, email):
    run_browser.clear_email_field()
    run_browser.fill_email_field(email)
    assert run_browser.email_exception_field().text == u'Потрібна дійсна електронна адреса'


def test_empty_email_field(run_browser):
    run_browser.clear_email_field()
    run_browser.fill_email_field(' ')
    assert run_browser.email_exception_field().text == u'Відповідь на це запитання обов’язкова'


@pytest.mark.parametrize('date', [('01', '05', '1867'), ('31', '03', '2017'), ('05', '01', '1999'), ('29', '02', '2016')])
def test_positive_born_date(run_browser, date):
    run_browser.empty_date_field()
    run_browser.day_field().send_keys(date[0])
    run_browser.month_field().send_keys(date[1])
    run_browser.year_field().send_keys(date[2])
    assert run_browser.date_exception_field().is_displayed() is False


@pytest.mark.parametrize('date', [('00', '05', '1867'), ('06', '13', '2017'), ('31', '11', '1999'), ('32', '12', '2000'), ('29', '02', '2017')])
def test_negative_born_date(run_browser, date):
    run_browser.empty_date_field()
    run_browser.day_field().send_keys(date[0])
    run_browser.month_field().send_keys(date[1])
    run_browser.year_field().send_keys(date[2])
    assert run_browser.date_exception_field().text == u'Недійсна дата'


@pytest.mark.skip(reason="works incorrect via test but works ok manually")
def test_empty_born_date(run_browser):
    run_browser.empty_date_field()
    time.sleep(4)
    assert run_browser.date_exception_field().text == u'Відповідь на це запитання обов’язкова'


_name_pos = ['Hellomynameisdenys J', 'R_1', 'E. Harry', '!@#$%^&*()_']

@pytest.mark.parametrize('name', _name_pos)
def test_name_field_positive(run_browser, name):
    run_browser.clear_name_field()
    run_browser.fill_name_field(name)
    assert run_browser.name_exception_field().is_displayed() is False, 'Field\'s boundary values are incorrect'

_name_neg = ['Hellomynameisdenys Jr']

@pytest.mark.parametrize('name', _name_neg)
def test_name_field_above_limit(run_browser, name):
    run_browser.clear_name_field()
    run_browser.fill_name_field(name)
    assert run_browser.name_exception_field().text == u'Максимальное количество символов 20 превышено'


def test_name_field_empty(run_browser):
    run_browser.clear_name_field()
    run_browser.fill_name_field(' ')
    assert run_browser.name_exception_field().text == u'Відповідь на це запитання обов’язкова'

@pytest.mark.skip(reason="sex deleted")
@pytest.mark.parametrize('option', ['Мужской', 'Женский', 'Другой'])
def test_sex_field_options(run_browser, option):
    run_browser.select_sex_option(option)
    time.sleep(2)
    return
