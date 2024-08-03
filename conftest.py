import os
import pytest
from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options as CH_Options
from selenium.webdriver.firefox.options import Options as FF_Options
from config import RunConfig

# 项目目录配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = BASE_DIR + "/test_report/"


# 设置用例描述表头
def pytest_html_results_table_header(cells):
    cells.insert(2, '<th>Description</th>')
    cells.pop()


# 设置用例描述表格
def pytest_html_results_table_row(report, cells):
    cells.insert(2, f'<td>{report.description}</td>')
    cells.pop()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    用于向测试用例中添加用例的开始时间、内部注释，和失败截图等.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    report.description = description_html(item.function.__doc__)
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            case_path = report.nodeid.replace("::", "_") + ".png"
            if "[" in case_path:
                case_name = case_path.split("-")[0] + "].png"
            else:
                case_name = case_path
            capture_screenshots(case_name)
            img_path = "image/" + case_name.split("/")[-1]
            if img_path:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % img_path
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def description_html(desc):
    """
    将用例中的描述转成HTML对象
    :param desc: 描述
    :return:
    """
    if desc is None:
        return "No case description"
    desc_ = ""
    for i in range(len(desc)):
        if i == 0:
            pass
        elif desc[i] == '\n':
            desc_ += ";"
        else:
            desc_ += desc[i]
    
    desc_lines = desc_.split(";")

    head = f"<head><meta name='Content-Type' content='text/html; charset=latin1'></head>"

    # 构建 HTML 正文部分
    body = "<body>"
    for line in desc_lines:
        body += f"<p>{line}</p>"
    body += "</body>"

    # 完整的 HTML 文档
    desc_doc = f"<html>{head}{body}</html>"

    return desc_doc


def capture_screenshots(case_name):
    """
    配置用例失败截图路径
    :param case_name: 用例名
    :return:
    """
    global driver
    file_name = case_name.split("/")[-1]
    if RunConfig.NEW_REPORT is None:
        raise NameError('没有初始化测试报告目录')
    else:
        image_dir = os.path.join(RunConfig.NEW_REPORT, "image", file_name)
        RunConfig.driver.save_screenshot(image_dir)


# 启动浏览器
@pytest.fixture(scope='session', autouse=True)
def browser():
    """
    全局定义浏览器驱动
    :return:
    """
    global driver

    if RunConfig.driver_type == "chrome":
        # 本地chrome浏览器
        driver = webdriver.Chrome()
        driver.maximize_window()

    elif RunConfig.driver_type == "firefox":
        # 本地firefox浏览器
        driver = webdriver.Firefox()
        driver.maximize_window()

    elif RunConfig.driver_type == "chrome-headless":
        # chrome headless模式
        chrome_options = CH_Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(options=chrome_options)

    elif RunConfig.driver_type == "firefox-headless":
        # firefox headless模式
        firefox_options = FF_Options()
        firefox_options.headless = True
        driver = webdriver.Firefox(options=firefox_options)

    elif RunConfig.driver_type == "grid":
        # 通过远程节点运行
        chrome_options = CH_Options()
        driver = Remote(command_executor='http://localhost:4444/wd/hub', options=chrome_options)

    else:
        raise NameError("driver驱动类型定义错误！")

    RunConfig.driver = driver

    yield driver

    driver.quit()

    return driver


if __name__ == "__main__":
    capture_screenshots("test_dir/test_baidu_search.test_search_python.png")
