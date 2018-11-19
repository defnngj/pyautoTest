# pyautoTest Web UI 自动化项目

#### 特点：
* 整个测试过程只需要打开/关闭一次浏览器，大大缩短测试时间。

* 测试用例运行失败自动截图。

* 测试用例运行失败可以重跑。

* 测试数据参数化。

#### 依赖库：
__selenium：__ Web自动化测试库
https://pypi.python.org/pypi/selenium

__selenium-page-objects：__ 实现page层的封装（需要单独安装）

https://github.com/defnngj/selenium_page_objects

__pytest：__ 单元测试框架
https://pypi.python.org/pypi/pytest

__pytest-html：__ 生成html测试报告
https://pypi.python.org/pypi/pytest-html

__pytest-rerunfailures：__ 失败重跑
https://pypi.python.org/pypi/pytest-rerunfailures

#### 安装：

```
$ pip install -r requirements.txt

$ pip install -i https://test.pypi.org/simple/ selenium-page-objects
```

#### 运行：

```
python run_test.py
```
