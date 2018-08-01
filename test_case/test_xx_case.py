import sys
import pytest
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.xx_page import BaiduSearchPage


class TestSearch:

    def test_baidu_search_case(self, browser):
        """ 百度搜索：pytest """
        page = BaiduSearchPage(browser, root_uri="https://www.baidu.com")
        page.get("/")
        page.search_input = "pytest"
        page.search_button.click()
        page.sleep(2)
        title = page.driver.title
        title2 = page.get_title()
        print(title2)
        assert title == "pytest_百度搜索"


if __name__ == '__main__':
    pytest.main(["-v", "test_xx_case.py"])
