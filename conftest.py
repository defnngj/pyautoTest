from selenium import webdriver
from selenium.webdriver import Remote
import pytest
import os


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
    try:
        file_name = name.split("test_case/")[1]
    except IndexError:
        file_name = name
    base_dir = str(os.getcwd()).replace('\\', '/').split('test_case/')[0]
    file_path = base_dir + "/test_report/image/" + file_name
    driver.get_screenshot_as_file(file_path)


# 启动浏览器
@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    if driver is None:
        driver = webdriver.Chrome()
        '''
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


if __name__ == "__main__":
    _capture_screenshot("test_case/test_baidu_search.test_search_python.png")
