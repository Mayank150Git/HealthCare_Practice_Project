import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_type", action="store", default="Chrome", help="If no value is passed then the Automation will happen using Chrome Browser"
    )


@pytest.fixture(scope = "class")
def setup(request):
    browser = request.config.getoption("--browser_type")
    if browser == "Chrome":
        Service_Object = Service()
        driver = webdriver.Chrome(service=Service_Object)
        driver.get("https://katalon-demo-cura.herokuapp.com/")
        driver.maximize_window()
        request.cls.driver = driver
        yield
        driver.close()
    elif browser == "Firefox":
        Service_Object = Service()
        driver = webdriver.Firefox(service=Service_Object)
        driver.get("https://katalon-demo-cura.herokuapp.com/")
        driver.maximize_window()
        request.cls.driver = driver
        yield
        driver.close()

