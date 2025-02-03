from PageObjects.Homepage import Homepage
from PageObjects.Loginpage import Login
from utilities.customlogger import LogGen

class Test_002_login:
    baseurl = "https://naveenautomationlabs.com/opencart/"
    logger = LogGen.loggen()
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
            self.driver.quit()
            assert False

        # Navigating to Login page
        self.logger.debug("**** Reached the login page ****")
        self.lp = Login(self.driver)

        try:
            self.lp.click_email()
            self.logger.debug("**** Email field clicked ****")
            self.lp.click_password()
            self.logger.debug("**** Password field clicked")
            self.lp.click_login()
            self.logger.debug("**** Login button clicked ****")
            self.myacc = self.lp.myaccount_page()
        except Exception as e:
            self.logger.error("**** error occurred during login ****")
            self.driver.quit()



        if self.myacc.is_displayed():
            self.logger.info("**** Login Successful ****")
            assert True
        else:
            self.logger.error("**** Login unsuccessful, My Account page not displayed ****")
            assert False, "Login was unsuccessful"




