import unittest
import json
from selenium import webdriver
from parameterized import parameterized, param
from baidu_page import BaiduPage
from common import json_to_data


class BaiduTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        global dd
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @parameterized.expand([
        ('', '123', '请输入帐号'),
        ('user', '', '请输入密码'),
        ('error', 'error', '帐号或密码错误'),
        ('admin', 'admin123', 'admin你好'),
        ('guest', 'guest123', 'guest你好')
    ])
    def test_search(self, name, username, password, assert_info):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.find_element_by_id("inputUsername").send_keys(username)
        self.driver.find_element_by_id("inputPassword").send_keys(password)
        self.driver.find_element_by_id("Login").click()


if __name__ == '__main__':
    unittest.main()


