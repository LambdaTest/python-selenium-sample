# Import necessary libraries
import time
import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# Fetching environment variables for LambdaTest authentication
username = os.getenv("LT_USERNAME")
access_key = os.getenv("LT_ACCESS_KEY")

# Define the test class which inherits from unittest.TestCase
class AutoHealDemoTest(unittest.TestCase):

    # This method will be executed before every test method
    def setUp(self):
        # Desired capabilities for the test
        desired_caps = {
            'LT:Options': {
                "build": "Auto Heal Demo",
                "name": "Auto Heal Enabled",
                "autoHeal": 'true',
                "geoLocation": "IN"
            },
            "browserName": "Chrome",
        }

        # Initialize the remote webdriver for LambdaTest
        self.driver = webdriver.Remote(
            command_executor="http://{}:{}@hub.lambdatest.com/wd/hub".format(
                username, access_key),
            desired_capabilities=desired_caps)

    # This method will be executed after every test method
    def tearDown(self):
        # Close the browser session
        self.driver.quit()

    # Method to update locators on the page
    def updateLocators(self, driver):
        print("Updating Page Locators")
        # Change the ID of the search submit button
        driver.execute_script("document.getElementById('nav-search-submit-button').id = 'changed-search-submit-btn';")
        time.sleep(1)
        # Change the ID of the search textbox
        driver.execute_script("document.getElementById('twotabsearchtextbox').id = 'newsearchtextbtn';")
        time.sleep(1)

    # Main test method
    def test_demo_site(self):
        driver = self.loadAmazonWebsite()
        # Uncomment below to update page locators.
        self.updateLocators(driver)
        self.searchBookAndGoToCart(driver)

    # Method to search for a book and navigate to the cart
    def searchBookAndGoToCart(self, driver):
        print("Executing Test Script")
        try:
            # Select the dropdown for search categories
            drop_down_btn = driver.find_element(By.ID, "searchDropdownBox")
            drop_down_btn.click()
            time.sleep(1)
            # Select 'Books' from the dropdown
            books_btn = driver.find_element(By.XPATH, "//*[@id=\"searchDropdownBox\"]/option[11]")
            if books_btn.is_displayed():
                books_btn.click()
                # Enter 'Python Programming' in the search box
                search_box = driver.find_element(By.ID, "twotabsearchtextbox")
                if search_box.is_displayed():
                    time.sleep(1)
                    search_box.send_keys("Python Programming")
                    time.sleep(1)
                    # Click the search button
                    search_button = driver.find_element(By.ID, "nav-search-submit-button")
                    if search_button.is_displayed():
                        time.sleep(1)
                        search_button.click()
                        # Mark the test as passed on LambdaTest
                        driver.execute_script("lambda-status=passed")
                        return
            # Mark the test as failed on LambdaTest if any of the above steps fail
            driver.execute_script("lambda-status=failed")
        except:
            # Mark the test as failed on LambdaTest if there's an exception
            driver.execute_script("lambda-status=failed")

    # Method to load the Amazon website
    def loadAmazonWebsite(self):
        driver = self.driver
        print('Loading URL')
        driver.get("https://www.amazon.com")
        driver.set_page_load_timeout(30)
        time.sleep(10)
        print("Page Loaded Successfully.")
        return driver

# This block ensures the test runs if this script is executed
if __name__ == "__main__":
    unittest.main()
