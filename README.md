## Python unittest automation Lambdatest

Python selenium automation sample test for [LambdaTest](https://www.lambdatest.com/) cloud-based Selenium Grid.


## Install Python
 - Download the latest python build from https://www.python.org/downloads/
 - Make sure pip should installed. you can check using `pip --version`


### Configuring Test
- Replace {username}  with your username 
- Replace {accessToken}  with your username 
- List of supported platfrom, browser, version can be found at https://www.lambdatest.com/capabilities-generator/


### Installating Dependencies
```bash
pip install selenium
export PYTHONWARNINGS="ignore:Unverified HTTPS request"   //Disable ssl warning
```

### Executing Test
```bash
python google-serach-lambdatest.py
```
## About LambdaTest
[LambdaTest](https://www.lambdatest.com/) is a cloud based selenium grid infrastructure that can help you run automated cross browser compatibility tests on 2000+ different browser and operating system environments. All test data generated during testing including Selenium command logs, screenshots generated in testing, video logs, selenium logs, network logs, console logs, and metadata logs can be extracted using [LambdaTest automation APIs](https://www.lambdatest.com/support/docs/api-doc/). This data can then be used for creating custom reports.
