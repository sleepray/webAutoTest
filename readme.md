# web-UI自动化测试示例

----

## 框架设计


* pytest
* selenium
* POM模型

----

## 目录结构

    common                 ——公共类
    Page                   ——基类
    PageElements           ——页面元素类
    PageObject             ——页面对象类
    TestCase               ——测试用例
    conf.py                ——各种固定配置
    conftest.py            ——pytest胶水文件
    pytest.ini             ——pytest配置文件

----

## 运行

* `cd 项目目录`

* 在命令行输入`pytest`即可运行

