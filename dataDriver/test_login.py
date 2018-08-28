import pytest
from selenium import webdriver
from time import sleep


class TestLogin:
    """登陆测试demo"""

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.url = "http://127.0.0.1:8000/"
        cls.driver.implicitly_wait(10)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def user_login(self, username, password):
        driver = self.driver
        driver.get(self.url)
        driver.find_element_by_id("inputUsername").send_keys(username)
        driver.find_element_by_id("inputPassword").send_keys(password)
        driver.find_element_by_id("Login").click()

    def test_login_01(self, config_data):
        self.user_login(config_data["username"], config_data["password"])
        tips = self.driver.find_element_by_id("tips").text
        assert tips == '请输入帐号'

    def test_login_02(self, config_data):
        self.user_login(config_data["username"], config_data["password"])
        tips = self.driver.find_element_by_id("tips").text
        assert tips == '请输入密码'

    def test_login_03(self, config_data):
        self.user_login(config_data["username"], config_data["password"])
        tips = self.driver.find_element_by_id("tips").text
        assert tips == '帐号或密码错误'

    def test_login_04(self, config_data):
        self.user_login(config_data["username"], config_data["password"])
        sleep(2)
        tips = self.driver.find_element_by_id("user").text
        assert tips == 'admin你好'


# def test_one(config_data):
#     assert config_data >= 0
#
#
# def test_two(config_data):
#     assert config_data == 'split'
#
#
# def test_three(config_data):
#     assert config_data['three'] == 3
#
#
# def test_four(config_data):
#     assert config_data['four'] == 4
#

if __name__ == '__main__':
    pytest.main(["-v", "test_login.py"])
