#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element

menu = Element('courier_menu')
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

    def action_admin(self):
        """浮动登出"""
        self.is_action(login['admin'])

    def click_logout(self):
        """点击登录"""
        self.is_click(login['退出登录'])

    def input_clear(self, content):
        """清空输入栏"""
        self.clear_text(login[content])
        sleep()

    def click_Menu(self, content):
        """点击菜单"""
        self.is_click(menu[content])

if __name__ == '__main__':
    pass