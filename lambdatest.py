import unittest
import sys
from selenium import webdriver

username = "Your Username" # Replace the username
access_key = "Your Access Key" # Replace the access key

class FirstSampleTest(unittest.TestCase):
    # Generate capabilites from here: https://www.lambdatest.com/capabilities-generator/
    # setUp runs before each test case and 
    def setUp(self):
        desired_caps = {
            "build": 'PyunitTest sample build', # Change your build name here
            "name": 'Py-unittest', # Change your test name here
            "browserName": 'Chrome',
            "version": '92.0',
            "platform": 'Windows 10',
            "resolution": '1024x768',
            "console": 'true', # Enable or disable console logs
            "network":'true'   # Enable or disable network logs
        }
        self.driver = webdriver.Remote(
            command_executor="https://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key),
            desired_capabilities= desired_caps)


# tearDown runs after each test case
    def tearDown(self):
        self.driver.quit()

    # """ You can write the test cases here """
    def test_unit_user_should_able_to_add_item(self):
        # try:
        driver = self.driver

        # Url
        driver.get("https://lambdatest.github.io/sample-todo-app/")

        # Click on check box
        check_box_one = driver.find_element_by_name("li1")
        check_box_one.click()

        # Click on check box
        check_box_two = driver.find_element_by_name("li2")
        check_box_two.click()

        # Enter item in textfield
        textfield = driver.find_element_by_id("sampletodotext")
        textfield.send_keys("Yey, Let's add it to list")

        # Click on add button
        add_button = driver.find_element_by_id("addbutton")
        add_button.click()

        # Verified added item
        added_item = driver.find_element_by_xpath("//span[@class='done-false']").text
        print (added_item)

if __name__ == "__main__":
    unittest.main()
