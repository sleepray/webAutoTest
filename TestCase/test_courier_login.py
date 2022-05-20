#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import pytest
import allure
from utils.times import sleep
from utils.logger import log

from common.readconfig import ini
from page_object.loginpage import LoginPage,MenuPage


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

# @pytest.mark.skip(reason="暂时跳过测试")
@allure.feature("courier菜单栏点击")
class TestMenu:
    @pytest.fixture(scope='function', autouse=True)
    def open_devops(self, drivers):
        """打开courier"""
        menu = MenuPage(drivers)
        menu.get_url(ini.url)

    @allure.story("点击BackHome按钮")
    def test_001(self, drivers):
        """点击BackHome"""
        menu = MenuPage(drivers)
        menu.click_Menu('backhome')
        result = re.search(r'服务管理', menu.get_source)
        log.info(result)
        assert result

    @allure.story("点击链路追踪")
    def test_002(self, drivers):
        """点击链路追踪"""
        menu = MenuPage(drivers)
        menu.click_Menu('链路追踪')
        result = re.search(r'链路追踪记录列表', menu.get_source)
        log.info(result)
        assert result

    @allure.story("点击服务管理")
    def test_003(self, drivers):
        """点击服务管理"""
        menu = MenuPage(drivers)
        menu.click_Menu('服务管理')
        result = re.search(r'服务列表', menu.get_source)
        log.info(result)
        assert result

    @allure.story("点击服务配置")
    def test_004(self, drivers):
        """点击服务配置"""
        menu = MenuPage(drivers)
        menu.click_Menu('服务配置')
        result = re.search(r'新建配置', menu.get_source)
        log.info(result)
        assert result

    @pytest.mark.usefixtures("open_devops")
    @allure.story("服务网关点击配置管理")
    def test_005(self, drivers):
        """点击配置管理"""
        menu = MenuPage(drivers)
        menu.click_Menu('服务网关')
        result = re.search(r'黑白名单', menu.get_source)
        log.info(result)
        menu.click_Menu('配置管理')
        result = re.search(r'一致性哈希', menu.get_source)
        log.info(result)
        assert result

    @allure.story("服务网关点击黑白名单")
    def test_006(self, drivers):
        """点击配置管理"""
        menu = MenuPage(drivers)
        menu.click_Menu('服务网关')
        result = re.search(r'黑白名单', menu.get_source)
        log.info(result)
        menu.click_Menu('黑白名单')
        result = re.search(r'黑名单管理', menu.get_source)
        log.info(result)
        assert result

    @allure.story("服务网关点击地理位置")
    def test_007(self, drivers):
        """点击配置管理"""
        menu = MenuPage(drivers)
        menu.click_Menu('服务网关')
        result = re.search(r'黑白名单', menu.get_source)
        log.info(result)
        menu.click_Menu('地理位置')
        result = re.search(r'地理位置启用开关', menu.get_source)
        log.info(result)
        assert result

    @allure.story("服务网关点击条件表达式")
    def test_008(self, drivers):
        """点击条件表达式"""
        menu = MenuPage(drivers)
        menu.click_Menu('服务网关')
        result = re.search(r'黑白名单', menu.get_source)
        log.info(result)
        menu.click_Menu('条件表达式')
        result = re.search(r'服务名', menu.get_source)
        log.info(result)
        assert result

    @allure.story("点击指标统计")
    def test_009(self, drivers):
        """点击指标统计"""
        menu = MenuPage(drivers)
        menu.click_Menu('指标统计')
        result = re.search(r'成功次数', menu.get_source)
        log.info(result)
        assert result


if __name__ == '__main__':
    pytest.main(['TestCase/test_courier_login.py', '-sv'])

# if __name__ == '__main__':
# 下面的代码使用pycharm运行可能会没有生成报告，建议使用vscode执行
#     import os
#     pytest.main(['TestCase/test_search.py', '--alluredir', './allure'])
#     os.system('allure serve allure')
