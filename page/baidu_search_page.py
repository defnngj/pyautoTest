# coding=utf-8
from .common import WebDriver

"""
废弃
"""
class BaiduSearchPage(WebDriver):
    """
    百度首页
    """
    page_url = '/'

    # 百度输入框
    def search_input(self, search_key):
        self.type("#kw", search_key)

    # 百度按钮
    def search_button(self):
        self.click("#su")

    # 搜索标题
    def search_title(self):
        return self.get_title()

    # 设置
    def settings(self):
        self.click("link_text=>设置")

    # 搜索设置
    def search_setting(self):
        self.click(".setpref")

    # 保存设置
    def save_setting(self):
        self.click(".prefpanelgo")

    def get_alert(self):
        text = self.get_alert_text()
        #self.accept_alert()   # 接受警告框
        return text
