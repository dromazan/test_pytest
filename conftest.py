import optparse
import pytest

parser = optparse.OptionParser()


def pytest_addoption(parser):
    parser.addoption('--browser', action="store", default="Chrome")


def _browser(request):
    return request.config.getoption("--browser")