import os.path

from PageObjects.Homepage import Homepage
from PageObjects.Registrationpage import Registration
from utilities.customlogger import LogGen
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
from utilities.randomstring import random_string_generator
import time
import os

class Test_001_AccountReg:
    baseUrl = "https://naveenautomationlabs.com/opencart/"
    logger = LogGen.loggen()

    def test_account_reg(self, setup):
        # Log the start of the test case
        self.logger.info("**** Starting test_account_reg ****")

        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        # Log the navigation step
        self.logger.debug("**** Navigating to My Account and Register ****")
        self.hp = Homepage(self.driver)

        try:
            # Clicking 'My Account' and 'Register'
            self.hp.clickmyaccount()
            self.logger.debug("**** Clicking My Account ****")
            time.sleep(2)
            self.hp.clickregister()
            self.logger.debug("**** Clicking Register ****")
        except Exception as e:
            self.logger.error(f"Error during navigation: {e}")
            self.driver.quit()
            assert False

        # Log when reaching the registration page
        self.logger.debug("**** Reached Registration Page ****")
        self.repage = Registration(self.driver)

        try:
            # Fill out the registration form
            self.repage.clickfirstname()
            self.logger.debug("**** First Name clicked ****")
            self.repage.clicklastname()
            self.logger.debug("**** Last Name clicked ****")
            self.email = random_string_generator()+'@gamil.com'
            self.repage.clickemail(self.email)
            self.logger.debug("**** Email clicked ****")
            self.repage.clicktelephone()
            self.logger.debug("**** telephone clicked ****")
            self.repage.clickpassword()
            self.logger.debug("**** Password clicked ****")
            self.repage.clickcnfpassword()
            self.logger.debug("**** confirm password clicked")
            self.repage.clickagreebtn()
            self.logger.debug("**** Privacy Policy clicked ****")
            self.repage.clickcontinuebtn()
            self.logger.debug("**** continue button clicked")
        except Exception as e:
            self.logger.error(f"Error during form submission: {e}")
            # # Capture screenshot before quitting
            # screenshots_dir = os.path.join(os.path.abspath(os.curdir), "screenshots")
            # if not os.path.exists(screenshots_dir):
            #     os.makedirs(screenshots_dir)
            # screenshot_path = os.path.join(screenshots_dir, "error.png")
            # self.driver.save_screenshot(screenshot_path)
            # self.logger.error(f"Screenshot saved to {screenshot_path}")
            self.driver.quit()
            assert False

        # Log the confirmation message
        self.cnfmessage = self.repage.getsuccessmessage()
        self.logger.info(f"**** Confirmation message: {self.cnfmessage} ****")

        # Log the test result and close the browser
        self.driver.close()

        # Assert based on the confirmation message
        if self.cnfmessage == "Your Account Has Been Created!":
            self.logger.info("**** Account creation successful ****")
            assert True
            self.driver.close()
        else:
            self.logger.error("**** Account creation failed ****")
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "error.png")
            self.driver.close()
            assert False
