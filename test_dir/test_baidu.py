import sys
from time import sleep
import pytest
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.baidu_page import BaiduPage


class TestSearch:
    """百度搜索"""

    def test_baidu_search_case(self, browser, base_url):
        """
        名称：百度搜索"pytest"
        步骤：
        1、打开浏览器
        2、输入"pytest"关键字
        3、点击搜索按钮
        检查点：
        * 检查页面标题是否包含关键字。
        """
        page = BaiduPage(browser)
        page.get(base_url)
        page.search_input = "pytest"
        page.search_button.click()
        sleep(2)
        assert browser.title == "pytest_百度搜索"

    @pytest.mark.parametrize(
        "name, search_key",
        [("1", "Selenium"),
         ("2", "pytest文档"),
         ("3", "pytest-html"),
         ],
         ids=["case1", "case2", "case3"]
        )
    def test_baidu_search(self, name, search_key, browser, base_url):
        page = BaiduPage(browser)
        page.get(base_url)
        page.search_input = search_key
        page.search_button.click()
        sleep(2)
        assert browser.title == search_key+"_百度搜索"


class TestSearchSettings:
    """百度搜索设置"""

    def test_baidu_search_setting(self, browser, base_url):
        """
        名称：百度搜索设置
        步骤：
        1、打开百度浏览器
        2、点击设置链接
        3、在下拉框中"选择搜索"
        4、点击"保存设置"
        5、对弹出警告框保存
        检查点：
        * 检查是否弹出提示框
        """
        page = BaiduPage(browser)
        page.get(base_url)
        page.settings.click()
        page.search_setting.click()
        sleep(2)
        page.save_setting.click()
        alert_text = page.get_alert_text
        page.accept_alert()
        assert alert_text == "已经记录下您的使用偏好"


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_baidu.py"])
    # pytest.main(["-v", "-s", "test_baidu.py::TestSearch::test_baidu_search_case"])
    # pytest.main(["-v", "-s", "test_baidu.py::TestSearch"])
    # pytest.main(["-v", "-s", "test_baidu.py::TestSearchSettings"])
