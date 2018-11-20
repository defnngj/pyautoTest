import os
from os.path import abspath, dirname
from datetime import datetime

import pytest
from py.xml import html
from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options as CH_Options
from selenium.webdriver.firefox.options import Options as FF_Options


############################

# 配置浏览器驱动类型。
driver = "grid"

# 配置运行的 URL
url = "https://www.baidu.com"

# 失败重跑次数
rerun = 0

# 运行测试用例的目录或文件
cases_path = "./test_case/"

############################


# 定义基本测试环境
@pytest.fixture(scope='function')
def base_url():
    global url
    return url


# 描述和运行时间表头
@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))
    cells.insert(1, html.th('Time', class_='sortable time', col='time'))
    cells.pop()


# 描述和运行时间表格
@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.insert(1, html.td(datetime.utcnow(), class_='col-time'))
    cells.pop()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    用于向测试用例中添加用例的开始时间、内部注释，和失败截图等.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name_ = report.nodeid.replace("::", "_") + ".png"
            if "[" in file_name_:
                file_name = file_name_.split("-")[0] + "].png"
            else:
                file_name = file_name_
            _capture_screenshot(file_name)
            file_name = "image/" + file_name.split("/")[-1]
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                            'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


# 配置用例失败截图路径
def _capture_screenshot(name):
    global driver
    file_name = name.split("/")[-1]
    base_path = dirname(abspath(__file__))
    image_path = base_path + "/test_report/image/"

    image_folder = os.path.exists(image_path)
    if image_folder is not True:
        os.mkdir(image_path)

    driver.save_screenshot(image_path + file_name)


# 启动浏览器
@pytest.fixture(scope='session', autouse=True)
def browser():
    """
    全局定义浏览器驱动
    :return:
    """
    global driver

    if driver == "chrome":
        # 本地chrome浏览器
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)

    elif driver == "firefox":
        # 本地firefox浏览器
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)

    elif driver == "chrome-headless":
        # chrome headless模式
        chrome_options = CH_Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(chrome_options=chrome_options)

    elif driver == "firefox-headless":
        # firefox headless模式
        firefox_options = FF_Options()
        firefox_options.headless = True
        driver = webdriver.Firefox(firefox_options=firefox_options)

    elif driver == "grid":
        # 通过远程节点运行
        driver = Remote(command_executor='http://10.2.16.182:4444/wd/hub',
                        desired_capabilities={
                              "browserName": "chrome",
                        })
        driver.set_window_size(1920, 1080)

    else:
        raise NameError("driver驱动类型定义错误！")

    return driver


# 关闭浏览器
@pytest.fixture(scope="session", autouse=True)
def browser_close():
    yield driver
    driver.quit()
    print("test end!")


if __name__ == "__main__":
    _capture_screenshot("test_case/test_baidu_search.test_search_python.png")
