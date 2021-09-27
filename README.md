# BStack_pyselenium_test_suite
This is a Selenium Test Suite written in python to be used on Browserstack Automate.

It is very basic a involves three tests on three diferent pages in browserstack namely
Main page - "https://www.browserstack.com"
Login page - "https://www.browserstack.com"
Home page - "https://www.browserstack.com/users/sign_in"

The first test visits the main page and go to the about us section and checks the names of
Browserstack founders.

The seconds test does a login to a test account on browserstack and logs out after successful login.

The third test enters invalid email id and check if the error message shown on the login page
is correct or not.


# Installing the required python packages
Simply run the following command
```
pip install -r requirements.txt

```

It is also important to set the environment variables `BROWSERSTACK_USERNAME` and
`BROWSERSTACK_ACCESS_KEY` with the correct values before running the test suite.


# How to run
To run this test suite simply clone the repository fire up the `run_test_suite.py` file
from the top directory as shown below
```
python PySeleniumTestSuite/Tests/run_test_suite.py

```

It runs the three aforementioned tests on 5 different browser/platform combinations in
paraller on Browserstack automate

Which browsers are being used can be seen in the
`PySeleniumTestSuite/Config/capabilities.py` file)


# Important note
The test suite uses an created on browserstack only for a free trial version which
only has 100 minutes of free testing.

So once that expires, this test suite will not run.


# How to hook up a new account to the test suite
Go to the `bashrc` or `zshrc` or whichever is applicable and update
`BROWSERSTACK_USERNAME` and `BROWSERSTACK_ACCESS_KEY` with new account's credentials

There is a class called `BstackCredentials` in `PySeleniumTestSuite/Config/test_params.py`
which takes the values of those credentials.



