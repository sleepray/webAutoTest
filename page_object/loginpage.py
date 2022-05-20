#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element

# login = Element('devops_login')
login = Element('courier_login')

class LoginPage(WebPage):
    """登录类"""

    def input_username_login(self, content):
        """输入用户名"""
        self.input_text(login['用户名'], txt=content)
        sleep()

    def input_password_login(self, content):
        """输入用户名"""
        self.input_text(login['密码'], txt=content)
        sleep()

    def search_login(self, content):
        """搜索名称"""
        self.input_text(login['搜索'], txt=content)
        sleep()

    def click_LDAP(self):
        """LDAP登录"""
        self.is_click(login['LDAP'])

    def click_login(self):
        """点击登录"""
        self.is_click(login['登录按钮'])

    def click_search(self):
        """搜索按钮"""
        self.is_click(login['搜索按钮'])

    def input_servername(self, content):
        """输入服务名"""
        self.input_text(login['服务名'], txt=content)
        sleep()

    def input_clear(self, content):
        """输入服务名"""
        self.clear_text(login[content])
        sleep()

class MenuPage(WebPage):
    """菜单类"""

    def click_Menu(self, content):
        """点击登录"""
        self.is_click(login[content])


if __name__ == '__main__':
    pass