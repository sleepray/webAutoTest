#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
sys.path.append('.')

import os
import shutil
from config.conf import ALLURE_RESULTS


def clear_allure_results():
    var = True
    for i in os.listdir(ALLURE_RESULTS):
        new_path = os.path.join(ALLURE_RESULTS, i)
        if os.path.isfile(new_path):
            os.remove(new_path)
            print("删除{}成功！".format(new_path))
            var = False
    if var:
        print("没有数据可清理！")


if __name__ == "__main__":
    clear_allure_results()
