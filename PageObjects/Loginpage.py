from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:
    txt_email_xpath = "//input[@id='input-email']"
    txt_password_xpath = "//input[@id='input-password']"
    btn_login_xpath = "//input[@value='Login']"
    txt_login_cnf_msg_xpath = "//h2[normalize-space()='My Account']"

    def __init__(self, driver):
        self.driver = driver

    def click_email(self,email):
        email_field = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, self.txt_email_xpath)))
        email_field.send_keys(email)
    def click_password(self,password):
        password_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.txt_password_xpath)))
        password_field.send_keys(password)
    def click_login(self):
        login_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.btn_login_xpath)))
        login_button.click()
    def myaccount_page(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.txt_login_cnf_msg_xpath)))

