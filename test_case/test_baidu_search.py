# coding=utf-8
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.baidu_search_page import BaiduSearchPage
import pytest


class TestSearch:

    def test_baidu_search_case(self, browser):
        """ 百度搜索：pytest """
        page = BaiduSearchPage(browser)
        page.search_input("pytest")
        page.search_button()
        page.sleep(1)
        title = page.search_title()
        assert title == "pytest_百度搜索"

    @pytest.mark.parametrize(
        "name, search_key",
        [("1", "Selenium"),
         ("2", "pytest文档"),
         ("3", "pytest-html"),
         ],
         ids=["case1", "case2", "case3"]
        )
    def test_baidu_search(self, name, search_key, browser):
        """百度搜索 --参数化"""
        page = BaiduSearchPage(browser)
        page.search_input(search_key)
        page.search_button()
        page.sleep(2)
        title = page.search_title()
        assert title == search_key+"_百度搜索"


class TestSearchSettings:

    def test_baidu_search_setting(self, browser):
        """百度搜索设置"""
        page = BaiduSearchPage(browser, url="http://www.baidu.com", timeout=2)
        page.settings()
        page.search_setting()
        page.save_setting()
        page.sleep(2)
        assert page.get_alert() == "已经记录下您的使用偏好"


if __name__ == "__main__":
    pytest.main(["-s", "test_baidu_search.py::TestSearchSettings"])
