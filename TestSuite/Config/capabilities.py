

# This tells browserstack which browser on which platform
# to use to run the test suite


class Capabilities():
    caps = [{
            'bstack:options' : {
                "os" : "Windows",
                "osVersion" : "10",
                "local" : "false",
                "seleniumVersion" : "3.141.0",
            },
            "browserName" : "Chrome",
            "browserVersion" : "latest",
            "build": "BStack_pyselenium_testbuild_012"
        },
        {
            'bstack:options': {
                "os": "Windows",
                "osVersion": "10",
                "local": "false",
                "seleniumVersion": "3.5.2",
            },
            "browserName": "Edge",
            "browserVersion": "latest",
            "build": "BStack_pyselenium_testbuild_012"
        },
        {
            'bstack:options': {
                "os": "Windows",
                "osVersion": "8.1",
                "local": "false",
                "seleniumVersion": "3.141.0",
            },
            "browserName": "Chrome",
            "browserVersion": "90.0",
            "build": "BStack_pyselenium_testbuild_012"
        },
        {
            'bstack:options': {
                "os": "Windows",
                "osVersion": "8.1",
                "local": "false",
                "seleniumVersion": "3.10.0",
            },
            "browserName": "Firefox",
            "browserVersion": "91.0",
            "build": "BStack_pyselenium_testbuild_012"
        },
        {
            'bstack:options': {
                "os": "Windows",
                "osVersion": "10",
                "local": "false",
                "seleniumVersion": "3.14.0",
            },
            "browserName": "Firefox",
            "browserVersion": "latest",
            "build": "BStack_pyselenium_testbuild_012"
        }
    ]
