import unittest


# 测试用例(组)类
class Parametrized_TestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
    inherit from this class.
    """

    def __init__(self, methodName='runTest', test_data=None, http=None,
                 db1_cursor=None, db2_cursor=None):
        super(Parametrized_TestCase, self).__init__(methodName)
        self.test_data = test_data
        self.http = http
        self.db1_cursor = db1_cursor
        self.db2_cursor = db2_cursor
