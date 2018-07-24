import unittest
from selenium import webdriver
from parameterized import parameterized
import json


class BaiduTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        with open("./JsonData.json") as f:
            json_str = f.read()
        test_data = json.dumps(json_str)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @parameterized([
        (2, 2, 4),
        (2, 3, 8),
        (1, 9, 1),
        (0, 9, 0),
    ])
    def test_search(self):
        pass



if __name__ == '__main__':
    unittest.main()


