import locators
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class BookingPage:

    bl = locators.BookingLocators

    def __init__(self, driver):
        self.driver = driver
        self.wb = WebDriverWait(driver, 60)

    def book_a_flight(self, listofParams):
        self.wb.until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.bl.rdbRoundTrip_css)))
        if listofParams['type'] == 'roundtrip':
            self.driver.find_element_by_css_selector(self.bl.rdbRoundTrip_css).click()
        else:
            self.driver.find_element_by_css_selector(self.bl.rdbOneWay_css).click()
        passengers = self.driver.find_element_by_name(self.bl.cmbPassengers_name)
        Select(passengers).select_by_visible_text(listofParams['passenger'])
        departingfrom = self.driver.find_element_by_name(self.bl.cmbDepartingFrom_name)
        Select(departingfrom).select_by_visible_text(listofParams['departfrom'])
        frommonth = self.driver.find_element_by_name(self.bl.cmbFromMonth_name)
        Select(frommonth).select_by_visible_text(listofParams['onmonth'])
        fromdate = self.driver.find_element_by_name(self.bl.cmbFromDate_name)
        Select(fromdate).select_by_visible_text(listofParams['ondate'])
        arrivingin = self.driver.find_element_by_name(self.bl.cmbArrivingIn_name)
        Select(arrivingin).select_by_visible_text(listofParams['arrivingin'])
        tomonth = self.driver.find_element_by_name(self.bl.cmbToMonth_name)
        Select(tomonth).select_by_visible_text(listofParams['tomonth'])
        todate = self.driver.find_element_by_name(self.bl.cmbToDate_name)
        Select(todate).select_by_visible_text(listofParams['todate'])
        if listofParams['class'] == 'economy':
            self.driver.find_element_by_css_selector(self.bl.rdbEconomy_css).click()
        elif listofParams['class'] == 'business':
            self.driver.find_element_by_css_selector(self.bl.rdbBusiness_css).click()
        else:
            self.driver.find_element_by_css_selector(self.bl.rdbFirstClass_css).click()
        self.driver.find_element_by_name(self.bl.cmbToDate_name).click()
        options=self.driver.find_elements_by_tag_name("option")
        for option in options:
            if option.text == listofParams['airline']:
                option.click()
        return BookingPage(self.driver)

    def click_continue(self):
        self.wb.until(ec.element_to_be_clickable((By.NAME, self.bl.btnContinue_name)))
        self.driver.find_element_by_name(self.bl.btnContinue_name).click()
