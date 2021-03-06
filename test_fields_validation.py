import pytest
import time

import logging
logging.basicConfig(filename="log.txt", level=logging.INFO)


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
    assert run_browser.email_exception_field().text == u'Must be a valid email address'


def test_empty_email_field(run_browser):
    run_browser.clear_email_field()
    run_browser.fill_email_field(' ')
    assert run_browser.email_exception_field().text == u'This is a required question'


@pytest.mark.parametrize('date', [('01', '05', '1867'), ('31', '03', '2017'), ('05', '01', '1999'), ('29', '02', '2016')])
@pytest.mark.skipped(reason="""
Google made some changes into Forms:
selenium.common.exceptions.InvalidElementStateException: 
Message: invalid element state: Element is not currently interactable and may not be manipulated
""")
def test_positive_born_date(run_browser, date):
    run_browser.empty_date_field()
    run_browser.day_field().send_keys(date[0])
    run_browser.month_field().send_keys(date[1])
    run_browser.year_field().send_keys(date[2])
    assert run_browser.date_exception_field().is_displayed() is False


@pytest.mark.parametrize('date', [('00', '05', '1867'), ('06', '13', '2017'), ('31', '11', '1999'), ('32', '12', '2000'), ('29', '02', '2017')])
@pytest.mark.skipp(reason="""
Google made some changes into Forms:
selenium.common.exceptions.InvalidElementStateException: 
Message: invalid element state: Element is not currently interactable and may not be manipulated
""")
def test_negative_born_date(run_browser, date):
    run_browser.empty_date_field()
    # run_browser.date_field_chrome.send_keys('%s-%s-%s' % (date[2], date[0], date[1]))
    run_browser.day_field().send_keys(date[0])
    run_browser.month_field().send_keys(date[1])
    run_browser.year_field().send_keys(date[2])
    assert run_browser.date_exception_field().text == u'Недійсна дата'


@pytest.mark.skip(reason="works incorrect via test but works ok manually")
def test_empty_born_date(run_browser):
    run_browser.empty_date_field()
    time.sleep(4)
    assert run_browser.date_exception_field().text == u'This is a required question'


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
    assert run_browser.name_exception_field().text == u'Maximum field length 20 chars is exceeded'


def test_name_field_empty(run_browser):
    run_browser.clear_name_field()
    run_browser.fill_name_field(' ')
    assert run_browser.name_exception_field().text == u'This is a required question'


