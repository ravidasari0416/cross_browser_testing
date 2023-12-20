# pages/tv_signin.py

import time
from resources.env import BASE_URL,BROWSER_NAME
from utils.drivers import WebDriverManager

class Signin:
    signIn_XPath = "//button[@class='commerce-button'][contains(.,'Sign In')]" # //button[contains(.,'Sign In')]
    userId_xpath = "//input[contains(@id,'accountName')]"
    password_xpath = "//input[contains(@id,'password_text_field')]"
    continue_button_xpath = "//button[contains(.,'Continue')]"

    def __init__(self, driver_manager):
        self.driver = driver_manager.set_driver()

    def clickElement(self, xpath):
        element = self.driver.find_element(by='xpath', value=xpath)
        element.click()

    def setUserID(self, user_id):
        user_id_field = self.driver.find_element(by='xpath', value=self.userId_xpath)
        user_id_field.send_keys(user_id)

    def setPassword(self, password):
        password_field = self.driver.find_element(by='xpath', value=self.password_xpath)
        password_field.send_keys(password)

    def login(self):
        self.clickElement(self.signIn_XPath)
        time.sleep(5)  # It's better to use explicit waits instead of sleep
        self.setUserID(USER_ID)
        time.sleep(5)  # It's better to use explicit waits instead of sleep
        self.setPassword(PASSWORD)
        self.clickElement(self.continue_button_xpath)
        time.sleep(20)  # It's better to use explicit waits instead of sleep
