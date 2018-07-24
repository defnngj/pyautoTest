
class BasePage(object):

    def __init__(self, driver, url=None):
        self.driver = driver
        default_url = "http://www.baidu.com"
        if url is None:
            self.driver.get(default_url)
        else:
            self.driver.get(url)

    def by_id(self, id_):
        return self.driver.find_element_by_id(id_)


class BaiduPage(BasePage):

    def search_input(self, search_key):
        self.by_id("kw").send_keys(search_key)

    def search_button(self):
        self.by_id("su").click()

