# coding=utf-8
import pytest
import time
import click

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


@click.command()
@click.option('-mode', default="run", help="输入运行模式：run 或 debug")
def run(mode):
    if mode == "run":
        now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
        pytest.main(["-s", "./test_case/",
                     "--html", "./test_report/" + now_time + "report.html",
                     "--self-contained-html",
                     "--reruns", "3"])
    elif mode == "debug":
        print("debug模式运行测试用例：")
        pytest.main(["-v", "./test_case/"])
        print("运行结束！！")


if __name__ == '__main__':
    run()
