# Run Selenium Tests With Python On LambdaTest

![171934563-4806efd2-1154-494c-a01d-1def95657383 (1)](https://user-images.githubusercontent.com/70570645/172273386-fa9606ac-3e63-4b2e-8978-3142add3e038.png)


<p align="center">
  <a href="https://www.lambdatest.com/blog/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample" target="_bank">Blog</a>
  &nbsp; &#8901; &nbsp;
  <a href="https://www.lambdatest.com/support/docs/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample" target="_bank">Docs</a>
  &nbsp; &#8901; &nbsp;
  <a href="https://www.lambdatest.com/learning-hub/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample" target="_bank">Learning Hub</a>
  &nbsp; &#8901; &nbsp;
  <a href="https://www.lambdatest.com/newsletter/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample" target="_bank">Newsletter</a>
  &nbsp; &#8901; &nbsp;
  <a href="https://www.lambdatest.com/certifications/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample" target="_bank">Certifications</a>
  &nbsp; &#8901; &nbsp;
  <a href="https://www.youtube.com/c/LambdaTest" target="_bank">YouTube</a>
</p>
&emsp;
&emsp;
&emsp;

*Learn how to run your Python automation testing scripts on the LambdaTest platform*

[<img height="58" width="200" src="https://user-images.githubusercontent.com/70570645/171866795-52c11b49-0728-4229-b073-4b704209ddde.png">](https://accounts.lambdatest.com/register)


## Table Of Contents

* [Pre-requisites](#pre-requisites)
* [Run Your First Test](#run-your-first-test)
* [Local Testing With Python](#testing-locally-hosted-or-privately-hosted-projects)

## Prerequisites

Before you can start performing **Python** automation testing with **Selenium**, you would need to:

* Install the latest Python build from the [official website](https://www.python.org/downloads/). We recommend using the latest version.
* Make sure **pip** is installed in your system. You can install **pip** from [here](https://pip.pypa.io/en/stable/installation/).
* Download the latest **Selenium Client** and its **WebDriver bindings** from the [official website](https://www.selenium.dev/downloads/). Latest versions of **Selenium Client** and **WebDriver** are ideal for running your automation script on LambdaTest Selenium cloud grid.

### Installing Selenium Dependencies And Tutorial Repo

**Step 1:** Clone the LambdaTest’s python-selenium-sample repository and navigate to the code directory as shown below:

```bash
git clone https://github.com/LambdaTest/python-selenium-sample
cd python-selenium-sample
```

**Step 2:** Download the driver from the link, or you can use **pip** to install it.
```bash
pip install selenium
export PYTHONWARNINGS="ignore:Unverified HTTPS request"   //Disable ssl warning
```

### Setting Up Your Authentication

Make sure you have your LambdaTest credentials with you to run test automation scripts. You can get these credentials from the [LambdaTest Automation Dashboard](https://automation.lambdatest.com/build/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample) or by your [LambdaTest Profile](https://accounts.lambdatest.com/login/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample).

**Step 2:** Set LambdaTest **Username** and **Access Key** in environment variables.

* For **Linux/macOS**:
  
  ```bash
  export LT_USERNAME="YOUR_USERNAME" 
  export LT_ACCESS_KEY="YOUR ACCESS KEY"
  ```
  * For **Windows**:
  ```bash
  set LT_USERNAME="YOUR_USERNAME" 
  set LT_ACCESS_KEY="YOUR ACCESS KEY"
  ```

## Run Your First Test

>**Test Scenario**: The [lambdatest.py](https://github.com/LambdaTest/python-selenium-sample/blob/master/lambdatest.py) sample script tests a simple to-do application with basic functionalities like mark items as done, add items in a list, calculate total pending items etc.

### Configuration Of Your Test Capabilities

**Step 4:** In the python script, you need to update your test capabilities. In this code, we are passing browser, browser version, and operating system information, along with LambdaTest Selenium grid capabilities via capabilities object. 

The capabilities in the below code are defined as:

```python
options = ChromeOptions()
options.browser_version = "114.0"
options.platform_name = "macOS High Sierra"
lt_options = {}
lt_options["video"] = True
lt_options["resolution"] = "1920x1080"
lt_options["network"] = True
lt_options["build"] = "test_build"
lt_options["project"] = "unit_testing"
lt_options["smartUI.project"] = "test"
lt_options["name"] = "basic_unit_selinium"
lt_options["w3c"] = True
lt_options["plugin"] = "python-python"
options.set_capability('LT:Options', lt_options)
```
You can generate capabilities for your test requirements with the help of our inbuilt [Desired Capability Generator](https://www.lambdatest.com/capabilities-generator/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample).

### Executing The Test

**Step 5:** You would need to execute the below command in your terminal/cmd.

```bash
python lambdatest.py
```
For python3 use
```bash
python3 lambdatest.py
```

Your test results would be displayed on the test console (or command-line interface if you are using terminal/cmd) and on LambdaTest automation dashboard. 


## Testing Locally Hosted Or Privately Hosted Projects

You can test your locally hosted or privately hosted projects with LambdaTest Selenium grid using LambdaTest Tunnel. All you would have to do is set up an SSH tunnel using tunnel and pass toggle `tunnel = True` via desired capabilities. LambdaTest Tunnel establishes a secure SSH protocol based tunnel that allows you in testing your locally hosted or privately hosted pages, even before they are live.

Refer our [LambdaTest Tunnel documentation](https://www.lambdatest.com/support/docs/testing-locally-hosted-pages/) for more information.

Here’s how you can establish LambdaTest Tunnel.

Download the binary file of:
* [LambdaTest Tunnel for Windows](https://downloads.lambdatest.com/tunnel/v3/windows/64bit/LT_Windows.zip)
* [LambdaTest Tunnel for macOS](https://downloads.lambdatest.com/tunnel/v3/mac/64bit/LT_Mac.zip)
* [LambdaTest Tunnel for Linux](https://downloads.lambdatest.com/tunnel/v3/linux/64bit/LT_Linux.zip)

Open command prompt and navigate to the binary folder.

Run the following command:

```bash
LT -user {user’s login email} -key {user’s access key}
```
So if your user name is lambdatest@example.com and key is 123456, the command would be:

```bash
LT -user lambdatest@example.com -key 123456
```
Once you are able to connect **LambdaTest Tunnel** successfully, you would just have to pass on tunnel capabilities in the code shown below :

**Tunnel Capability**

```
"tunnel" : true
```

## Tutorials 📙

Check out our latest tutorials on Python automation testing 👇

* [Why Python Is A Preferred Language For Test Automation?](https://www.lambdatest.com/blog/python-automation-testing/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample)
* [7 Best Python Testing Frameworks](https://www.lambdatest.com/blog/top-python-frameworks-in-2020-for-selenium-test-automation/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample)
* [Selenium 4 With Python: All You Need To Know](https://www.lambdatest.com/blog/selenium-with-python/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample)
* [How to Set Up Selenium With Python for Modern Web Automation](https://www.lambdatest.com/blog/selenium-webdriver-with-python/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample)
* [Using Selenium and Python Hypothesis for Automation Testing](https://www.lambdatest.com/blog/using-selenium-and-python-hypothesis-for-automation-testing/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample)
* [Selenium Python Tutorial: Getting Started With BDD In Behave](https://www.lambdatest.com/blog/selenium-python-behave-tutorial-bdd/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample)
* [Selenium Python Tutorial: Getting Started With Pytest](https://www.lambdatest.com/blog/selenium-python-pytest-testing-tutorial/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample)
* [Selenium Python Tutorial: Running First PyUnit Script](https://www.lambdatest.com/blog/using-pyunit-for-testing-a-selenium-python-test-suite/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample)
* [Robot Framework with Selenium and Python](https://www.lambdatest.com/blog/robot-framework-tutorial/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample)
* [Getting Started With Selenium Python [Tutorial]](https://www.lambdatest.com/blog/robot-framework-tutorial/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample)
* [Running Python Selenium Test in Parallel With PyTest](https://www.lambdatest.com/blog/robot-framework-tutorial/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample)
* [Parallel Testing In Selenium WebDriver With Python Using Unittest](https://www.lambdatest.com/blog/robot-framework-tutorial/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample)
* [Automated Browser Testing with Opera and Selenium in Python](https://www.lambdatest.com/blog/automated-browser-testing-with-opera-and-selenium-in-python/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample)
* [How To Take A Screenshot Using Python & Selenium?](https://www.lambdatest.com/blog/python-selenium-screenshots/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample)
* [How To Drag And Drop In Selenium With Python?](https://www.lambdatest.com/blog/drag-and-drop-in-selenium-python/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample)
* [How To Switch Tabs In A Browser Using Selenium Python?](https://www.lambdatest.com/blog/python-selenium-switch-tabs/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample)
* [How To Get Page Source In Selenium Using Python?](https://www.lambdatest.com/blog/how-to-get-page-source-in-selenium-webdriver/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample)
* [How To Handle Dropdowns In Selenium WebDriver Using [Python?]](https://www.lambdatest.com/blog/handling-dropdown-in-selenium-webdriver-python/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample)
* [How To Do Parameterization In Pytest With Selenium?](https://www.lambdatest.com/blog/parameterization-in-pytest-with-selenium/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample)
* [Page Object Model (POM) In Selenium Python](https://www.lambdatest.com/blog/page-object-model-in-selenium-python/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample)
* [How To Read Configuration Files in Python Using Selenium](https://www.lambdatest.com/blog/how-to-read-configuration-files-in-python-using-selenium/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample)
* [How To Create an Automated Web Bot With Selenium in Python?](https://www.lambdatest.com/blog/automated-web-bot-with-selenium-python/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample)
* [How To Perform Web Scraping Using Selenium and Python?](https://www.lambdatest.com/blog/web-scraping-using-selenium-and-python/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample)
* [Adding Firefox Extensions With Selenium in Python](https://www.lambdatest.com/blog/adding-firefox-extensions-with-selenium-in-python/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample)
* [How to Handle JavaScript Alert in Selenium WebDriver Using Python?](https://www.lambdatest.com/blog/how-to-handle-javascript-alert-in-selenium-webdriver/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample)
* [Use Selenium Wait for Page to Load With Python](https://www.lambdatest.com/blog/selenium-wait-for-page-to-load/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample)
* [Selenium Python Cheat Sheet for Test Automation](https://www.lambdatest.com/blog/selenium-python-cheat-sheet/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample)


## Documentation & Resources :books:

      
Visit the following links to learn more about LambdaTest's features, setup and tutorials around test automation, mobile app testing, responsive testing, and manual testing.

* [LambdaTest Documentation](https://www.lambdatest.com/support/docs/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample)
* [LambdaTest Blog](https://www.lambdatest.com/blog/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample)
* [LambdaTest Learning Hub](https://www.lambdatest.com/learning-hub/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample)    

## LambdaTest Community :busts_in_silhouette:

The [LambdaTest Community](https://community.lambdatest.com/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample) allows people to interact with tech enthusiasts. Connect, ask questions, and learn from tech-savvy people. Discuss best practises in web development, testing, and DevOps with professionals from across the globe 🌎

## What's New At LambdaTest ❓

To stay updated with the latest features and product add-ons, visit [Changelog](https://changelog.lambdatest.com/) 
      
## About LambdaTest

[LambdaTest](https://www.lambdatest.com/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample) is a leading test execution and orchestration platform that is fast, reliable, scalable, and secure. It allows users to run both manual and automated testing of web and mobile apps across 3000+ different browsers, operating systems, and real device combinations. Using LambdaTest, businesses can ensure quicker developer feedback and hence achieve faster go to market. Over 500 enterprises and 1 Million + users across 130+ countries rely on LambdaTest for their testing needs.    

### Features

* Run Selenium, Cypress, Puppeteer, Playwright, and Appium automation tests across 3000+ real desktop and mobile environments.
* Real-time cross browser testing on 3000+ environments.
* Test on Real device cloud
* Blazing fast test automation with HyperExecute
* Accelerate testing, shorten job times and get faster feedback on code changes with Test At Scale.
* Smart Visual Regression Testing on cloud
* 120+ third-party integrations with your favorite tool for CI/CD, Project Management, Codeless Automation, and more.
* Automated Screenshot testing across multiple browsers in a single click.
* Local testing of web and mobile apps.
* Online Accessibility Testing across 3000+ desktop and mobile browsers, browser versions, and operating systems.
* Geolocation testing of web and mobile apps across 53+ countries.
* LT Browser - for responsive testing across 50+ pre-installed mobile, tablets, desktop, and laptop viewports

    
[<img height="58" width="200" src="https://user-images.githubusercontent.com/70570645/171866795-52c11b49-0728-4229-b073-4b704209ddde.png">](https://accounts.lambdatest.com/register)


      
## We are here to help you :headphones:

* Got a query? we are available 24x7 to help. [Contact Us](support@lambdatest.com/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample)
* For more info, visit - [LambdaTest](https://www.lambdatest.com/?utm_source=github&utm_medium=repo&utm_campaign=python-selenium-sample)

