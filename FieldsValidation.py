import pytest
from selenium import webdriver

import time

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options

from PageObject.GoogleForm import GoogleForm
from Resources.resources import __google_form_url



@pytest.fixture(scope = 'module')
def run_chrome():
    print('setup fixture')
    #options = Options()
    #options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
    #driver = webdriver.Chrome(chrome_options=options)

    #FIREFOX
    cap = DesiredCapabilities().FIREFOX
    cap["marionette"] = True
    opt = Options()
    opt.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    driver = webdriver.Firefox(capabilities=cap, firefox_options=opt)
    google = GoogleForm(driver)
    google.driver.get(__google_form_url)
    yield google
    driver.close()


@pytest.mark.parametrize('email', ['test@gmail.com', 'quitealongnameofemail@yahoo.com', 'gmail@qc.eu'])
def test_email_field_positive(run_chrome, email):
    run_chrome.clear_email_field()
    run_chrome.fill_email_field(email)
    assert run_chrome.email_exception_field().is_displayed() is False


email_data_negative = ['test@gmail', '@gmail', 'gmail.com', '@com.com', '', 'w@test.c']

@pytest.mark.parametrize('email', email_data_negative)
def test_email_field_negative(run_chrome, email):
    run_chrome.clear_email_field()
    run_chrome.fill_email_field(email)
    assert run_chrome.email_exception_field().text == u'Потрібна дійсна електронна адреса'


def test_empty_email_field(run_chrome):
    run_chrome.clear_email_field()
    run_chrome.fill_email_field(' ')
    assert run_chrome.email_exception_field().text == u'Відповідь на це запитання обов’язкова'


@pytest.mark.parametrize('date', [('01', '05', '1867'), ('31', '03', '2017'), ('05', '01', '1999'), ('29', '02', '2016')])
def test_positive_born_date(run_chrome, date):
    run_chrome.empty_date_field()
    run_chrome.day_field().send_keys(date[0])
    run_chrome.month_field().send_keys(date[1])
    run_chrome.year_field().send_keys(date[2])
    assert run_chrome.date_exception_field().is_displayed() is False


@pytest.mark.parametrize('date', [('00', '05', '1867'), ('06', '13', '2017'), ('31', '11', '1999'), ('32', '12', '2000'), ('29', '02', '2017')])
def test_negative_born_date(run_chrome, date):
    run_chrome.empty_date_field()
    run_chrome.day_field().send_keys(date[0])
    run_chrome.month_field().send_keys(date[1])
    run_chrome.year_field().send_keys(date[2])
    assert run_chrome.date_exception_field().text == u'Недійсна дата'


@pytest.mark.skip(reason="works incorrect via test but works ok manually")
def test_empty_born_date(run_chrome):
    run_chrome.empty_date_field()
    time.sleep(4)
    assert run_chrome.date_exception_field().text == u'Відповідь на це запитання обов’язкова'


_name_pos = ['Hellomynameisdenys J', 'R_1', 'E. Harry', '!@#$%^&*()_']

@pytest.mark.parametrize('name', _name_pos)
def test_name_field_positive(run_chrome, name):
    run_chrome.clear_name_field()
    run_chrome.fill_name_field(name)
    assert run_chrome.name_exception_field().is_displayed() is False, 'Field\'s boundary values are incorrect'

_name_neg = ['Hellomynameisdenys Jr']

@pytest.mark.parametrize('name', _name_neg)
def test_name_field_above_limit(run_chrome, name):
    run_chrome.clear_name_field()
    run_chrome.fill_name_field(name)
    assert run_chrome.name_exception_field().text == u'Максимальное количество символов 20 превышено'


def test_name_field_empty(run_chrome):
    run_chrome.clear_name_field()
    run_chrome.fill_name_field(' ')
    assert run_chrome.name_exception_field().text == u'Відповідь на це запитання обов’язкова'

@pytest.mark.skip(reason="sex deleted")
@pytest.mark.parametrize('option', ['Мужской', 'Женский', 'Другой'])
def test_sex_field_options(run_chrome, option):
    run_chrome.select_sex_option(option)
    time.sleep(2)
    return
