# Python-Selenium-Sample

![MSTest](https://opengraph.githubassets.com/8039186e9aebcc17be88d53ac4b85364a56f6aae503057e0ebf36dfcc5b5cc32/LambdaTest/python-selenium-sample)

## Prerequisites

1. Install pip and python.

```
sudo apt install python-pip
sudo apt install python
```

2. The recommended way to run your tests would be in virtualenv. It will isolate the build from other setups you may have running and ensure that the tests run with the specified versions of the modules specified in the requirements.txt file.

```
pip install virtualenv
```

## Steps to Run your First Test

Step 1. Clone the Python-Selenium-Sample Repository.

```
git clone https://github.com/LambdaTest/python-selenium-sample
```

Step 2. Next we create and Activate the virtual environment in the Python-Selenium-Sample folder.

```
virtualenv venv
source venv/bin/activate
```

Step 3. Then install required packages.

```
pip install -r requirements.txt
```

Step 4. Inside Python-Selenium-Sample folder, export the Lambda-test Credentials. You can get these from your automation dashboard.

<p align="center">
   <b>For Linux/macOS:</b>
   
```
export LT_USERNAME="YOUR_USERNAME"
export LT_ACCESS_KEY="YOUR ACCESS KEY"
```

<p align="center">
   <b>For Windows:</b>
   
```
set LT_USERNAME="YOUR_USERNAME"
set LT_ACCESS_KEY="YOUR ACCESS KEY"
```

Step 5. To run your first test.
```
python lambdatest.py
```

## About LambdaTest

[LambdaTest](https://www.lambdatest.com/) is a cloud based selenium grid infrastructure that can help you run automated cross browser compatibility tests on 2000+ different browser and operating system environments. LambdaTest supports all programming languages and frameworks that are supported with Selenium, and have easy integrations with all popular CI/CD platforms. It's a perfect solution to bring your [selenium automation testing](https://www.lambdatest.com/selenium-automation) to cloud based infrastructure that not only helps you increase your test coverage over multiple desktop and mobile browsers, but also allows you to cut down your test execution time by running tests on parallel.