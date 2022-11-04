import os
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="edge", help="browser to open"
    )
    parser.addoption(
        "--drivers_source", default="C:\selenium_drivers", help="Source where drivers exists"
    )
    parser.addoption(
        "--headless", action="store_true", help="browser to open"
    )
    parser.addoption(
        "--base_url", default="http://192.168.7.181:8081/", help="Service url"
    )


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    drivers_folder = request.config.getoption("--drivers_source")
    headless = request.config.getoption("--headless")
    base_url = request.config.getoption("--base_url")
    if browser_name == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        if headless:
            chrome_options.headless = True
        _driver = webdriver.Chrome(executable_path=os.path.join(drivers_folder, 'chromedriver.exe'),
                                   options=chrome_options)
    elif browser_name == 'edge':
        _driver = webdriver.Edge(executable_path=os.path.join(drivers_folder, 'msedgedriver.exe'))
    else:
        raise ValueError(f'Browser {browser_name} is not supported.')
    _driver.base_url = base_url
    yield _driver
    _driver.close()
