import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from PageObject.GoogleForm import GoogleForm
from Resources.resources import *


@pytest.yield_fixture(scope='module')
def run_browser(browser):
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
        #options_ff.binary_location = ff_binary_path
        driver = webdriver.Firefox(capabilities=cap, executable_path=gecko_path, firefox_options=options_ff)

    elif browser == 'Edge':
        print('using edge driver')
        from selenium.webdriver.edge.options import Options
        driver = webdriver.Edge(executable_path="Z:\\edgedriver\\MicrosoftWebDriver.exe")

    # Default browser is Chrome
    else:
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        driver = webdriver.Chrome(chrome_options=options, executable_path=chdriver_path)

    google = GoogleForm(driver)
    google.driver.get(google_form_url)
    yield google
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
