import sys
import json
from time import sleep
import pytest
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.baidu_page import BaiduPage


def get_data(file_path):
    data = []
    with(open(file_path, "r")) as f:
        dict_data = json.loads(f.read())
        for i in dict_data:
            data.append(tuple(i.values()))
    return data


@pytest.mark.parametrize(
    "name, search_key",
    get_data("./data/data_file.json")
    )
def test_baidu_search(name, search_key, browser, base_url):
    page = BaiduPage(browser)
    page.get(base_url)
    page.search_input = search_key
    page.search_button.click()
    sleep(2)
    assert browser.title == search_key+"_百度搜索"
