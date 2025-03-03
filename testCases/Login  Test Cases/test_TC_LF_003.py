import pytest
import allure
from allure_commons.types import AttachmentType
from PageObjects.Homepage import Homepage
from PageObjects.Loginpage import Login
from PageObjects.Myaccount_Page import My_Account_page
from testCases.conftest import setup
from utilities.customlogger import LogGen
from utilities.readproperties import Read_Commondata

@pytest.mark.negative
@pytest.mark.login
@pytest.mark.regression
@pytest.mark.critical
class Test_invalid_email:
    baseurl = Read_Commondata.get_App_url()
    logger = LogGen.loggen()

    def test_TS_002(self, setup):
            self.driver = setup
            self.driver.get(self.baseurl)
            self.driver.maximize_window()
            self.logger.info("Application started........")

            try:
                self.hp = Homepage(self.driver)
                self.hp.clickmyaccount()
                self.hp.clicklogin()

                self.lp = Login(self.driver)
                self.lp.click_email("xyzabc123@gmail.com        ")
                self.lp.click_password("12345")
                self.lp.click_login()
                allure.attach(self.driver.get_screenshot_as_png(), name = "invalid email", attachment_type=AttachmentType.PNG)

            except Exception as e:
                self.logger.error(f"Error during {Test_invalid_email} with {e}")
                allure.attach(self.driver.get_screenshot_as_png(), name= "Error occurred", attachment_type=AttachmentType.PNG)

                self.ma = My_Account_page(self.driver)
                self.myacc = self.lp.myaccount_page()
                if self.myacc.lower() == "valid":
                    self.ma.click_myaccount()
                    self.ma.click_logout()
                    self.logger.info("Account logged in with invalid credentials so logged out successfully.....")
                    self.logger.info("Test has been passed since not logged into the account as per the invalid creds")
                    assert False

                elif self.myacc.lower() == "Invalid" or self.myacc.lower() == "Unknown":
                    self.logger.info("Test has been passed since not logged into the account as per the invalid creds")
                    assert True

                else:
                    self.logger.error(f"Error occurred during {Test_invalid_email}")
                    allure.attach(self.driver.get_screenshot_as_png(), name = f"Error at{Test_invalid_email}", attachment_type=AttachmentType.PNG)
                    assert False


            finally:
                self.driver.quit()
