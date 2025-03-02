import allure
from allure_commons.types import AttachmentType

from PageObjects.Homepage import Homepage
from PageObjects.Loginpage import Login
from testCases.conftest import setup
from utilities.customlogger import LogGen
from utilities.readproperties import Read_Commondata
from PageObjects.Myaccount_Page import My_Account_page

class Test_TC_LF_002:
    baseurl = Read_Commondata.get_App_url()
    logger = LogGen.loggen()
    def test_TS_002(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logger.info(".... Browser started ....")

        try:

            self.hp = Homepage(self.driver)
            self.logger.info(".... clicking My Account drop down of Home Page ....")
            self.hp.clickmyaccount()
            self.logger.info(".... Clicking on Login button of Home Page ....")
            self.hp.clicklogin()
            self.logger.info("Executing login function......")
            self.lp = Login(self.driver)
            self.email = "xyzabc124@gmail.com"
            self.lp.click_email(self.email)
            allure.attach(self.driver.get_screenshot_as_png(), name="Email address", attachment_type=AttachmentType.PNG)
            self.password = "xyzabc12"
            self.lp.click_password(self.password)
            allure.attach(self.driver.get_screenshot_as_png(), name="Password entered", attachment_type=AttachmentType.PNG)
            self.lp.click_login()

            self.ma = My_Account_page(self.driver)
            self.myacc = self.lp.myaccount_page()
            self.logger.info(f"Value of myacc: {self.myacc}")  # Add this log

            if self.myacc == "Valid":
                self.logger.info(".... Login Test failed ....")
                self.ma.click_myaccount()
                self.ma.click_logout()
                assert False

            elif self.myacc == "Invalid":
                self.logger.info(".... Login Test passed: Invalid credentials ....")
                allure.attach(self.driver.get_screenshot_as_png(), name="Invalid Login",
                              attachment_type=AttachmentType.PNG)
                assert True

            elif self.myacc == "Exceeded" or self.myacc == "Unknown":
                self.logger.info(".... Login Test passed: Exceeded login attempts ....")
                allure.attach(self.driver.get_screenshot_as_png(), name="Exceeded Login",
                              attachment_type=AttachmentType.PNG)
                assert True

            else:
                self.logger.error("Failure caused during login test")
                allure.attach(self.driver.get_screenshot_as_png(), name="Unknown error",
                              attachment_type=AttachmentType.PNG)
                assert False
        except Exception as e:
            self.logger.error(f"Error occurred during {e}")
            allure.attach(self.driver.get_screenshot_as_png(), name="error during login process", attachment_type=AttachmentType.PNG)

        finally:
            self.driver.quit()
