# Checking user session existence without logging out and navigating back to homepage not quitting the browser
import allure
from allure_commons.types import AttachmentType
from PageObjects.Homepage import Homepage
from PageObjects.Loginpage import Login
from PageObjects.Myaccount_Page import My_Account_page
from utilities.readproperties import Read_Commondata
from utilities.customlogger import LogGen


class Test_TC_LG_003:
    baseurl = Read_Commondata.get_App_url()
    logger = LogGen.loggen()

    def test_TC_LG_003(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.logger.info("Application Started..........")

        try:
            # Step 1: Perform Login
            self.hp = Homepage(self.driver)
            self.hp.clickmyaccount()
            self.hp.clicklogin()

            self.lp = Login(self.driver)
            self.lp.click_email(Read_Commondata.get_useremail())
            self.lp.click_password(Read_Commondata.get_userpassword())
            self.lp.click_login()

            # Step 2: Validate Login Success
            self.myacc = self.lp.myaccount_page()

            if self.myacc.strip().lower() == "valid":
                self.logger.info(f"User {Read_Commondata.get_useremail()} logged in successfully")
                allure.attach(self.driver.get_screenshot_as_png(), name="After login: My Account page", attachment_type=AttachmentType.PNG)

                # Step 3: Navigate Back to Homepage (Without Closing Browser)
                self.driver.get(self.baseurl)
                self.driver.refresh()
                self.logger.info("Navigated back to the homepage to check session persistence")

                # Step 4: Validate Session Persistence
                self.ma = My_Account_page(self.driver)
                self.ma.click_myaccount()

                if self.ma.is_logout_visible():
                    self.logger.info("Session maintained successfully after reopening the browser")
                    allure.attach(self.driver.get_screenshot_as_png(), name="Session Maintained", attachment_type=AttachmentType.PNG)
                    assert True
                else:
                    self.logger.error("Session not maintained, user is logged out")
                    allure.attach(self.driver.get_screenshot_as_png(), name="Session Lost", attachment_type=AttachmentType.PNG)
                    assert False

            else:
                self.logger.error("Login unsuccessful, cannot validate session persistence")
                allure.attach(self.driver.get_screenshot_as_png(), name="Login Failed", attachment_type=AttachmentType.PNG)
                assert False

        except Exception as e:
            self.logger.error(f"Error during navigation or login function: {e}")
            allure.attach(self.driver.get_screenshot_as_png(), name="Error occurred", attachment_type=AttachmentType.PNG)
            assert False

        finally:
            self.driver.quit()
