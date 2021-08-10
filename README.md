# pyautoTest Web UI 自动化项目

### 特点

* 全局配置浏览器启动/关闭。
* 测试用例运行失败自动截图。
* 测试用例运行失败可以重跑。
* 测试数据参数化。

### 安装

```shell
$ pip install -r requirements.txt
```

注：安装```requirements.txt```指定依赖库的版本，这是经过测试的，有时候新的版本可会有错。

### 配置

在 `config.py` 文件配置

```python
class RunConfig:
    """
    运行测试配置
    """
    # 配置浏览器驱动类型。
    driver_type = "chrome"

    # 失败重跑次数
    rerun = "3"

    # 当达到最大失败数，停止执行
    max_fail = "5"

    # 运行测试用例的目录或文件
    cases_path = "./test_dir/"
```

### 运行

**不支持在编辑器（pycharm/ VS code ...）中运行，请在 cmd（windows）/终端(Linux)下执行。**

```shell
$ python run_tests.py  (回归模式，生成HTML报告)
$ python run_tests.py -m debug  (调试模式)
```

### 警告提示

`conftest.py` 文件有一行在 pycharm 中提示错误：

```python
from py.xml import html
```

* 原因

从源代码判断，py名称空间中的属性是动态创建的，这就是为什么静态分析工具pylint (pycharm)无法识别它们的原因:

```py
apipkg.initpkg(__name__, attr={'_apipkg': apipkg}, exportdefs={
    ...
    # small and mean xml/html generation
    'xml' : {
        '__doc__'            : '._xmlgen:__doc__',
        'html'               : '._xmlgen:html',
        'Tag'                : '._xmlgen:Tag',
        'raw'                : '._xmlgen:raw',
        'Namespace'          : '._xmlgen:Namespace',
        'escape'             : '._xmlgen:escape',
    },
})
```

所以，是pycharm 不够智能！你可以忽略这个错误。
