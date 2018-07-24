import unittest
import json
from selenium import webdriver
from parameterized import parameterized, param
from baidu_page import BaiduPage
from common import json_to_data


class BaiduTest(unittest.TestCase):

    dd = None

    @classmethod
    def setUpClass(cls):
        global dd
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        with open("./JsonData.json") as f:
            json_str = f.read()
        dd = json_to_data(json_str)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @parameterized.expand(dd["test_search"])
    def test_search(self, name, search_key, assert_title):
        bd = BaiduPage(self.driver)
        bd.search_input(search_key)
        bd.search_button()


if __name__ == '__main__':
    unittest.main()


