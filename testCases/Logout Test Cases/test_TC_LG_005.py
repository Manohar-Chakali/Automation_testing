from typing import final

import allure
from allure_commons.types import AttachmentType

from PageObjects.Homepage import Homepage
from PageObjects.Myaccount_Page import My_Account_page
from utilities.customlogger import LogGen
from utilities.readproperties import Read_Commondata


class Test_TC_LG_005:
    base_url = Read_Commondata.get_App_url()
    logger = LogGen.loggen()

    def test_LG_btn_check(self, setup):
        self.driver = setup
        self.logger.info("Staring application........")
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        self.hp = Homepage(self.driver)
        self.hp.clickmyaccount()
        self.ma = My_Account_page(self.driver)

        try:
            is_visible: bool = self.ma.is_logout_visible()
            assert not is_visible
        except Exception as e:
            self.logger.info(f"Error during Logout button checking process {e}")
            allure.attach(self.driver.get_screenshot_as_png(), name = "Visibility of Logout before login", attachment_type=AttachmentType.PNG)
        finally:
            self.driver.quit()