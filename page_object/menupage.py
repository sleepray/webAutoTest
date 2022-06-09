#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element
from utils.logger import log

menu = Element('courier_menu')

class MenuPage(WebPage):
    """菜单类"""

    def click_Menu(self, content):
        """点击菜单"""
        self.is_click(menu[content])

    def input_clear(self, content):
        """清空输入栏"""
        self.clear_text(menu[content])
        sleep()

    def click_Define(self):
        """确定按钮"""
        self.is_click(menu['确定按钮'])

    def click_search(self):
        """查询按钮"""
        self.is_click(menu['查询按钮'])

    def click_reset(self):
        """重置按钮"""
        self.is_click(menu['重置按钮'])

    def click_Canle(self):
        """取消按钮"""
        self.is_click(menu['取消按钮'])

    def click_close(self):
        """关闭按钮"""
        self.is_click(menu['关闭'])

    def click_refresh(self):
        """刷新按钮"""
        self.is_click(menu['刷新'])

    def click_add(self, num):
        """新增按钮"""
        self.is_clicks(num, menu['新增'])

    def click_edit(self, num):
        """编辑按钮"""
        self.is_clicks(num ,menu['编辑'])

    def click_gatedel(self, num):
        """网关模块删除按钮"""
        self.is_clicks(num, menu['网关删除'])

    def click_del(self, num):
        """删除按钮"""
        self.is_clicks(num, menu['删除'])

    def click_ButtoNo(self, num):
        """删除、注销按钮否"""
        self.is_clicks(num, menu['删除、注销按钮取消'])

    def click_ButtonYes(self, num):
        """删除、注销按钮是"""
        self.is_clicks(num ,menu['删除、注销按钮确定'])

    def click_switch(self, num):
        """点击开关按钮"""
        self.is_clicks(num ,menu['开关按钮'])

    def waite_element(self, content):
        """等待发现页面中的元素"""
        self.find_element(menu[content])
        log.info("等待 {} 元素节点加载出来".format(menu[content]))



class Service(MenuPage):
    """服务管理"""

    def input_servername(self, content):
        """输入服务名"""
        self.input_text(menu['服务名'], txt=content)
        sleep()

    def input_devname(self, content):
        """输入设备名"""
        self.input_text(menu['设备名'], txt=content)
        sleep()

    def input_colonyname(self, content):
        """输入集群名"""
        self.input_text(menu['集群名'], txt=content)
        sleep()

    def input_longtitude(self, content):
        """输入经度"""
        self.input_text(menu['经度'], txt=content)
        sleep()

    def input_latitude(self, content):
        """输入纬度"""
        self.input_text(menu['纬度'], txt=content)
        sleep()

    def input_basic(self, content):
        """输入服务描述"""
        self.input_text(menu['服务描述'], txt=content)
        sleep()

    def click_logoff(self):
        """注销异常按钮"""
        self.is_click(menu['注销异常按钮'])

    def click_refresh(self):
        """重置按钮"""
        self.is_click(menu['刷新按钮'])

    def click_change(self, num):
        """修改按钮"""
        self.is_clicks(num, menu['修改按钮'])

    def click_logoffs(self, num):
        """注销按钮"""
        self.is_clicks(num,menu['注销按钮'])

class Link(MenuPage):
    """链路追踪"""

    def input_rootservername(self, content):
        """输入服务名"""
        self.input_text(menu['根服务名'], txt=content)
        sleep()

    def click_datesubmit(self):
        """日期确定按钮"""
        self.is_click(menu['日期确定'])

    def input_enddate(self, content):
        """输入结束日期"""
        self.input_text(menu['结束日期'], txt=content)

    def click_lookup(self, num):
        """查看按钮"""
        self.is_clicks(num, menu['查看按钮'])

    def click_Linkinfo(self, num):
        """链路详情画布"""
        self.is_clicks(num, menu['链路详情画布'])

class ServiceConfig(MenuPage):
    """服务配置"""

    def input_key1(self, content):
        """输入key1"""
        self.input_text(menu['key输入框'], txt=content)
        sleep()

    def input_key2(self, content):
        """输入key1"""
        self.input_text(menu['key输入框2'], txt=content)
        sleep()

    def input_value1(self, content):
        """输入value1"""
        self.input_text(menu['value输入框'], txt=content)
        sleep()

    def input_value2(self, content):
        """输入value1"""
        self.input_text(menu['value输入框2'], txt=content)
        sleep()

    def input_servicename(self, content):
        """输入服务名"""
        self.input_text(menu['新建配置服务名'], txt=content)
        sleep()

    def input_key(self, content):
        """输入key"""
        self.input_text(menu['key'], txt=content)
        sleep()

    def input_configType(self, content):
        """输入服务配置名称"""
        self.input_text(menu['服务名称'], txt=content)
        sleep()

    def click_contentdel(self, num):
        """删除配置内容"""
        self.is_clicks(num, menu['配置内容删除'])

class ConfigManage(MenuPage):
    """配置管理"""

    def input_box(self, content):
        """输入阈值"""
        self.input_text(menu['输入框'], txt=content)
        sleep()

    def input_retain(self, content):
        """输入保留值"""
        self.input_text(menu['保留值'], txt=content)
        sleep()

    def input_upper(self, content):
        """输入上限值"""
        self.input_text(menu['上限值'], txt=content)
        sleep()

    def input_weight(self, content):
        """输入权重"""
        self.input_text(menu['权重'], txt=content)
        sleep()

    def click_list(self, num):
        """编辑列表值"""
        self.is_clicks(num, menu['列表编辑'])

    def click_DegradServList(self, num):
        """点击展开降级服务下拉框"""
        self.is_clicks(num, menu['降级服务展开按钮'])

    def click_DegradServ(self, num):
        """点击降级服务"""
        self.is_clicks(num, menu['降级服务'])

    def click_DegradServEnd(self):
        """点击最后一个降级服务"""
        self.is_clicksEnd(menu['降级服务'])

    def click_Tick(self):
        """点击编辑确定"""
        self.is_click(menu['编辑确定'])

    def click_fork(self):
        """点击编辑关闭"""
        self.is_click(menu['编辑关闭'])

    def click_DefaultEdit(self):
        """点击默认编辑"""
        self.is_click(menu['默认编辑'])

class Blacklist(MenuPage):
    """黑白名单"""

    def input_ip(self, content):
        """输入IP"""
        self.input_text(menu['ip'], txt=content)
        sleep()

class Location(MenuPage):
    """地理位置"""

    def input_locationame(self, content):
        """输入区域名"""
        self.input_text(menu['区域名'], txt=content)
        sleep()

    def input_longtitude(self, content):
        """输入经度"""
        self.input_text(menu['地理位置经度'], txt=content)
        sleep()

    def input_latitude(self, content):
        """输入纬度"""
        self.input_text(menu['地理位置纬度'], txt=content)
        sleep()

    def input_radius(self, content):
        """输入区域半径"""
        self.input_text(menu['区域半径'], txt=content)
        sleep()

class Conditional(MenuPage):
    """条件表达式"""

    def input_servicename(self, num, content):
        """输入服务名"""
        self.inputs_text(num, menu['服务名输入'], txt=content)
        sleep()

    def input_tagname1(self, content):
        """输入第一行tagname"""
        self.input_text(menu['tagname1'], txt=content)
        sleep()

    def input_tagname2(self, content):
        """输入第二行tagname"""
        self.input_text(menu['tagname2'], txt=content)
        sleep()

    def input_address1(self, content):
        """输入第一行第一个的address"""
        self.input_text(menu['address1'], txt=content)
        sleep()

    def input_address2(self, content):
        """输入第一行第二个的address"""
        self.input_text(menu['address2'], txt=content)
        sleep()

    def input_address3(self, content):
        """输入第一行第三个的address"""
        self.input_text(menu['address3'], txt=content)
        sleep()

    def input_2address1(self, content):
        """输入第二行第一个的address"""
        self.input_text(menu['2address1'], txt=content)
        sleep()

    def input_2address2(self, content):
        """输入第二行第二个的address"""
        self.input_text(menu['2address2'], txt=content)
        sleep()

    def click_address(self, num):
        """点击添加address按钮"""
        self.is_clicks(num ,menu['添加address'])

    def click_details(self, num):
        """点击详情按钮"""
        self.is_clicks(num ,menu['详情'])

    def click_opens(self, num):
        """点击开启按钮"""
        self.is_clicks(num ,menu['开启'])

    def click_shut(self, num):
        """点击关闭按钮"""
        self.is_clicks(num ,menu['列表关闭'])

class Statistics(MenuPage):
    """黑白名单"""

    def input_ip(self, content):
        """输入IP"""
        self.input_text(menu['ip'], txt=content)
        sleep()

    def input_port(self, content):
        """输入端口"""
        self.input_text(menu['端口'], txt=content)
        sleep()

    def input_serviceName(self, content):
        """输入服务名"""
        self.input_text(menu['新建配置服务名'], txt=content)
        sleep()

if __name__ == '__main__':
    pass
