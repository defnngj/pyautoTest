import sys
from time import sleep
import pytest
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.baidu_page import BaiduPage


class TestSearch:
    """百度搜索"""

    def test_baidu_search_case(self, browser, base_url):
        """ 百度搜索：pytest """
        page = BaiduPage(browser)
        page.get(base_url)
        page.search_input.send_keys("pytest")
        page.search_button.click()
        sleep(2)
        assert browser.title == "pytest_百度搜索222"

    @pytest.mark.parametrize(
        "name, search_key",
        [("1", "Selenium"),
         ("2", "pytest文档"),
         ("3", "pytest-html"),
         ],
         ids=["case1", "case2", "case3"]
        )
    def test_baidu_search(self, name, search_key, browser, base_url):
        """百度搜索 --参数化"""
        page = BaiduPage(browser)
        page.get(base_url)
        page.search_input.send_keys(search_key)
        page.search_button.click()
        sleep(2)
        assert browser.title == search_key+"_百度搜索"


class TestSearchSettings:
    """百度搜索设置"""

    def test_baidu_search_setting(self, browser, base_url):
        """百度搜索设置"""
        page = BaiduPage(browser)
        page.get(base_url)
        page.settings.click()
        page.search_setting.click()
        sleep(2)
        page.save_setting.click()
        alert_text = browser.switch_to.alert.text
        browser.switch_to.alert.accept()
        assert alert_text == "已经记录下您的使用偏好"


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_baidu.py"])
    # pytest.main(["-v", "-s", "test_baidu.py::TestSearch::test_baidu_search_case"])
    # pytest.main(["-v", "-s", "test_baidu.py::TestSearch"])
    # pytest.main(["-v", "-s", "test_baidu.py::TestSearchSettings"])
