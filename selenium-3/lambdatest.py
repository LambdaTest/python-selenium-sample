import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import warnings

username = os.getenv("LT_USERNAME")  # Replace the username
access_key = os.getenv("LT_ACCESS_KEY")  # Replace the access key


capability = {
	"browserName": "Chrome",
	"browserVersion": "latest",
	"LT:Options": {
        "username": username,
		"accessKey": access_key,
		"platformName": "Windows 10",
        "build": "Selenium 3 Example",
        "name" : "Selenium 3 Sample Test"
	}
}

def suppress_resource_warnings():
    warnings.filterwarnings("ignore", category=ResourceWarning)

class FirstSampleTest(unittest.TestCase):
    driver = None

    def setUp(self):
        suppress_resource_warnings()
        self.driver = webdriver.Remote(
            command_executor = "http://{}:{}@hub.lambdatest.com/wd/hub".format(
                username, access_key
            ),
            # options=options,
            desired_capabilities = capability
        )

    # """ You can write the test cases here """
    def test_demo_site(self):
        suppress_resource_warnings()
        driver = self.driver
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(30)
        # driver.set_window_size(1920, 1080)

        # Url
        print("Loading URL")
        driver.get(
            "https://lambdatest.github.io/sample-todo-app/"
        )

        # Let's click on a element
        driver.find_element(By.NAME, "li1").click()
        location = driver.find_element(By.NAME, "li2")
        location.click()
        print("Clicked on the second element")

        # Let's add a checkbox
        driver.find_element(By.ID, "sampletodotext").send_keys("LambdaTest")
        add_button = driver.find_element(By.ID, "addbutton")
        add_button.click()
        print("Added LambdaTest checkbox")

        # print the heading
        search = driver.find_element(By.CSS_SELECTOR, ".container h2")
        assert search.is_displayed(), "heading is not displayed"
        print(search.text)
        search.click()
        driver.implicitly_wait(3)

         # Let's download the invoice
        heading = driver.find_element(By.CSS_SELECTOR, ".container h2")
        if heading.is_displayed():
            heading.click()
            driver.execute_script("lambda-status=passed")
            print("Tests are run successfully!")
        else:
            driver.execute_script("lambda-status=failed")

  # tearDown runs after each test case
    def tearDown(self):
        self.driver.quit()
       

if __name__ == "__main__":
    unittest.main()