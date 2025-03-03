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
class Test_invalid_pass:
    baseurl = Read_Commondata.get_App_url()
    logger = LogGen.loggen()

    def test_TS_002(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logger.info("Application started........")

        try:
            self.hp =  Homepage(self.driver)
            self.hp.clickmyaccount()
            self.hp.clicklogin()

            self.lp = Login(self.driver)
            self.lp.click_email("ndj@mailinator.com")
            self.password = "xyzabc123"
            self.lp.click_password(self.password)
            self.lp.click_login()
            allure.attach(self.driver.get_screenshot_as_png(), name = f"Error with {self.password}", attachment_type=AttachmentType.PNG)

            self.myacc = self.lp.myaccount_page()
            self.logger.info(f"Captured myacc value: {self.myacc}")

            # Ensure we handle unexpected whitespace or casing issues
            myacc_status = self.myacc.strip().lower()

            if myacc_status == "valid":
                self.ma = My_Account_page(self.driver)
                self.ma.click_myaccount()
                self.ma.click_logout()
                self.logger.info("Test logged in with invalid credentials so logged out successfully.....")
                assert False

            elif myacc_status in ["invalid", "unknown"]:
                self.logger.info("Test passed and no login successful....")
                assert True

            else:
                self.logger.info(f"Error occurred at {Test_invalid_pass} validation: Received '{myacc_status}'")
                allure.attach(self.driver.get_screenshot_as_png(), name=f"Error at {Test_invalid_pass}",
                              attachment_type=AttachmentType.PNG)
                assert False

        except Exception as e:
            self.logger.info(f"Error occurred at {Test_invalid_pass}")
            allure.attach(self.driver.get_screenshot_as_png(), name= f"Error occurred at {Test_invalid_pass}", attachment_type=AttachmentType.PNG)



        finally:
            self.driver.quit()

