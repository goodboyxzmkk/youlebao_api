import unittest
from selenium import webdriver


class B(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        B.dr = webdriver.Chrome()

    def get_screenshot_as_file(self, func):
        def wrapper(self):
            try:
                func(self)
            except:
                self.dr.get_screenshot_as_file('./{}.png'.format(func.__name__))

        return wrapper

    @get_screenshot_as_file
    def test1(self):
        self.assertTrue(True)
        self.dr = B.dr
        self.dr.get('http://www.baidu.com')
        assert False

    @get_screenshot_as_file
    def test2(self):
        assert True

    @classmethod
    def tearDownClass(cls):
        B.dr.quit()


unittest.main()
