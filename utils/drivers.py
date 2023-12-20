# utils/drivers.py
import os.path
from selenium import webdriver
from resources.env import BASE_URL, BROWSER_NAME
import logger_util


logger = logger_util.get_module_logger(os.path.basename(__file__))

class WebDriverManager:
    def __init__(self):
        self.driver = None

    def set_driver(self):
        try:
            if BROWSER_NAME.lower() == "chrome":
                self.driver = webdriver.Chrome()
            elif BROWSER_NAME.lower() == "firefox":
                self.driver = webdriver.Firefox()
            elif BROWSER_NAME.lower() == "edge":
                self.driver = webdriver.Edge()
            # Add other browsers as needed
            else:
                logger.error("Browser not supported")
                raise ValueError("Browser not supported")

            self.driver.get(BASE_URL)
            logger.info(f"Opened {BASE_URL} in {BROWSER_NAME} browser.")
            return self.driver
        except Exception as e:
            logger.exception("Failed to initialize the web driver: " + str(e))


    def tear_down(self):
        """Tear down method to close the web driver."""
        try:
            self.driver.quit()
            logger.info("Web driver closed.")
        except Exception as e:
            logger.exception("Failed to close the web driver: " + str(e))
