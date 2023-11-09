import time
from selenium import webdriver

class TestPositiveScenarios:
    def test_positive_login(self):
        # Go to webpage
        driver = webdriver.Chrome()
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(10)
        
        # Type Username into username field
        # username_locator = 