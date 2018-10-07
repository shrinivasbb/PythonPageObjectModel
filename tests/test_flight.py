import pytest
from selenium import webdriver
import os
from Flight.startuppage import StartUpPage
from Flight.registerpage import RegisterPage
from Flight.bookingpage import BookingPage
from Flight.selectflightpage import SelectFlightPage
from helper.jsonreader import JsonReader
import unittest


@pytest.fixture(scope="class")
def driver_actions(request):
    direct_path = os.path.dirname(os.path.realpath(__file__))
    direct_path = os.path.abspath(os.path.join(direct_path, '..'))
    #request.cls.driver = webdriver.Chrome(direct_path + '/resources/chromedriver.exe')
    request.cls.driver = webdriver.Chrome("/usr/bin/chromedriver")
    request.cls.startup = StartUpPage(request.cls.driver)
    request.cls.register = RegisterPage(request.cls.driver)
    request.cls.booking = BookingPage(request.cls.driver)
    request.cls.select = SelectFlightPage(request.cls.driver)
    dat = request.cls.json_reader.read_from_file_and_element("testdata.json", "login")
    request.cls.startup.navigate_to_url(dat['url']) \
               .click_on_register_button()
    request.cls.register.create_user(dat['uid'], dat['pwd'], dat['con_pwd'])
    request.cls.startup.click_sign_in_link() \
               .login_to_flight_app(dat['uid'], dat['pwd'])
    yield
    request.cls.driver.quit()


@pytest.mark.usefixtures('driver_actions')
class FlightTest(unittest.TestCase):
    json_reader = JsonReader

    def test_book_a_flight(self):
        dat = self.json_reader.read_from_file("testdata.json")
        self.booking.book_a_flight(dat) \
                    .click_continue()
        returntext = self.select.get_labels()
        assert returntext == dat['label']

