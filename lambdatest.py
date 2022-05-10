import unittest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

username = os.getenv("LT_USERNAME")  # Replace the username
access_key = os.getenv("LT_ACCESS_KEY")  # Replace the access key


class FirstSampleTest(unittest.TestCase):
    # Generate capabilites from here: https://www.lambdatest.com/capabilities-generator/
    # setUp runs before each test case and
    def setUp(self):
        desired_caps = {
            'LT:Options': {
                "build": "Python Demo",  # Change your build name here
                "name": "Python Demo Test",  # Change your test name here
                "platformName": "Windows 11",
                "selenium_version": "4.0.0",
                "console": 'true',  # Enable or disable console logs
                "network": 'true'  # Enable or disable network logs
            },
            "browserName": "firefox",
            "browserVersion": "98.0",
        }

        self.driver = webdriver.Remote(
            command_executor="https://{}:{}@hub.lambdatest.com/wd/hub".format(
                username, access_key),
            desired_capabilities=desired_caps)

    # tearDown runs after each test case

    def tearDown(self):
        self.driver.quit()

    # """ You can write the test cases here """
    def test_demo_site(self):

        # try:
        driver = self.driver

        # Url
        print('Loading URL')
        driver.get("https://stage-demo.lambdatest.com/")

        # Let's select the location
        driver.find_element(By.ID, "headlessui-listbox-button-1").click()
        location = driver.find_element(By.ID, "Bali")
        location.click()
        print("Location is selected as Bali.")

        # Let's select the number of guests
        driver.find_element(By.ID, "headlessui-listbox-button-5").click()
        guests = driver.find_element(By.ID, "2")
        guests.click()
        print("Number of guests are selected.")

        # Searching for the results
        search = driver.find_element(By.XPATH, "//*[@id='search']")
        print("Search button is displayed " + str(search.is_displayed()))
        assert search.is_displayed(), "Search is not displayed"
        search.click()
        driver.implicitly_wait(3)

        # Let's select one of the hotels for booking
        reserve = driver.find_element(By.ID, "reserve-now")
        reserve.click()
        driver.implicitly_wait(3)
        proceed = driver.find_element(By.ID, "proceed")
        proceed.click()
        driver.implicitly_wait(3)
        print("Booking is confirmed.")

        # Let's download the invoice
        download = driver.find_element(By.ID, "invoice")
        if (download.is_displayed()):
            download.click()
            driver.execute_script("lambda-status=passed")
            print("Tests are run successfully!")
        else:
            driver.execute_script("lambda-status=failed")


if __name__ == "__main__":
    unittest.main()
