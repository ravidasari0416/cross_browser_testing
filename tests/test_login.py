# tests/test_login.py

from utils.drivers import WebDriverManager
import logger_util
import os.path
from pages.tv_signin import Signin
from selenium.webdriver.support.ui import WebDriverWait

logger = logger_util.get_module_logger(os.path.basename(__file__))


class TestLogin:


    def validate_title(self,driver):
        """Validate the title of the web page."""
        try:
            expected_title = "Apple TV+"  # Update this as per the current title
            actual_title = driver.title
            assert actual_title == expected_title, f"Expected title was '{expected_title}', but actual title was '{actual_title}'."
            logger.info(f"Title validation passed. Expected title {expected_title} & actual title {actual_title} ")
        except AssertionError as e:
            logger.error(f"Title validation failed: {e}")
            raise

    def test_sign_in(self, driver):

        try:
            signin_page = Signin(driver)
            logger.info("Reached signin element")

            # Perform the sign-in operation using the methods from the Signin class
            signin_page.clickElement(signin_page.signIn_XPath)
            time.sleep(10)  # Consider using WebDriverWait here
            logger.info("Clicked signin element")

            signin_page.setUserID(USER_ID)
            WebDriverWait(15)
            #time.sleep(10)  # Consider using WebDriverWait here

            signin_page.setPassword(PASSWORD)
            time.sleep(10)  # Consider using WebDriverWait here

            signin_page.clickElement(signin_page.continue_button_xpath)
            time.sleep(10)  # Consider using WebDriverWait here

            # Validation checks (e.g., for successful login)
            # Replace 'some_element_after_login' with the actual element to check for
            # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, 'some_element_after_login')))
            # Add more validation logic here

            logger.info("Sign-in test completed successfully.")

        except Exception as e:
            logger.error(f"An error occurred during the sign-in test: {e}")


'''
    def test_sign_in(self, driver):
        try:
            
        # After sign in, wait for an element that signifies successful login
        # Replace 'some_element_after_login' with an actual element to check for
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, signin.signIn_XPath ))
        )


        # You might want to check for a welcome message, user's name, or logout button etc.
        # to confirm that the login was successful.
        # This is an example, you will need to change it to suit the actual page structure.
        welcome_message = self.driver.find_element(By.XPATH, 'welcome_message_xpath').text
        self.assertIn("Welcome", welcome_message)
'''
