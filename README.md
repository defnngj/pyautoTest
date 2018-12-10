# pyautoTest Web UI 自动化项目

#### 特点：
* 全局配置浏览器启动/关闭。
* 测试用例运行失败自动截图。
* 测试用例运行失败可以重跑。
* 测试数据参数化。

#### 安装：

```
$ pip install -r requirements.txt

$ pip install -i https://test.pypi.org/simple/ selenium-page-objects
```
#### 配置：
在 __conftest.py__ 文件配置

```python
# 配置浏览器驱动类型。
driver = "chrome"

# 配置运行的 URL
url = "https://www.baidu.com"

# 失败重跑次数
rerun = "3"

# 运行测试用例的目录或文件
cases_path = "./test_dir/"
```

#### 运行：

```shell
$ python3 run_tests.py  (回归模式，生成HTML报告)
$ python3 run_tests.py --method debug  (调试模式)
```
