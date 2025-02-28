import allure
import pytest
from allure_commons.types import AttachmentType
from testCases.conftest import setup
from utilities.Excel_Data import get_exceldata
from PageObjects.Homepage import Homepage
from PageObjects.Loginpage import Login
from PageObjects.Myaccount_Page import My_Account_page
from utilities.readproperties import Read_Commondata
from utilities.customlogger import LogGen
import os

class Test_Data_Driven:
    logger = LogGen.loggen()
    logger.info("**** Logging Started ****")

    baseurl = Read_Commondata.get_App_url()
    path = os.path.join(os.path.abspath(os.curdir), "testData", "Opencart_LoginData.xlsx")

    # Parametrize the test with login data from the Excel file
    @pytest.mark.parametrize("username, password, expected_result", get_exceldata(path, "Sheet1"))
    def test_data_driven_testing(self, setup, username, password, expected_result):
        self.logger.info("**** Setting up the browser ****")

        self.driver = setup
        self.driver.maximize_window()

        try:
            # Navigate to Login Page
            self.driver.get(self.baseurl)
            self.hp = Homepage(self.driver)
            self.hp.clickmyaccount()
            self.hp.clicklogin()
            self.ma = My_Account_page(self.driver)

        except Exception as e:
            self.logger.error(f"Error during navigation: {e}")
            allure.attach(self.driver.get_screenshot_as_png(), name="Error_Login_Page", attachment_type=AttachmentType.PNG)
            self.driver.quit()
            assert False

        try:
            # Perform Login
            self.lp = Login(self.driver)
            self.lp.click_email(username)
            self.lp.click_password(password)
            self.lp.click_login()

        except Exception as e:
            self.logger.error(f"Error during login execution: {e}")
            allure.attach(self.driver.get_screenshot_as_png(), name="Login_Execution_Error", attachment_type=AttachmentType.PNG)
            self.driver.quit()
            assert False

        try:
            # Initialize actual_result to avoid AttributeError
            self.actual_result = self.lp.myaccount_page()

            if self.actual_result == expected_result:
                self.logger.info(
                    f"Test Passed for {username}: Expected = {expected_result}, Got = {self.actual_result}")
                assert True
            else:
                self.logger.error(
                    f"Test Failed for {username}: Expected = {expected_result}, Got = {self.actual_result}")
                allure.attach(self.driver.get_screenshot_as_png(), name="Test_Failure",
                              attachment_type=AttachmentType.PNG)
                assert False
        except Exception as e:
            self.logger.error(f"Unexpected error during validation: {e}")
            allure.attach(self.driver.get_screenshot_as_png(), name="Unexpected_Error",
                          attachment_type=AttachmentType.PNG)
            assert False

        finally:
            # Logout if login was successful
            if self.actual_result == "Valid":
                self.ma.click_myaccount()
                self.ma.click_logout()
                self.logger.info("User logged out successfully.")
