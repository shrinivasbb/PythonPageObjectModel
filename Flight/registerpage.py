from selenium.webdriver.common.keys import Keys
import locators
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class RegisterPage(object):

    rl = locators.RegisterLocators

    def __init__(self, driver):
        self.driver = driver
        self.wb = WebDriverWait(driver, 60)

    def create_user(self, uid, pwd, con_pwd):
        self.wb.until(ec.element_to_be_clickable((By.ID, self.rl.txtUserName_id)))
        self.driver.find_element_by_id(self.rl.txtUserName_id).send_keys(uid)
        self.driver.find_element_by_name(self.rl.txtPassword_name).send_keys(pwd)
        self.driver.find_element_by_name(self.rl.txtConfirm_Password_name).send_keys(con_pwd)
        self.driver.find_element_by_name(self.rl.btnRegister_name).click()
        return RegisterPage(self.driver)

