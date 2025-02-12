from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Registration:
    txt_firstname_xpath = "//input[@id='input-firstname']"
    txt_lastname_xpath = "//input[@id='input-lastname']"
    txt_email_xpath = "//input[@id='input-email']"
    txt_telephone_xpath = "//input[@id='input-telephone']"
    txt_password_xpath = "//input[@id='input-password']"
    txt_confirm_passord_xpath = "//input[@id='input-confirm']"
    tbutton_agree_xpath = "//input[@name='agree']"
    button_continue_xpath = "//input[@value='Continue']"
    txt_account_success_xpath = "//h1[normalize-space()='Your Account Has Been Created!']"
    btn_continue_afterreg_xpath = "//a[@class='btn btn-primary']"
    txt_myaccountmsg_xpath = "//h2[normalize-space()='My Account']"

    def __init__(self, driver):
        self.driver = driver

    def clickfirstname(self):
        fname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.txt_firstname_xpath)))
        fname.send_keys("raju")

    def clicklastname(self):
        lname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.txt_lastname_xpath)))
        lname.send_keys("abcd")

    def clickemail(self,email):
        email_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.txt_email_xpath)))
        email_field.send_keys(email)
    def clicktelephone(self):
        telephone = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, self.txt_telephone_xpath)))
        telephone.send_keys("+1 (987) 654-3321")  # Example with country code and formatting

    def clickpassword(self):
        password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.txt_password_xpath)))
        password.send_keys("abcd@123")

    def clickcnfpassword(self):
        confirm_password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.txt_confirm_passord_xpath)))
        confirm_password.send_keys("abcd@123")

    def clickagreebtn(self):
        agree_btn = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.tbutton_agree_xpath)))
        agree_btn.click()

    def clickcontinuebtn(self):
        continue_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.button_continue_xpath)))
        continue_btn.click()

    def getsuccessmessage(self):
        return WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.txt_account_success_xpath))).text

    def clickcontinue_after_reg(self):
        continubtn  = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.btn_continue_afterreg_xpath)))
        continubtn.click()

    def get_myacc_cnfmsg(self):
        return WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, self.txt_myaccountmsg_xpath))).text
