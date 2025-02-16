import os.path

import allure
import pytest
from allure_commons.types import AttachmentType
from PageObjects.Registrationpage import Registration
from PageObjects.Homepage import Homepage
from utilities.customlogger import LogGen
from utilities.randomstring import random_string_generator
from utilities.readproperties import Read_Commondata

@allure.severity(allure.severity_level.NORMAL)
class Test_browser_details:
    baseurl = Read_Commondata.get_App_url()
    logger = LogGen.loggen()
@pytest.mark.usefixtures("setup")
class Test_reg_succ_continue(Test_browser_details):
    @allure.severity(allure.severity_level.NORMAL)
    def test_reg(self,setup):
        self.driver = setup

        self.logger.info("** Setting the browser.......... **")

        try:
            self.driver.get(self.baseurl)
            self.driver.maximize_window()
            self.logger.info("** Driver Initiated.......... **")

            self.hp = Homepage(self.driver)
            self.hp.clickmyaccount()
            self.hp.clickregister()
            self.logger.info("** Register clicked .......... **")
            self.logger.info("** Registration started.......... **")
            self.repage = Registration(self.driver)
            self.repage.clickfirstname()
            self.repage.clicklastname()
            self.email = random_string_generator() + '@mailinator.com'
            self.repage.clickemail(self.email)
            self.repage.clicktelephone()
            self.repage.clickpassword()
            self.repage.clickcnfpassword()
            self.repage.clickagreebtn()
            self.repage.clickcontinuebtn()

            self.cnf_mesg = self.repage.getsuccessmessage()

            if self.cnf_mesg == "Your Account Has Been Created!":
                self.repage.clickcontinue_after_reg()
                self.myacc_page = self.repage.get_myacc_cnfmsg()
                if self.myacc_page == "My Account":
                    screenshot_dir = os.path.join(os.path.abspath(os.curdir), "screenshots")
                    if not os.path.exists(screenshot_dir):
                        os.makedirs(screenshot_dir)
                    self.driver.save_screenshot(os.path.join(screenshot_dir,"Myacc_succ.png"))
                    print(f"screen shot saves to {screenshot_dir}")
                    assert True

                else:
                    assert False

        except Exception as e:
            self.logger.error(f"Error occurred while registering: {e}")
            # screenshot_dir = os.path.join(os.path.abspath(os.curdir), "screenshots")
            # if not os.path.exists(screenshot_dir):
            #     os.makedirs(screenshot_dir)
            # self.driver.save_screenshot(os.path.join(screenshot_dir, "test_reg_succ_continue_error.png"))
            # self.logger.info(f"Failed screenshot saved to {screenshot_dir}")
            allure.attach(self.driver.get_screenshot_as_png(), name = "auuretest",
                          attachment_type=AttachmentType.PNG)
            assert False  # Fail the test if an exception occurs

        finally:
                # Close the driver at the end of the test
                if self.driver:
                    self.driver.quit()



