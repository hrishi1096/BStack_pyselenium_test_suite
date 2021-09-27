

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
            "name" : "Win10_chrome_latest_parallel_test",
            "build": "BStack_pyselenium_testbuild_015"
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
            "name": "Win10_edge_latest_parallel_test",
            "build": "BStack_pyselenium_testbuild_015"
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
            "name": "Win8.1_chrome_90.0_parallel_test",
            "build": "BStack_pyselenium_testbuild_015"
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
            "name": "Win8.1_firefox_91.0_parallel_test",
            "build": "BStack_pyselenium_testbuild_015"
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
            "name": "Win10_firefox_latest_parallel_test",
            "build": "BStack_pyselenium_testbuild_015"
        }
    ]
