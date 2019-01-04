## Python unittest automation Lambdatest

Python selenium automation sample test for Lambdatest Cloud GRID.


## Install Python
 - Download the latest python build from https://www.python.org/downloads/
 - Make sure pip should installed. you can check using `pip --version`


### configuring test.
- Replace {username}  with your username 
- Replace {accessToken}  with your username 
- List of supported platfrom, browser, version can be found at https://www.lambdatest.com/capabilities-generator/


### Installating dependencies.
```bash
pip install selenium
export PYTHONWARNINGS="ignore:Unverified HTTPS request"   //Disable ssl warning
```

### Executing test
```bash
python google-serach-lambdatest.py
```
