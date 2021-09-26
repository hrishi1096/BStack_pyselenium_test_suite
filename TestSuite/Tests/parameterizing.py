import unittest

class ParameterizedTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', param=None):
        super(ParameterizedTestCase, self).__init__(methodName)
        self.param = param

    @staticmethod
    def parameterize(tests_class, param=None):
        tests_loader = unittest.TestLoader()
        tests_names = tests_loader.getTestCaseNames(tests_class)
        suite = unittest.TestSuite()
        for name in tests_names:
            suite.addTest(tests_class(name, param=param))
        return suite

