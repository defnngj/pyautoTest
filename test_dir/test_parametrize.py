"""
@author:  虫师
@data: 2019-10-17
@function pytest 参数使用
"""
import sys
import json
from time import sleep
import pytest
from os.path import dirname, abspath

base_path = dirname(dirname(abspath(__file__)))
sys.path.insert(0, base_path)
from page.baidu_page import BaiduPage


@pytest.mark.parametrize(
    "name, search_key",
    [("1", "Selenium"),
     ("2", "pytest文档"),
     ("3", "pytest-html"),
     ],
    ids=["case1", "case2", "case3"]
)
def test_baidu_search(name, search_key, browser, base_url):
    """百度搜索参数化"""
    page = BaiduPage(browser)
    page.get(base_url)
    page.search_input = search_key
    page.search_button.click()
    sleep(2)
    assert browser.title == search_key + "_百度搜索"


def get_data(file_path):
    """
    读取参数化文件
    :param file_path:
    :return:
    """
    data = []
    with(open(file_path, "r")) as f:
        dict_data = json.loads(f.read())
        for i in dict_data:
            data.append(tuple(i.values()))
    return data


@pytest.mark.parametrize(
    "name, search_key",
    get_data(base_path + "/test_dir/data/data_file.json")
)
def test_baidu_search(name, search_key, browser, base_url):
    page = BaiduPage(browser)
    page.get(base_url)
    page.search_input = search_key
    page.search_button.click()
    sleep(2)
    assert browser.title == search_key + "_百度搜索"
