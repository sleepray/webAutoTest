#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
from selenium.webdriver.common.by import By
from utils.times import dt_strftime


class ConfigManager(object):
    # 项目目录
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 页面元素目录
    ELEMENT_PATH = os.path.join(BASE_DIR, 'page_element')

    # 报告文件
    REPORT_FILE = os.path.join(BASE_DIR, 'report.html')

    # log目录
    LOG_FILE = os.path.join(BASE_DIR, 'logs')

    # 截图目录
    SCREEN_FILE = os.path.join(BASE_DIR, 'screen_capture')

    # 元素定位的类型
    LOCATE_MODE = {
        'css': By.CSS_SELECTOR,
        'xpath': By.XPATH,
        'name': By.NAME,
        'id': By.ID,
        'class': By.CLASS_NAME
    }

    # 邮件信息
    EMAIL_INFO = {
        'username': '302559651@qq.com',  # 切换成你自己的地址
        'password': 'gnwzuldkeobpbjdh',
        'smtp_host': 'smtp.qq.com',
        'smtp_port': 465
    }

    # 收件人
    ADDRESSEE = [
        '302559651@qq.com',
    ]

    @property
    def screen_path(self):
        """截图目录"""
        if not os.path.exists(self.SCREEN_FILE):
            os.makedirs(self.SCREEN_FILE)
        now_time = dt_strftime("%Y%m%d%H%M%S")
        screen_file = os.path.join(self.SCREEN_FILE, "{}.png".format(now_time))
        return now_time, screen_file

    @property
    def log_file(self):
        """日志目录"""
        if not os.path.exists(self.LOG_FILE):
            os.makedirs(self.LOG_FILE)
        return os.path.join(self.LOG_FILE, '{}.log'.format(dt_strftime()))

    @property
    def ini_file(self):
        """配置文件"""
        ini_file = os.path.join(self.BASE_DIR, 'config', 'config.ini')
        if not os.path.exists(ini_file):
            raise FileNotFoundError("配置文件%s不存在！" % ini_file)
        return ini_file



cm = ConfigManager()
if __name__ == '__main__':
    print(cm.screen_path)
    print(cm.log_file)
