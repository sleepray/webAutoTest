#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import pytest
import allure
from utils.times import sleep
from utils.logger import log

from common.readconfig import ini
from page_object.loginpage import LoginPage

@pytest.mark.skip(reason="跳过devops登录测试")
@allure.feature("测试devops登录")
class TestLogin:
    @pytest.fixture(scope='function', autouse=True)
    def open_devops(self, drivers):
        """打开devops"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("输入正确用户名密码")
    def test_001(self, drivers):
        """登录"""
        login = LoginPage(drivers)
        login.click_LDAP()
        login.input_username_login('chenlei')
        login.input_password_login('password')
        login.click_login()
        result = re.search(r'成都精灵云科技', login.get_source)
        log.info(result)
        assert result

    @allure.story("输入错误用户名密码")
    def test_002(self, drivers):
        """登录"""
        login = LoginPage(drivers)
        login.click_LDAP()
        login.input_username_login('chenlei')
        login.input_password_login('123456')
        login.click_login()
        result = re.search(r'密码错误', login.get_source)
        log.info(result)
        assert result

    @allure.story("不输入用户名密码")
    def test_003(self, drivers):
        """登录"""
        login = LoginPage(drivers)
        login.click_LDAP()
        login.click_login()
        result = re.search(r'请输入账户', login.get_source)
        log.info(result)
        assert result

    @allure.story("不输入密码")
    def test_004(self, drivers):
        """登录"""
        login = LoginPage(drivers)
        login.click_LDAP()
        login.input_username_login('chenlei')
        login.click_login()
        result = re.search(r'请输入密码', login.get_source)
        log.info(result)
        assert result

    @allure.story("不使用LDAP登录")
    def test_005(self, drivers):
        """登录"""
        login = LoginPage(drivers)
        login.input_username_login('chenlei')
        login.input_password_login('123456')
        login.click_login()
        result = re.search(r'密码错误', login.get_source)
        log.info(result)
        assert result

@pytest.mark.skip(reason="跳过devops登录测试")
@allure.feature("测试devops搜索")
class TestLoginSearch:
    @pytest.fixture(scope='function', autouse=True)
    def open_devops(self, drivers):
        """打开devops"""
        login = LoginPage(drivers)
        login.get_url(ini.url)
        login.click_LDAP()
        login.input_username_login('chenlei')
        login.input_password_login('password')
        login.click_login()
        sleep()

    @allure.story("搜索中间件")
    def test_001(self, drivers):
        """搜索"""
        login = LoginPage(drivers)
        login.search_login('中间件业务线')
        login.click_search()
        result = re.search(r'中间件业务线', login.get_source)
        log.info(result)
        assert result

    @allure.story("搜索Pengze")
    def test_002(self, drivers):
        """搜索"""
        login = LoginPage(drivers)
        login.search_login('Pengze')
        login.click_search()
        result = re.search(r'Pengze', login.get_source)
        log.info(result)
        assert result

if __name__ == '__main__':
    pytest.main(['TestCase/test_login.py', '-sv'])

# if __name__ == '__main__':
# 下面的代码使用pycharm运行可能会没有生成报告，建议使用vscode执行
#     import os
#     pytest.main(['TestCase/test_search.py', '--alluredir', './allure'])
#     os.system('allure serve allure')
