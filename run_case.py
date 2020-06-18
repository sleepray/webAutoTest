#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'

import os
import shutil
import subprocess
from config.conf import ALLURE_DIR
from tools.times import datetime_strftime

ALLURE_TEST = './report/allure'



def copy_history():
    """复制allure历史数据"""
    allure_file = [os.path.join(ALLURE_DIR, i) for i in os.listdir(ALLURE_DIR)]
    new_path = sorted(allure_file, key=lambda x: os.stat(x).st_ctime)
    start_path = os.path.join(new_path[-1], 'history')
    end_path = os.path.join(ALLURE_TEST, 'history')
    if os.path.exists(end_path):
        shutil.rmtree(end_path)
    try:
        shutil.copytree(start_path, end_path)
    except FileNotFoundError:
        print("上一次的allure历史数据不存在！")


def export_dir():
    """导出目录"""
    export = os.path.join(ALLURE_DIR, datetime_strftime("%Y%m%d%H%M%S"))
    if not os.path.exists(export):
        os.makedirs(export)
    return export


def main():
    """主函数"""
    copy_history()
    export_dirname = export_dir()
    subprocess.call(['pytest', '--alluredir', ALLURE_TEST], shell=True)
    subprocess.call(['allure', 'generate', ALLURE_TEST,
                     '-o', export_dirname], shell=True)
    subprocess.call(['allure', 'open', export_dirname], shell=True)


if __name__ == '__main__':
    main()
