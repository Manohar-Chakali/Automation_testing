import os
import time
# from turtle import Screen

# from tomlkit import datetime
import allure
from allure_commons.types import AttachmentType

from PageObjects.Homepage import Homepage
from PageObjects.Registrationpage import Registration
from utilities.customlogger import LogGen
from utilities.randomstring import random_string_generator
from utilities.readproperties import Read_Commondata

class Test_001_AccountReg:
    baseUrl = Read_Commondata.get_App_url()
    logger = LogGen.loggen()

    def test_account_reg(self, setup):
        self.driver = setup
        try:
            # Log the start of the test case
            self.logger.info("**** Starting test_account_reg ****")

            self.driver.get(self.baseUrl)
            self.driver.maximize_window()

            # Log the navigation step
            self.logger.debug("**** Navigating to My Account and Register ****")
            self.hp = Homepage(self.driver)

            # Clicking 'My Account' and 'Register'
            self.hp.clickmyaccount()
            self.logger.debug("**** Clicking My Account ****")
            time.sleep(2)
            self.hp.clickregister()
            self.logger.debug("**** Clicking Register ****")

            # Log when reaching the registration page
            self.logger.debug("**** Reached Registration Page ****")
            self.repage = Registration(self.driver)

            # Fill out the registration form
            self.repage.clickfirstname()
            self.logger.debug("**** First Name clicked ****")
            self.repage.clicklastname()
            self.logger.debug("**** Last Name clicked ****")
            self.email = random_string_generator() + '@mailinator.com'
            self.repage.clickemail(self.email)
            allure.attach(self.driver.get_screenshot_as_png(),name='Email-added', attachment_type=AttachmentType.PNG)
            self.logger.debug("**** Email clicked ****")
            self.repage.clicktelephone()
            self.logger.debug("**** Telephone clicked ****")
            self.repage.clickpassword()
            self.logger.debug("**** Password clicked ****")
            self.repage.clickcnfpassword()
            self.logger.debug("**** Confirm password clicked ****")
            self.repage.clickagreebtn()
            self.logger.debug("**** Privacy Policy clicked ****")
            self.repage.clickcontinuebtn()
            self.logger.debug("**** Continue button clicked ****")

            # Log the confirmation message
            self.cnfmessage = self.repage.getsuccessmessage()
            self.logger.info(f"**** Confirmation message: {self.cnfmessage} ****")

            # Assert based on the confirmation message
            if self.cnfmessage == "Your Account Has Been Created!":
                self.logger.info("**** Account creation successful ****")
                assert True
            else:
                self.logger.error("**** Account creation failed ****")
                # Ensure the screenshots directory exists
                screenshots_dir = os.path.join(os.path.abspath(os.curdir), "screenshots")
                if not os.path.exists(screenshots_dir):
                    os.makedirs(screenshots_dir)
                self.driver.save_screenshot(os.path.join(screenshots_dir, "error1.png"))
                assert False

        except Exception as e:
            self.logger.error(f"Error during the test: {e}")
            screenshots_dir = os.path.join(os.path.abspath(os.curdir), "screenshots")
            if not os.path.exists(screenshots_dir):
                os.makedirs(screenshots_dir)
            self.driver.save_screenshot(os.path.join(screenshots_dir, "error.png"))
            assert False

        finally:
            # Close the driver at the end of the test
            if self.driver:
                self.driver.quit()
