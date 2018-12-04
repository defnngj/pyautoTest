# coding=utf-8
import os
import time
import shutil
import pytest
import click
from conftest import REPORT_DIR, IMAGE_DIR
from conftest import cases_path, rerun

'''
说明：
1、用例创建原则，测试文件名必须以“test”开头，测试函数必须以“test”开头。
2、用例运行策略，
*  -s 指定运行目录或文件，例: -s  ./test_case/ ,  -s  /test_case/test_demo.py
*  --html  指定测试报告目录及文件名。
*  --self-contained-html 表示创建独立的测试报告。
*  --reruns 3   指定用例失败重跑次数。
3、运行方式
*  > python3 run_tests.py  (回归模式，生成HTML报告)
*  > python3 run_tests.py --method debug  (调试模式)
'''


def last_report_time():
    """
    获取上一份报告的目录名（即运行时间：2018_11_21_17_40_44）
    """
    files = os.listdir(REPORT_DIR)
    files.sort()
    try:
        return files[-3]
    except IndexError:
        return None


def init_env(now_time):
    """
    初始化测试报告目录
    """
    image = os.path.exists(IMAGE_DIR)
    if image is not True:
        os.mkdir(IMAGE_DIR)

    report = os.path.exists(REPORT_DIR + "report.html")
    if report is True:
        r_tine = last_report_time()
        shutil.move(REPORT_DIR + "report.html", REPORT_DIR + r_tine + "/report.html")
        image_folder = os.path.exists(IMAGE_DIR)
        if image_folder is True:
            for image_file in os.listdir(IMAGE_DIR):
                shutil.move(IMAGE_DIR + image_file, REPORT_DIR + r_tine + "/image/" + image_file)

    os.mkdir(REPORT_DIR + now_time)
    os.mkdir(REPORT_DIR + now_time + "/image")


@click.command()
@click.option('--method', default=None)
def run(method):
    if method is None:
        print("回归模式，执行完成生成测试结果")
        now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
        init_env(now_time)
        pytest.main(["-s", "-v", cases_path,
                     "--html=" + REPORT_DIR + "report.html",
                     "--junit-xml=" + REPORT_DIR + now_time + "/junit-xml.xml",
                     "--self-contained-html",
                     "--reruns", rerun])
    elif method == "debug":
        print("debug模式运行测试用例：")
        pytest.main(["-v", "-s", cases_path])
        print("运行结束！！")


if __name__ == '__main__':
    run()
