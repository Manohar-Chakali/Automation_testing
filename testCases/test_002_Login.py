import allure
import pytest
from allure_commons.types import AttachmentType

from PageObjects.Homepage import Homepage
from PageObjects.Loginpage import Login
from utilities.customlogger import LogGen
from utilities.readproperties import Read_Commondata

@allure.severity(allure.severity_level.NORMAL)

class Test_002_login:
    baseurl = Read_Commondata.get_App_url()
    logger = LogGen.loggen()
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.logger.info("**** Login test started ****")
        self.hp = Homepage(self.driver)
        try:
            self.hp.clickmyaccount()
            self.logger.debug("**** My Account clicked ****")
            self.hp.clicklogin()
            self.logger.debug("**** Clicked login button ****")
        except Exception as e:
            self.logger.error(f"error during navigation {e}")
            allure.attach(self.driver.get_screenshot_as_png(), name = "Error_during_navigation",attachment_type=AttachmentType.PNG)
            self.driver.quit()
            assert False

        # Navigating to Login page
        self.logger.debug("**** Reached the login page ****")
        self.lp = Login(self.driver)

        try:
            self.email = Read_Commondata.get_useremail()
            self.lp.click_email(self.email)
            self.logger.debug("**** Email field clicked ****")
            self.password = Read_Commondata.get_userpassword()
            self.lp.click_password(self.password)
            self.logger.debug("**** Password field clicked")
            self.lp.click_login()
            self.logger.debug("**** Login button clicked ****")
            self.myacc = self.lp.myaccount_page()
        except Exception as e:
            self.logger.error("**** error occurred during login ****")
            allure.attach(self.driver.get_screenshot_as_png(), name = "Error_during_login", attachment_type=AttachmentType.PNG)
            self.driver.quit()



        if self.myacc.is_displayed():
            self.logger.info("**** Login Successful ****")
            assert True
        else:
            self.logger.error("**** Login unsuccessful, My Account page not displayed ****")
            allure.attach(self.driver.get_screenshot_as_png(), name = "After login", attachment_type=AttachmentType.PNG)
            assert False, "Login was unsuccessful"




