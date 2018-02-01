import optparse

parser = optparse.OptionParser()


def pytest_addoption(parser):
    parser.addoption('--browser', action="store", default="Chrome")


def _browser(request):
    print(request.config.getoption("--browser"))
    return request.config.getoption("--browser")
