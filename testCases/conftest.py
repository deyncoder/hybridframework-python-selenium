from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):

    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching chrome browser...")
    elif browser =='edge':
        driver = webdriver.Edge()
        print("Launching internet explorer browser...")
    else:                                                       # setting up default browser in case none is specified
        driver = webdriver.Chrome()
        print("Launching chrome browser...")
    return driver


def pytest_addoption(parser):     # this will get value from CLI
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): # this will return browser value to setup method
    return request.config.getoption("--browser")

############### PyTest HTML REPORT ########################

# Hook for adding environment info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'hybridframework-python-selenium'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'DM'

# Hook for delete/modify environment info to HTML report
@pytest.mark.optionalhook
def pytest_metada(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

