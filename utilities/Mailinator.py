
from selenium import webdriver
from selenium.webdriver.common.by import By
from testCases.conftest import setup


def get_mail(setup):
    url = "https://www.mailinator.com/"
    driver = setup()
    driver.get(url)
    driver.find_element(By.XPATH,"//a[@class='inbox-link']").click()
    driver.find_element(By.XPATH,"//input[@id='inbox_field']").send_keys("ndj@mailinator.com")
    driver.find_element(By.XPATH,"//button[normalize-space()='GO']").click()
