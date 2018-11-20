# coding=utf-8
import os
import time
import shutil
from os.path import dirname, abspath

import click
import pytest

from conftest import rerun, cases_path

'''
说明：
1、用例创建原则，测试文件名必须以“test”开头，测试函数必须以“test”开头。
2、用例运行策略，
*  指定运行目录或文件，例: "./test_case/" , "/test_case/test_demo.py"
*  -s  关闭捕捉，不显示测试运行百分比
*  -v  参数增加测试用例冗长，显示详细测试结果。
*  --html  指定测试报告目录及文件名。
*  --self-contained-html 表示创建独立的测试报告。
*  --reruns 3   指定用例失败重跑次数。
3、运行方式：
> python run_tests.py  # run模式，生成HTML测试报告 
> python run_tests.py  -mode debug  # debug模式, 不生成报告
'''


def init_env(now_time):
    """初始化测试报告目录"""
    base_path = dirname(abspath(__file__))
    report_path = base_path + "/test_report/"
    image_path = base_path + "/test_report/image/"

    report = os.path.exists(report_path + "report.html")
    if report is True:
        with open("time.txt", "r") as f:
            last_time = f.read()
            shutil.move(report_path + "report.html", report_path + last_time + "/report.html")
            image_folder = os.path.exists(image_path)
            if image_folder is True:
                for image in os.listdir(image_path):
                    shutil.move(image_path + image, report_path + last_time + "/image/" + image)

    with open("time.txt", "w") as f:
        f.write(now_time)

    os.mkdir(report_path + now_time)
    os.mkdir(report_path + now_time + "/image")


@click.command()
@click.option('-mode', default="run", help="输入运行模式：run 或 debug")
def run(mode):
    if mode == "run":
        print("回归模式，执行完成生成测试结果")
        now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
        init_env(now_time)
        pytest.main(["-s", cases_path,
                     "--html", "./test_report/report.html",
                     "--junit-xml=./test_report/" + now_time + "/junit-xml.xml",
                     "--self-contained-html",
                     "--reruns", rerun])
    elif mode == "debug":
        print("debug模式运行测试用例：")
        pytest.main(["-v", cases_path])
        print("运行结束！！")


if __name__ == '__main__':
    run()
