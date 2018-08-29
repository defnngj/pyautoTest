import unittest
from selenium import webdriver
from ddt import ddt, file_data, data
from time import sleep


@ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.url = "http://127.0.0.1:8000/"
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def user_login(self, username, password):
        driver = self.driver
        driver.get(self.url)
        driver.find_element_by_id("inputUsername").send_keys(username)
        driver.find_element_by_id("inputPassword").send_keys(password)
        driver.find_element_by_id("Login").click()

    @file_data("./test_data/test_ddt_file.json")
    def test_login(self, username, password, assert_text):
        self.user_login(username, password)
        if username == "admin":
            sleep(2)
            tips = self.driver.find_element_by_id("user").text
            self.assertEqual(tips, assert_text)
        else:
            tips = self.driver.find_element_by_id("tips").text
            self.assertEqual(tips, assert_text)

    @data(["", "123", "请输入帐号"],
          ["user", "", "请输入密码"],
          ["error", "error", "帐号或密码错误"],
          ["admin", "admin123456", "admin你好"],
    )
    def test_login_2(self, username, password, assert_text):
        self.user_login(username, password)
        if username == "admin":
            sleep(2)
            tips = self.driver.find_element_by_id("user").text
            self.assertEqual(tips, assert_text)
        else:
            tips = self.driver.find_element_by_id("tips").text
            self.assertEqual(tips, assert_text)


if __name__ == '__main__':
    unittest.main()
