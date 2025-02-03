import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup():
    # Initialize ChromeOptions
    options = Options()
    # options.add_argument("--headless")  # Running in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")

    service=Service(ChromeDriverManager().install())
    # Initialize the WebDriver with the options and ChromeDriverManager for the driver path
    driver = webdriver.Chrome(service=service, options=options)

    # Yield the driver to the test
    yield driver

    # Cleanup: Quit the driver after the test is done
    driver.quit()
