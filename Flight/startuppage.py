from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webium import BasePage, Find
from selenium.webdriver.common.keys import Keys
import locators
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from .registerpage import RegisterPage


class StartUpPage(object):
    sl = locators.StartUpLocators

    def __init__(self, driver):
        self.driver = driver
        self.wb = WebDriverWait(driver, 60)

    def navigate_to_url(self, url):
        #self.driver.maximize_window()
        self.driver.get(url)
        return StartUpPage(self.driver)

    def click_on_register_button(self):
        self.wb.until(ec.element_to_be_clickable((By.LINK_TEXT, self.sl.lnkRegister_linktext)))
        self.driver.find_element_by_link_text(self.sl.lnkRegister_linktext).click()

    def fill_search_field(self, fieldtext):
        self.driver.find_element_by_name(self.sl.text_field_name).send_keys(fieldtext)

    def click_sign_in_link(self):
        self.wb.until(ec.element_to_be_clickable((By.LINK_TEXT, self.sl.lnksignin_linktext)))
        self.driver.find_element_by_link_text(self.sl.lnksignin_linktext).click()
        return StartUpPage(self.driver)

    def login_to_flight_app(self, username, password):
        self.wb.until(ec.visibility_of_element_located((By.NAME, self.sl.txtUserName_name)))
        self.driver.find_element_by_name(self.sl.txtUserName_name).send_keys(username)
        self.driver.find_element_by_name(self.sl.txtPassword_name).send_keys(password)
        self.driver.find_element_by_name(self.sl.btnSignIn_name).click()



