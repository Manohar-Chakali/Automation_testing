from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class My_Account_page:
    drp_myAccount_xpath = "//span[normalize-space()='My Account']"
    btn_logout_xpath = "//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Logout']"
    btn_lgout_inside_myacc_xpath = "//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Logout']"
    txt_logout_outside_myacc_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def click_logout(self):
        logout_btn = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.btn_logout_xpath)))
        logout_btn.click()

    def click_myaccount(self):
        my_account = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.drp_myAccount_xpath)))
        my_account.click()
    def is_logout_visible(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self. btn_lgout_inside_myacc_xpath)))
            return True # Logout is visible
        except:
            return False # Logout not found (session not maintained)
    def is_logout_appeared_at_homepage(self):
        try:
            is_logout_visible = WebDriverWait(self.driver, timeout=5).until(EC.presence_of_element_located((By.LINK_TEXT, self.txt_logout_outside_myacc_linktext)))
            return is_logout_visible.is_displayed()
        except:
            return False



