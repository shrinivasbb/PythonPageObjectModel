import locators
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class SelectFlightPage:

    sf = locators.SelectFlightLocators

    def __init__(self, driver):
        self.driver = driver
        self.wb = WebDriverWait(driver, 60)

    def get_labels(self):
        element = self.driver.find_elements_by_css_selector(self.sf.lblDepart_css)
        return [elem.text for elem in element]
