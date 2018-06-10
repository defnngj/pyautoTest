import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from page_obj.baidu_page import BaiduPage
from time import sleep
import pytest


def test_baidu_search_setting(browser):
    bd = BaiduPage(browser)
    bd.open()
    bd.setings()
    bd.search_setting()
    bd.save_seting()
    assert bd.get_alert() == "已经记录下您的使用偏好"



if __name__ == "__main__":
    pytest.main(["-s", "test_baidu_settings.py"])