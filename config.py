import os
PRO_PATH = os.path.dirname(os.path.abspath(__file__))

#配置文件or参数需要放到一个class类里的属性
class RunConfig:
    """
    运行测试配置
    """
    # 运行测试用例的目录文件
    cases_path = os.path.join(PRO_PATH, "test_dir", "test_baidu.py")
    # 运行测试用例的目录文件夹下的所有测试用例
    cases_path = os.path.join(PRO_PATH, "test_dir")

    # 配置浏览器驱动类型(chrome/chrome-headless/grid)。
    driver_type = "chrome"

    # 失败重跑次数
    rerun = "1"

    # 当达到最大失败数，停止执行
    max_fail = "5"

    # 浏览器驱动（不需要修改）
    driver = None

    # 报告路径（不需要修改）
    NEW_REPORT = None
