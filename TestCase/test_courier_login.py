#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import pytest
import allure
from utils.times import sleep
from utils.logger import log

from common.readconfig import ini
from page_object.loginpage import LoginPage


@allure.feature("测试courier登录")
class TestLogin:
    @pytest.fixture(scope='session', autouse=True)
    def open_devops(self, drivers):
        """打开courier"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("输入错误用户名密码")
    def test_001(self, drivers):
        """登录-输入错误用户名密码"""
        login = LoginPage(drivers)
        login.input_username_login('admin')
        login.input_password_login('123456')
        login.click_login()
        result = re.search(r'密码错误', login.get_source)
        log.info(result)
        assert result

    @allure.story("不输入用户名密码")
    def test_002(self, drivers):
        """登录-不输入用户名密码"""
        login = LoginPage(drivers)
        login.input_clear("用户名")
        login.input_clear("密码")
        login.click_login()
        result = re.search(r'请输入用户名', login.get_source)
        log.info(result)
        assert result

    @allure.story("不输入密码")
    def test_003(self, drivers):
        """登录-不输入密码"""
        login = LoginPage(drivers)
        login.input_clear("用户名")
        login.input_clear("密码")
        login.input_username_login('admin')
        login.click_login()
        result = re.search(r'请输入密码', login.get_source)
        log.info(result)
        assert result

    @allure.story("输入正确用户名密码")
    def test_004(self, drivers):
        """登录-输入正确用户名密码"""
        login = LoginPage(drivers)
        login.input_clear("用户名")
        login.input_clear("密码")
        login.input_username_login('admin')
        login.input_password_login('password')
        login.click_login()
        result = re.search(r'admin', login.get_source)
        log.info(result)
        assert result

    @allure.story("退出登录")
    def test_005(self, drivers):
        """退出登录"""
        login = LoginPage(drivers)
        login.action_admin()
        login.click_logout()
        result = re.search(r'请输入用户名', login.get_source)
        log.info(result)
        assert result


if __name__ == '__main__':
    pytest.main(['TestCase/test_courier_login.py', '-sv'])

# if __name__ == '__main__':
# 下面的代码使用pycharm运行可能会没有生成报告，建议使用vscode执行
#     import os
#     pytest.main(['TestCase/test_search.py', '--alluredir', './allure'])
#     os.system('allure serve allure')
