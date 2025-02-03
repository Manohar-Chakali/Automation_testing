from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.customlogger import LogGen

class Homepage():
    lnk_Myaccount_xpath = "//span[normalize-space()='My Account']"
    lnk_register_xpath = "//a[normalize-space()='Register']"
    lnk_login_xpath = "//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Login']"
    logger=LogGen.loggen()

    def __init__(self, driver):
        self.driver = driver

    def clickmyaccount(self):
        # Wait for "My Account" to be clickable and click it
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.lnk_Myaccount_xpath))).click()

    def clickregister(self):
        try:
            # Log visibility and interactability status
            print(
                f"Is the element visible: {self.driver.find_element(By.XPATH, self.lnk_register_xpath).is_displayed()}")
            print(
                f"Is the element clickable: {self.driver.find_element(By.XPATH, self.lnk_register_xpath).is_enabled()}")

            # Wait and click
            register_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, self.lnk_register_xpath)))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", register_button)
            register_button.click()

        except Exception as e:
            print(f"Error during clicking register: {e}")
            self.logger.error(f"Error during clicking register: {e}")
            raise

    def clicklogin(self):
        login_lnk = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.lnk_login_xpath)))
        login_lnk.click()



