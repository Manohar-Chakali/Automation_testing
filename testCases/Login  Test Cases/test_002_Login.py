import allure
from allure_commons.types import AttachmentType

from PageObjects.Homepage import Homepage
from PageObjects.Loginpage import Login
from utilities.customlogger import LogGen
from utilities.readproperties import Read_Commondata
from PageObjects.Myaccount_Page import My_Account_page


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
            # Navigate to Login Page
            self.hp.clickmyaccount()
            self.logger.debug("**** My Account clicked ****")
            self.hp.clicklogin()
            self.logger.debug("**** Clicked login button ****")
            self.ma = My_Account_page(self.driver)

            # Perform Login
            self.logger.debug("**** Reached the login page ****")
            self.lp = Login(self.driver)

            self.email = Read_Commondata.get_useremail()
            self.password = Read_Commondata.get_userpassword()

            self.lp.click_email(self.email)
            self.logger.debug(f"**** Entered email: {self.email} ****")
            self.lp.click_password(self.password)
            self.logger.debug(f"**** Entered password: {self.password} ****")
            self.lp.click_login()
            self.logger.debug("**** Login button clicked ****")

            # Screenshot after login attempt
            allure.attach(self.driver.get_screenshot_as_png(), name="After_Login_Attempt",
                          attachment_type=AttachmentType.PNG)

        except Exception as e:
            self.logger.error(f"**** Error during login: {e} ****")
            allure.attach(self.driver.get_screenshot_as_png(), name="Error_during_login",
                          attachment_type=AttachmentType.PNG)
            self.driver.quit()
            assert False, "Exception occurred during login"


        finally:

            # Check the login result

            self.myacc = self.lp.myaccount_page()

            self.logger.info(f"**** Detected login result: {self.myacc} ****")

            # Save page source if result is unexpected

            if self.myacc.strip().lower() not in ["valid", "invalid"]:
                with open("debug_page_source.html", "w", encoding="utf-8") as f:
                    f.write(self.driver.page_source)

                self.logger.warning("**** Unexpected login result! Saved page source for analysis ****")

            # Handle special cases like "exceeded" or "unknown"

            if self.myacc.strip().lower() in ["exceeded", "unknown"]:

                self.myacc = "Invalid"


            # Successful Login Handling

            elif self.myacc.strip().lower() == "valid":

                self.logger.info("**** Login Successful ****")

                self.ma.click_myaccount()

                self.logger.info("**** Clicked on My account ****")

                self.ma.click_logout()

                self.logger.info("**** Logout Successful ****")

                assert True


            # Failed Login Handling

            else:

                self.logger.error("**** Login unsuccessful, My Account page not displayed ****")

                allure.attach(self.driver.get_screenshot_as_png(), name="After_login",

                              attachment_type=AttachmentType.PNG)

                assert False, "Login was unsuccessful"
