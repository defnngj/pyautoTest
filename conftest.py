from selenium import webdriver
from selenium.webdriver import Remote
import pytest
from os.path import abspath, dirname
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from py.xml import html


driver = None


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
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
            file_name = file_name.replace('test_case/', 'image/')
            # image/test_baidu_search.py_test_baidu_search1.png
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                            'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


# 配置用例失败截图路径
def _capture_screenshot(name):
    print(name)
    try:
        file_name = name.split("test_case/")[1]
        print(file_name)
    except IndexError:
        file_name = name
    base_dir = dirname(abspath(__file__))
    file_path = base_dir + "/test_report/image/" + file_name
    driver.save_screenshot(file_path)


# 启动浏览器
@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    if driver is None:
        driver = webdriver.Chrome()
        '''
        # chrome-headless 模式
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        # 远程模式
        driver = Remote(command_executor='http://192.168.44.129:5557/wd/hub',
                        desired_capabilities={
                              "browserName": "firefox",
                        })
        '''
    return driver


# 关闭浏览器
@pytest.fixture(scope="session", autouse=True)
def browser_close():
    yield driver
    driver.quit()
    print("test end!")


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


# 描述和运行时间输出
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)


if __name__ == "__main__":
    _capture_screenshot("test_case/test_baidu_search.test_search_python.png")
