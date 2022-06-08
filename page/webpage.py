#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
selenium基类
本文件存放了selenium基类的封装方法
"""
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

from config.conf import cm
from utils.times import sleep
from utils.logger import log

from selenium.webdriver.common.by import By
from selenium import webdriver

class WebPage(object):
    """selenium基类"""

    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver
        self.timeout = 20
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
        return func(cm.LOCATE_MODE[name], value)

    def find_element(self, locator):
        """寻找单个元素"""
        return WebPage.element_locator(lambda *args: self.wait.until(
            EC.presence_of_element_located(args)), locator)

    def find_elements(self, locator):
        """查找多个相同的元素"""
        return WebPage.element_locator(lambda *args: self.wait.until(
            EC.presence_of_all_elements_located(args)), locator)

    def wait_element(self, locator):
        self.wait.until(
            EC.presence_of_element_located(locator))

    def elements_num(self, locator):
        """获取相同元素的个数"""
        number = len(self.find_elements(locator))
        log.info("相同元素：{}".format((locator, number)))
        return number

    def input_text(self, locator, txt):
        """输入(输入前先清空)"""
        sleep(0.5)
        ele = self.find_element(locator)
        # ele.clear()  clear() 函数有时不生效,这里先用键盘删除来替代
        ele.send_keys(Keys.CONTROL,"a")
        ele.send_keys(Keys.BACKSPACE)
        ele.send_keys(txt)
        log.info("输入文本：{}".format(txt))

    def inputs_text(self, num, locator, txt):
        """输入(输入前先清空)"""
        sleep(0.5)
        ele = self.find_elements(locator)[num]
        # ele.clear()  clear() 函数有时不生效,这里先用键盘删除来替代
        ele.send_keys(Keys.CONTROL,"a")
        ele.send_keys(Keys.BACKSPACE)
        ele.send_keys(txt)
        log.info("输入文本：{}".format(txt))

    def clear_text(self, locator):
        """clear()函数不起作用时，采用Backspace键删除"""
        sleep(0.5)
        ele = self.find_element(locator)
        ele.send_keys(Keys.CONTROL,"a")
        ele.send_keys(Keys.BACKSPACE)
        log.info("清空元素输入框：{}".format(locator))

    def is_click(self, locator):
        """点击"""
        self.find_element(locator).click()
        sleep()
        log.info("点击元素：{}".format(locator))

    def is_clicks(self, num, locator):
        """点击相同元素"""
        self.find_elements(locator)[num].click()
        sleep()
        log.info("点击元素：{} 中的第 {}个".format(locator, num + 1))

    def is_clicksEnd(self, locator):
        """点击相同元素中最后一个元素"""
        num = len(self.find_elements(locator)) - 1 #获取列表元素，在列表中使用时是从0开始数，所以这里减1
        self.find_elements(locator)[num].click()
        sleep()
        log.info("点击元素：{} 中的最后一个".format(locator))

    def element_text(self, locator):
        """获取当前的text"""
        _text = self.find_element(locator).text
        log.info("获取文本：{}".format(_text))
        return _text

    @property
    def get_source(self):
        """获取页面源代码"""
        self.driver.implicitly_wait(30) # 等待页面全部加载完成后，获取源码
        sleep()  # courier 项目中，隐式等待无效，故停顿1s
        return self.driver.page_source

    def refresh(self):
        """刷新页面F5"""
        self.driver.refresh()
        self.driver.implicitly_wait(30)

    def close(self):
        """关闭浏览器"""
        self.driver.close()

    def is_action(self, locator):
        """浮动在元素上方"""
        ele = self.find_element(locator)
        ActionChains(self.driver).move_to_element(ele).perform()


if __name__ == "__main__":
    pass
