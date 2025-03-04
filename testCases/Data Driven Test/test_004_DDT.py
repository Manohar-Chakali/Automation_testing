import allure
import pytest
from allure_commons.types import AttachmentType
from allure_pytest.utils import pytest_markers

from testCases.conftest import setup
from utilities.Excel_Data import get_exceldata
from PageObjects.Homepage import Homepage
from PageObjects.Loginpage import Login
from PageObjects.Myaccount_Page import My_Account_page
from utilities.readproperties import Read_Commondata
from utilities.customlogger import LogGen
import os

@pytest.mark.critical
@pytest.mark.login
@pytest.mark.datadriven
@pytest.mark.positive
@pytest.mark.negative
class Test_Data_Driven:
    logger = LogGen.loggen()
    logger.info("**** Logging Started ****")

    baseurl = Read_Commondata.get_App_url()
    path = os.path.join(os.path.abspath(os.curdir), "testData", "Opencart_LoginData.xlsx")

    @pytest.mark.parametrize("username, password, expected_result", get_exceldata(path, "Sheet1"))
    def test_data_driven_testing(self, setup, username, password, expected_result):
        self.logger.info(f"Starting test for: {username}")

        self.driver = setup
        self.driver.maximize_window()

        try:
            # Navigate to Login Page
            self.driver.get(self.baseurl)
            self.hp = Homepage(self.driver)
            self.hp.clickmyaccount()
            self.hp.clicklogin()
            self.ma = My_Account_page(self.driver)

            # Perform Login
            self.lp = Login(self.driver)
            self.lp.click_email(username)
            self.lp.click_password(password)
            self.lp.click_login()

            # Capture Screenshot after Login
            allure.attach(self.driver.get_screenshot_as_png(), name=f"Login_status_for_{username}",
                          attachment_type=AttachmentType.PNG)

            # Validate Result
            self.actual_result = self.lp.myaccount_page()
            self.logger.info(f"Actual: {self.actual_result}, Expected: {expected_result}")
            if self.actual_result.strip().lower() in ["exceeded","unknown"]:
                self.actual_result = "Invalid"
            # Assert and Capture Failures
            elif self.actual_result.strip().lower() == expected_result.strip().lower():
                self.logger.info(f"Test Passed for {username}")
                assert True
            else:
                self.logger.error(f"Test Failed for {username}")
                allure.attach(self.driver.get_screenshot_as_png(), name=f"Failure_{username}",
                              attachment_type=AttachmentType.PNG)
                assert False

        except Exception as e:
            self.logger.error(f"Unexpected error: {e}")
            allure.attach(self.driver.get_screenshot_as_png(), name=f"Unexpected_Error_{username}",
                          attachment_type=AttachmentType.PNG)
            assert False

        finally:
            # Logout only if login was successful
            if self.actual_result.strip().lower() == "valid":
                self.ma.click_myaccount()
                self.ma.click_logout()
                self.logger.info("User logged out successfully.")
