#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from common.times import sleep
from common.log import log
import conf

"""
selenium基类
本文件存放了selenium基类的封装方法
"""


class WebPage(object):
    """selenium基类"""

    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(self.driver, self.timeout)

    def get_url(self, url):
        """打开网址并验证"""
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(60)
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            log.info("打开网页：%s" % url)
        except TimeoutException:
            raise TimeoutException("打开%s超时请检查网络或网址服务器" % url)

    @staticmethod
    def element_locator(func, locator):
        """元素定位器"""
        name, value = locator
        return func(conf.LOCATE_MODE[name], value)

    def findelement(self, locator):
        """寻找单个元素"""
        return WebPage.element_locator(lambda *args: self.wait.until(lambda x: x.find_element(*args)), locator)

    def findelements(self, locator):
        """查找多个相同的元素"""
        return WebPage.element_locator(lambda *args: self.wait.until(lambda x: x.find_elements(*args)), locator)

    def isElementNum(self, locator):  # 获取相同元素的个数
        """获取相同元素的个数"""
        number = len(self.findelements(locator))
        log.info("相同元素：{}".format((locator, number)))
        return number

    def is_clear(self, locator):
        """清空输入框"""
        self.findelement(locator).clear()
        self.driver.implicitly_wait(0.5)
        log.info("清空输入框！")

    def input_text(self, locator, txt):
        """输入(输入前先清空)"""
        sleep(0.5)
        self.is_clear(locator)
        self.findelement(locator).send_keys(txt)
        log.info("输入文本：{}".format(txt))

    def is_click(self, locator):
        """点击"""
        self.findelement(locator).click()
        sleep()
        log.info("点击元素：{}".format(locator))

    def isElementText(self, locator):
        """获取当前的text"""
        __text = self.findelement(locator).text
        log.info("获取文本：{}".format(__text))
        return __text

    @property
    def getSource(self):
        """获取页面源代码"""
        return self.driver.page_source

    def shot_file(self, path):
        """文件截图"""
        return self.driver.save_screenshot(path)

    def close(self):
        """关闭当前标签"""
        self.driver.close()

    def refresh(self):
        """刷新页面F5"""
        self.driver.refresh()
        self.driver.implicitly_wait(30)


if __name__ == "__main__":
    pass
