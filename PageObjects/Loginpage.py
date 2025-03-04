from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:
    def __init__(self, driver):
        self.driver = driver

    # XPaths
    txt_email_xpath = "//input[@id='input-email']"
    txt_password_xpath = "//input[@id='input-password']"
    btn_login_xpath = "//input[@value='Login']"
    txt_login_cnf_msg_xpath = "//h2[normalize-space()='My Account']"
    txt_login_error_xpath = "//div[contains(text(), 'Warning: No match for E-Mail Address and/or Password.')]"
    txt_accout_exceeded_xpath = "//div[@class='alert alert-danger alert-dismissible']"

    def click_email(self, email):
        email_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.txt_email_xpath))
        )
        email_field.send_keys(email)

    def click_password(self, password):
        password_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.txt_password_xpath))
        )
        password_field.send_keys(password)

    def click_login(self):
        login_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_login_xpath))
        )
        login_button.click()

    def myaccount_page(self):
        try:
            # Check for all outcomes (independent checks)
            is_valid = False
            is_invalid = False
            is_exceeded = False

            try:
                is_valid = WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located((By.XPATH, self.txt_login_cnf_msg_xpath))
                )
            except:
                pass

            try:
                is_invalid = WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located((By.XPATH, self.txt_login_error_xpath))
                )
            except:
                pass

            try:
                is_exceeded = WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located((By.XPATH, self.txt_accout_exceeded_xpath))
                )
            except:
                pass

            # Determine result based on detected conditions
            if is_valid:
                print("Detected: Valid Login")
                return "Valid"
            elif is_invalid:
                print("Detected: Invalid Login")
                return "Invalid"
            elif is_exceeded:
                print("Detected: Exceeded Attempts")
                return "Exceeded"
            else:
                print("Detected: Unknown")
                return "Unknown"

        except Exception as e:
            print(f"Exception in myaccount_page(): {e}")
            return "Unknown error occurred"
