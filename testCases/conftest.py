import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

# Fixture to set up the browser based on input argument
@pytest.fixture()
def setup(request):
    browser = request.config.getoption("--browser")  # Get the browser argument from the command line
    print(f"Selected Browser: {browser}")  # Log the selected browser

    # Initialize the WebDriver based on the argument passed
    if browser.lower() == 'edge':
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
    elif browser.lower() == 'firefox':
        service = FirefoxService(GeckoDriverManager().install())  # Correct Firefox service initialization
        driver = webdriver.Firefox(service=service)  # Initialize Firefox browser
    else:
        service = ChromeService(ChromeDriverManager().install())  # Correct Chrome service initialization
        driver = webdriver.Chrome(service=service)

    # Maximize window
    driver.maximize_window()

    yield driver  # Return the driver instance to the test function

    # Teardown: Close the browser after the test is done
    driver.quit()


# Adding a command line option for browser selection
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Chrome", help="Choose browser: Chrome, Firefox, Edge")
