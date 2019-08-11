# pyautoTest Web UI 自动化项目

#### 特点：

* 全局配置浏览器启动/关闭。
* 测试用例运行失败自动截图。
* 测试用例运行失败可以重跑。
* 测试数据参数化。

#### 安装：

```shell
$ pip install -r requirements.txt
```
注：安装```requirements.txt```指定依赖库的版本，这是经过测试的，有时候新的版本可会有错。

#### 配置：

在 __conftest.py__ 文件配置

```python
# 配置浏览器驱动类型。
driver_type = "chrome"

# 配置运行的 URL
url = "https://www.baidu.com"

# 失败重跑次数
rerun = "3"

# 当达到最大失败数，停止执行
max_fail = "5"

# 运行测试用例的目录或文件
cases_path = "./test_dir/"
```

#### 运行：

```shell
$ python run_tests.py  (回归模式，生成HTML报告)
$ python run_tests.py -m debug  (调试模式)
```
注： 不支持在编辑器中运行，请在 cmd（windows）/终端(Linux)下执行。
