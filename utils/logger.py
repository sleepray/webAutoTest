#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import logging

from common.redlogyaml import redyaml
from config.conf import cm
from common import redlogyaml

# class Log:
#     def __init__(self):
#         if logging.getLogger():
#             self.logger = logging.getLogger()
#         if not self.logger.handlers:
#             self.logger.setLevel(logging.DEBUG)
#
#             # 创建一个handle写入文件
#             fh = logging.FileHandler(cm.log_file, encoding='utf-8')
#             fh.setLevel(logging.INFO)
#
#             # 创建一个handle输出到控制台
#             ch = logging.StreamHandler()
#             ch.setLevel(logging.INFO)
#
#             # 定义输出的格式
#             formatter = logging.Formatter(self.fmt)
#             fh.setFormatter(formatter)
#             ch.setFormatter(formatter)
#
#             # 添加到handle
#             self.logger.addHandler(fh)
#             self.logger.addHandler(ch)
#
#     @property
#     def fmt(self):
#         return '%(levelname)s\t%(asctime)s\t[%(filename)s:%(lineno)d]\t%(message)s'
#
#
#
# print("----log执行----")
#
# if __name__ == '__main__':
#     log = Log().logger
#     log.info('hello world')
#     log.info("写入测试")


class Logger(logging.Logger):

    def __init__(self,
                 name='root',
                 level='INFO',
                 file=None,
                 format=None):
        # 设置收集器
        super().__init__(name)
        # 设置收集器级别
        # self.setLevel(level)
        # 设置日志格式
        fmt = logging.Formatter(format)
        # 如果file存在就将日志输出到文件中
        if file:
            # 默认写入方式为'a'
            file_handler = logging.FileHandler(file, encoding='utf-8', mode='w')
            file_handler.setLevel(level)
            file_handler.setFormatter(fmt)
            self.addHandler(file_handler)
        # 设置streamHandler,输出日志到控制台
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(level)
        stream_handler.setFormatter(fmt)
        self.addHandler(stream_handler)

log = Logger(file=cm.log_file,format=redyaml.red()['logger']['format'])

if __name__ == '__main__':
    log.info('252345')



