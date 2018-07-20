# coding=utf-8
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from page_obj.baidu_search_page import BaiduSearchPage
from time import sleep
import pytest


class TestSearch:

    # 百度搜索 -- 单用例
    def test_baidu_search_case(self, browser):
        bd = BaiduSearchPage(browser)
        bd.open()
        bd.search_input("pytest")
        bd.search_button()
        sleep(1)
        title = bd.search_title()
        assert title == "pytest_百度搜索"

    # 百度搜索 --参数化
    @pytest.mark.parametrize(
        "name, search_key",
        [("1", "Selenium"),
         ("2", "pytest文档"),
         ("3", "pytest-html"),
         ],
         ids=["case1", "case2", "case3"]
        )
    def test_baidu_search(self, name, search_key, browser):
        bd = BaiduSearchPage(browser)
        bd.open()
        bd.search_input(search_key)
        bd.search_button()
        sleep(2)
        title = bd.search_title()
        assert title == search_key+"_百度搜索"


class TestSearchSettings:

    # 百度搜索设置
    def test_baidu_search_setting(self, browser):
        bd = BaiduSearchPage(browser)
        bd.open()
        bd.settings()
        bd.search_setting()
        bd.save_setting()
        assert bd.get_alert() == "已经记录下您的使用偏好"


if __name__ == "__main__":
    pytest.main(["-s", "test_baidu_search.py"])