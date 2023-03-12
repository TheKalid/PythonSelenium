from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=r'./utilities/geckodriver')
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


#Report

#Hook for adding environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Personal testing'
    config._metadata['Module Name'] = 'QA'
    config._metadata['Tester'] = 'Kalido'

@pytest.mark.optinalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)