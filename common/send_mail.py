#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'

import zmail
import conf


def send_report():
    """发送报告"""
    with open(conf.REPORT_PATH) as f:
        content_html = f.read()
    try:
        mail = {
            'from': '1084502012@qq.com',
            'subject': '最新的测试报告邮件',
            'content_html': content_html,
            'attachments': [conf.REPORT_PATH, ]
        }
        server = zmail.server(*conf.EMAIL_INFO.values())
        server.send_mail(conf.ADDRESSEE, mail)
    except Exception as e:
        print("Error: 无法发送邮件，{}！", format(e))
    else:
        print("测试邮件发送成功！")


if __name__ == "__main__":
    send_report()
