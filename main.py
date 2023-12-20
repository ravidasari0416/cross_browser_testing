# main.py
from utils.drivers import WebDriverManager
from tests.test_login import TestLogin

def run_cross_browser_tests():
    driver_Manager = WebDriverManager()
    driver = driver_Manager.set_driver()
    test = TestLogin()
    test.test_sign_in(driver)
#    test.validate_title(driver)

    driver_Manager.tear_down()

run_cross_browser_tests()
