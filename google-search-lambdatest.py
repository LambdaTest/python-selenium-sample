import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os


"""
    LambdaTest selenium automation sample example
    Configuration
    ----------
    username: Username can be found at automation dashboard
    accessToken:  AccessToken can be genarated from automation dashboard or profile section

    Result
    -------
    Execute Test on lambdatest Distributed Grid perform selenium automation based 
"""

# username: Username can be found at automation dashboard
username = os.getenv("LT_USERNAME")
# accessToken:  AccessToken can be genarated from automation dashboard or profile section
accessToken = os.getenv("LT_ACCESS_KEY")
# gridUrl: gridUrl can be found at automation dashboard
gridUrl = "hub.lambdatest.com/wd/hub"


capabilities = {
    'LT:Options': {
        "build": "your build name",
        "name": "your test name",
        "platformName": "Windows 10"
    },
    "browserName": "Chrome",
    "browserVersion": "latest",
}

url = "https://"+username+":"+accessToken+"@"+gridUrl


"""
    ----------
    platformName : Supported platfrom - (Windows 10, Windows 8.1, Windows 8, Windows 7,  macOS High Sierra, macOS Sierra, OS X El Capitan, OS X Yosemite, OS X Mavericks)
    browserName : Supported platfrom - (chrome, firefox, Internet Explorer, MicrosoftEdge)
    browserVersion :  Supported list of version can be found at https://www.lambdatest.com/capabilities-generator/

    Result
    -------
"""

driver = webdriver.Remote(
    command_executor=url,
    desired_capabilities=capabilities
)

"""
	----------
	Execute test:  navigate google.com search LambdaTest
	Result
	----------
	print title
"""

driver.get("https://www.google.com/ncr")

print("Searching lambdatest on google.com ")
time.sleep(8)
elem = driver.find_element_by_name("q")
elem.send_keys("lambdatest.com")
elem.submit()

print("Printing title of current page :"+driver.title)
driver.execute_script("lambda-status=passed")
print("Requesting to mark test : pass")

"""
	Quit selenium driver
"""
driver.quit()
