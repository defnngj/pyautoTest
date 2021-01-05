from poium import Page, Element


class BaiduPage(Page):
    search_input = Element(id_="kw", describe="搜索框")
    search_button = Element(id_="su", describe="搜索按钮")
    settings = Element(css="#s-usersetting-top", describe="设置")
    search_setting = Element(css="#s-user-setting-menu > div > a.setpref", describe="搜索设置")
    save_setting = Element(link_text="保存设置", describe="保存设置")
