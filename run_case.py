#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'

import pytest
from common.send_mail import send_report
from common.inspect import inspect_element

if __name__ == "__main__":
    inspect_element()
    pytest.main()
    send_report()
