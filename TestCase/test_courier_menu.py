#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import pytest
import allure
from datetime import datetime
from utils.times import sleep
from utils.logger import log

from common.readconfig import ini
from page_object.loginpage import LoginPage
from page_object.menupage import MenuPage, Service, Link, ServiceConfig, ConfigManage, Blacklist, Location, Conditional, Statistics

# 系统run时改为False
auto = False

# @pytest.mark.skip(reason="暂时跳过测试")
@allure.feature("courier菜单栏点击")
class TestService:

    @pytest.fixture(scope='session', autouse=True)
    def open_devops(self, drivers):
        """打开courier"""
        login = LoginPage(drivers)
        login.get_url(ini.url)
        login.input_username_login('admin')
        login.input_password_login('password')
        login.click_login()
        login.click_Menu("服务管理")

    @allure.story("点击服务管理")
    def test_001(self, drivers):
        """点击服务管理"""
        serv = Service(drivers)
        serv.click_Menu('服务管理')
        serv.waite_element('服务名')
        result = re.search(r'服务列表', serv.get_source)
        log.info(result)
        assert result

    @allure.story("服务管理搜索功能")
    def test_002(self, drivers):
        """服务管理搜索功能"""
        serv = Service(drivers)
        serv.input_servername("服务名搜索测试")
        serv.click_search()
        serv.click_reset()
        serv.input_devname("设备名称搜索测试")
        serv.click_search()
        serv.click_reset()
        serv.input_colonyname("集群名称搜索测试")
        serv.click_search()
        serv.click_reset()
        serv.input_servername("服务名搜索测试")
        serv.input_devname("设备名称搜索测试")
        serv.input_colonyname("集群名称搜索测试")
        serv.click_search()
        serv.click_reset()

    @allure.story("注销异常按钮")
    def test_003(self, drivers):
        """注销异常按钮"""
        serv = Service(drivers)
        serv.click_logoff()
        result = re.search(r'注销异常服务成功', serv.get_source)
        log.info(result)
        assert result

    @allure.story("刷新按钮")
    def test_004(self, drivers):
        """点击刷新按钮"""
        serv = Service(drivers)
        serv.click_refresh()


    @allure.story("修改按钮")
    def test_005(self, drivers):
        """点击修改按钮"""
        serv = Service(drivers)
        serv.click_change(0)
        result = re.search(r'修改服务', serv.get_source)
        log.info(result)
        assert result
        serv.click_Canle()

    @allure.story("输入经度")
    def test_006(self, drivers):
        """经度测试"""
        longtitude = "13.24"
        serv = Service(drivers)
        serv.click_change(0)
        serv.input_longtitude(longtitude)
        serv.click_Canle()
        serv.click_change(0)
        serv.input_longtitude(longtitude)
        serv.click_Define()
        result = re.search(r'修改服务成功', serv.get_source)
        log.info(result)
        assert result
        serv.click_change(0)
        result = re.search(longtitude, serv.get_source)
        log.info(result)
        assert result
        serv.click_Canle()

    @allure.story("输入纬度")
    def test_007(self, drivers):
        """纬度测试"""
        latitude = "165.24"
        serv = Service(drivers)
        serv.click_change(0)
        serv.input_latitude(latitude)
        serv.click_Canle()
        serv.click_change(0)
        serv.input_latitude(latitude)
        serv.click_Define()
        result = re.search(r'修改服务成功', serv.get_source)
        log.info(result)
        assert result
        serv.click_change(0)
        result = re.search(latitude, serv.get_source)
        log.info(result)
        assert result
        serv.click_Canle()

    @allure.story("服务描述")
    def test_008(self, drivers):
        """服务描述测试"""
        basic = "测试服务描述，随便写的一点文本内容"
        serv = Service(drivers)
        serv.click_change(0)
        serv.input_basic(basic)
        serv.click_Canle()
        serv.click_change(0)
        serv.input_basic(basic)
        serv.click_Define()
        result = re.search(r'修改服务成功', serv.get_source)
        log.info(result)
        assert result
        serv.click_change(0)
        result = re.search(basic, serv.get_source)
        log.info(result)
        assert result
        serv.click_Canle()

    @allure.story("修改服务模块参数一同修改")
    def test_09(self, drivers):
        """修改服务参数模块一同修改测试"""
        longtitude, latitude, basic = "12.31","123.98","测试服务描述，随便写的一点文本内容"
        serv = Service(drivers)

        # click_change(0) 代表修改元素列表中第一个元素
        serv.click_change(0)
        serv.input_longtitude(longtitude)
        serv.input_latitude(latitude)
        serv.input_basic(basic)
        serv.click_Canle()
        serv.click_change(0)
        serv.input_longtitude(longtitude)
        serv.input_latitude(latitude)
        serv.input_basic(basic)
        serv.click_Define()
        result = re.search(r'修改服务成功', serv.get_source)
        log.info(result)
        assert result
        serv.click_change(0)
        result1 = re.search(basic, serv.get_source)
        result2 = re.search(longtitude, serv.get_source)
        result3 = re.search(latitude, serv.get_source)
        log.info(f"匹配信息：result1：{result1},\nresult2：{result2},\nresult3：{result3}")
        assert result1 and result2 and result3
        serv.click_Canle()

    @pytest.mark.skip("系统run的时候不需要注销，否则后续用例无法正常运行")
    @allure.story("注销按钮")
    def test_010(self, drivers):
        """注销按钮测试"""
        serv = Service(drivers)
        serv.click_logoffs(0)
        serv.click_ButtoNo(0)
        sleep()
        serv.click_logoffs(0)
        serv.click_ButtonYes(0)
        result = re.search(r'注销成功', serv.get_source)
        log.info(result)
        assert result

@allure.feature("courier链路追踪")
class TestLink:
    # @pytest.mark.skip("整体run的时候，不启动前置条件")
    @pytest.fixture(scope='session', autouse=auto)
    def open_devops(self, drivers):
        """打开courier"""
        login = LoginPage(drivers)
        login.get_url(ini.url)
        login.input_username_login('admin')
        login.input_password_login('password')
        login.click_login()
        login.click_Menu("链路追踪")

    @allure.story("点击链路追踪")
    def test_001(self, drivers):
        """点击服务管理"""
        link = Link(drivers)
        link.click_Menu('链路追踪')
        link.waite_element("根服务名")
        result = re.search(r'链路追踪记录列表', link.get_source)
        log.info(result)
        assert result

    @allure.story("根服务名搜索功能")
    def test_002(self, drivers):
        """链路追踪搜索功能"""
        link = Link(drivers)
        link.input_rootservername("conditionservice")
        link.click_search()
        result = re.search(r'<span>conditionservice', link.get_source)
        log.info(result)
        assert result
        link.click_reset()
        link.input_rootservername("根服务名搜索功能")
        link.click_search()
        result = re.search(r'暂无数据', link.get_source)
        log.info(result)
        assert result
        link.click_reset()

    @allure.story("日期范围搜索功能")
    def test_003(self, drivers):
        """服务管理搜索功能"""

        # 开始日期
        link = Link(drivers)
        link.click_Menu("开始日期")
        result = re.search(r'2022年', link.get_source)
        log.info(result)
        assert result
        link.click_Menu('年份按钮')
        link.click_Menu('2020年')
        link.click_Menu('月份按钮')
        link.click_Menu('1月')
        link.click_Menu('1日')
        link.click_datesubmit()
        result = re.search(r'2020-01-01', link.get_source)
        log.info(result)
        assert result

        # 结束日期
        link.input_enddate(datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S"))
        link.click_datesubmit()
        result = re.search(datetime.strftime(datetime.now(), "%Y-%m-%d"), link.get_source)
        log.info(result)
        assert result
        link.click_search()
        link.click_search()
        result = re.search(r'开始日期', link.get_source)
        log.info(result)
        assert result

    @allure.story("链路追踪列表刷新")
    def test_004(self, drivers):
        """链路追踪列表刷新"""
        link = Link(drivers)
        link.click_refresh()
        result = re.search(r'disabled', link.get_source)
        log.info(result)
        assert result

    @allure.story("查看列表第一个链路追踪详情")
    def test_005(self, drivers):
        """查看列表第一个链路追踪详情"""
        link = Link(drivers)
        link.click_lookup(0)
        link.click_Linkinfo(1)
        result = re.search(r'链路追踪详情', link.get_source)
        log.info(result)
        assert result
        link.click_Menu('返回链路追踪')
        result = re.search(r'链路追踪记录列表', link.get_source)
        log.info(result)

@allure.feature("courier服务配置")
class TestServiceConfig:
    @pytest.fixture(scope='session', autouse=auto)
    def open_devops(self, drivers):
        """打开courier"""
        login = LoginPage(drivers)
        login.get_url(ini.url)
        login.input_username_login('admin')
        login.input_password_login('password')
        login.click_login()
        login.click_Menu("服务配置")

    @allure.story("点击服务配置")
    def test_001(self, drivers):
        """点击服务管理"""
        sercof = ServiceConfig(drivers)
        sercof.click_Menu('服务配置')
        sercof.waite_element("key")
        result = re.search(r'配置类型', sercof.get_source)
        log.info(result)
        assert result

    @allure.story("新建配置单个Global")
    def test_002(self, drivers):
        """新建配置单个Global"""
        sercof = ServiceConfig(drivers)
        sercof.click_add(0)
        result = re.search(r'data.prop', sercof.get_source)
        log.info(result)
        assert result
        sercof.click_Menu('Global')
        sercof.input_key1("key1")
        sercof.input_value1('value1')
        sercof.click_Canle()
        result = re.search(r'配置类型', sercof.get_source)
        log.info(result)
        assert result

        # 新建配置保存
        sercof.click_add(0)
        result = re.search(r'data.prop', sercof.get_source)
        log.info(result)
        assert result
        sercof.click_Menu('Global')
        sercof.input_key1("key1")
        sercof.input_value1('value1')
        sercof.click_Define()
        result = re.search(r'key1', sercof.get_source)
        log.info(result)
        assert result
        sercof.click_del(0)
        result = re.search(r'删除成功', sercof.get_source)
        log.info(result)
        assert result

    @allure.story("新建配置多个Global")
    def test_003(self, drivers):
        """新建配置多个Global"""
        sercof = ServiceConfig(drivers)
        sercof.click_add(0)
        result = re.search(r'data.prop', sercof.get_source)
        log.info(result)
        assert result
        sercof.click_Menu('Global')
        sercof.input_key1("key1")
        sercof.input_value1('value1')
        sercof.click_Menu('添加一行数据')
        result = re.search(r'删除', sercof.get_source)
        log.info(result)
        assert result
        sercof.input_key2("key2")
        sercof.input_value2("value2")
        sercof.click_contentdel(1)
        # sleep()
        # sercof.click_ButtoNo(0)
        # sercof.click_contentdel(1)
        # sleep(2)
        sercof.click_ButtonYes(0)
        sercof.click_Menu('添加一行数据')
        result = re.search(r'删除', sercof.get_source)
        log.info(result)
        assert result
        sercof.input_key2("key2")
        sercof.input_value2("value2")
        sercof.click_Define()
        result = re.search(r'value2', sercof.get_source)
        log.info(result)
        assert result
        sercof.click_del(0)
        sercof.click_del(0)
        result = re.search(r'删除成功', sercof.get_source)
        log.info(result)
        assert result

    @allure.story("编辑配置Global")
    def test_004(self, drivers):
        """编辑配置Global"""
        # 新建配置
        sercof = ServiceConfig(drivers)
        sercof.click_add(0)
        result = re.search(r'data.prop', sercof.get_source)
        log.info(result)
        assert result
        sercof.click_Menu('Global')
        sercof.input_key1("key1")
        sercof.input_value1('value1')
        sercof.click_Define()
        result = re.search(r'key1', sercof.get_source)
        log.info(result)
        assert result

        # 编辑配置
        sercof.click_edit(0)
        sercof.input_value1('value2')
        sercof.click_Define()
        result = re.search(r'value2', sercof.get_source)
        log.info(result)
        assert result
        sercof.click_del(0)
        result = re.search(r'删除成功', sercof.get_source)
        log.info(result)
        assert result

    @allure.story("新建配置单个Service")
    def test_005(self, drivers):
        """新建配置单个Service"""
        sercof = ServiceConfig(drivers)
        sercof.click_add(0)
        result = re.search(r'data.prop', sercof.get_source)
        log.info(result)
        assert result
        sercof.click_Menu('service')
        result = re.search(r'服务名', sercof.get_source)
        log.info(result)
        assert result
        sercof.input_servicename('service')
        sercof.input_key1("key1")
        sercof.input_value1('value1')
        sercof.click_Canle()
        result = re.search(r'配置类型', sercof.get_source)
        log.info(result)
        assert result

        # 新建配置保存
        sercof.click_add(0)
        result = re.search(r'data.prop', sercof.get_source)
        log.info(result)
        assert result
        sercof.click_Menu('service')
        sercof.input_servicename('service1')
        sercof.input_key1("key1")
        sercof.input_value1('value1')
        sercof.click_Define()
        result = re.search(r'service1', sercof.get_source)
        log.info(result)
        assert result
        sercof.click_del(0)
        result = re.search(r'删除成功', sercof.get_source)
        log.info(result)
        assert result

    @allure.story("新建配置多个Service")
    def test_006(self, drivers):
        """新建配置多个Service"""
        sercof = ServiceConfig(drivers)
        sercof.click_add(0)
        result = re.search(r'data.prop', sercof.get_source)
        log.info(result)
        assert result
        sercof.click_Menu('service')
        result = re.search(r'服务名', sercof.get_source)
        log.info(result)
        assert result
        sercof.input_servicename('service1')
        sercof.input_key1("key1")
        sercof.input_value1('value1')
        sercof.click_Menu('添加一行数据')
        result = re.search(r'删除', sercof.get_source)
        log.info(result)
        assert result
        sercof.input_key2("key2")
        sercof.input_value2("value2")
        # sercof.click_contentdel(1)
        # sercof.click_ButtoNo(0)
        sercof.click_contentdel(1)
        sercof.click_ButtonYes(0)
        sercof.click_Menu('添加一行数据')
        result = re.search(r'删除', sercof.get_source)
        log.info(result)
        assert result
        sercof.input_key2("key2")
        sercof.input_value2("value2")
        sercof.click_Define()
        result = re.search(r'value2', sercof.get_source)
        log.info(result)
        assert result
        sercof.click_del(0)
        sercof.click_del(0)
        result = re.search(r'删除成功', sercof.get_source)
        log.info(result)
        assert result

    @allure.story("编辑配置Global")
    def test_007(self, drivers):
        """编辑配置Global"""
        # 新建配置
        sercof = ServiceConfig(drivers)
        sercof.click_add(0)
        result = re.search(r'data.prop', sercof.get_source)
        log.info(result)
        assert result
        sercof.click_Menu('service')
        result = re.search(r'服务名', sercof.get_source)
        log.info(result)
        assert result
        sercof.input_servicename('service1')
        sercof.input_key1("key1")
        sercof.input_value1('value1')
        sercof.click_Define()
        result = re.search(r'service1', sercof.get_source)
        log.info(result)
        assert result

        # 编辑配置
        sercof.click_edit(0)
        sercof.input_value1('value2')
        sercof.click_Define()
        result = re.search(r'value2', sercof.get_source)
        log.info(result)
        assert result
        sercof.click_del(0)
        result = re.search(r'删除成功', sercof.get_source)
        log.info(result)
        assert result

    @allure.story("服务配置刷新")
    def test_008(self, drivers):
        """服务配置刷新"""
        # 新建配置
        sercof = ServiceConfig(drivers)
        sercof.click_refresh()
        result = re.search(r'anticon anticon-reload ant-tooltip-open', sercof.get_source)
        log.info(result)
        assert result

    @allure.story("服务配置搜索")
    def test_009(self, drivers):
        """服务配置搜索"""
        # 新建Global配置
        sercof = ServiceConfig(drivers)
        sercof.click_add(0)
        result = re.search(r'data.prop', sercof.get_source)
        log.info(result)
        assert result
        sercof.click_Menu('Global')
        sercof.input_key1("key1")
        sercof.input_value1('value1')
        sercof.click_Define()
        result = re.search(r'key1', sercof.get_source)
        log.info(result)
        assert result

        # 新建service配置
        sercof = ServiceConfig(drivers)
        sercof.click_add(0)
        result = re.search(r'data.prop', sercof.get_source)
        log.info(result)
        assert result
        sercof.click_Menu('service')
        result = re.search(r'服务名', sercof.get_source)
        log.info(result)
        assert result
        sercof.input_servicename('service1')
        sercof.input_key1("key2")
        sercof.input_value1('value2')
        sercof.click_Define()
        result = re.search(r'service1', sercof.get_source)
        log.info(result)
        assert result

        # key搜索
        sercof.input_key("key1")
        sercof.click_search()
        result = re.search(r'key2', sercof.get_source)
        log.info(result)
        assert not result
        sercof.click_reset()

        sercof.input_key('key2')
        sercof.click_search()
        result = re.search(r'key1', sercof.get_source)
        log.info(result)
        assert not result
        sercof.click_reset()

        sercof.input_key('key3')
        sercof.click_search()
        result = re.search(r'key1', sercof.get_source)
        result2 = re.search(r'key2', sercof.get_source)
        log.info("{result} \n {result2}")
        assert not result and not result2
        sercof.click_reset()

        # 服务名称搜索
        sercof.input_configType('global')
        sercof.click_search()
        result = re.search(r'service1', sercof.get_source)
        log.info(result)
        assert not result
        sercof.click_reset()

        sercof.input_configType('service1')
        sercof.click_search()
        result = re.search(r'global</td>', sercof.get_source)
        log.info(result)
        assert not result
        sercof.click_reset()

        sercof.input_configType('key3')
        sercof.click_search()
        result = re.search(r'global</td>', sercof.get_source)
        result2 = re.search(r'service1', sercof.get_source)
        log.info("{result} \n {result2}")
        assert not result and not result2
        sercof.click_reset()

        sercof.click_del(0)
        sercof.click_del(0)
        result = re.search(r'删除成功', sercof.get_source)
        log.info(result)
        assert result

@allure.feature("配置管理")
class TestConfigManage:
    @pytest.fixture(scope='session', autouse=auto)
    def open_devops(self, drivers):
        """打开courier"""
        login = LoginPage(drivers)
        login.get_url(ini.url)
        login.input_username_login('admin')
        login.input_password_login('password')
        login.click_login()
        login.click_Menu("服务网关")
        login.click_Menu("配置管理")

    @allure.story("点击配置管理")
    def test_001(self, drivers):
        """点击服务管理"""
        confma = ConfigManage(drivers)

        # 系统run的时候开启这一条，否则无法跳转配置管理
        confma.click_Menu("服务网关")
        confma.click_Menu('配置管理')
        confma.waite_element('随机')
        result = re.search(r'负载均衡', confma.get_source)
        log.info(result)
        assert result

    @allure.story("负载均衡选择")
    def test_002(self, drivers):
        """负载均衡选择"""
        confma = ConfigManage(drivers)
        confma.click_Menu('负载均衡')
        result = re.search(r'随机', confma.get_source)
        log.info(result)
        assert result

        confma.click_Menu("轮询")
        confma.click_Canle()
        confma.click_Menu("轮询")
        confma.click_close()
        confma.click_Menu("轮询")
        confma.click_Define()

        confma.click_Menu("一致性哈希")
        confma.click_Canle()
        confma.click_Menu("一致性哈希")
        confma.click_close()
        confma.click_Menu("一致性哈希")
        confma.click_Define()

        confma.click_Menu("最小连接数")
        confma.click_Canle()
        confma.click_Menu("最小连接数")
        confma.click_close()
        confma.click_Menu("最小连接数")
        confma.click_Define()

        confma.click_Menu("随机")
        confma.click_Canle()
        confma.click_Menu("随机")
        confma.click_close()
        confma.click_Menu("随机")
        confma.click_Define()

    @allure.story("服务熔断")
    def test_003(self, drivers):
        """服务熔断测试"""
        confma = ConfigManage(drivers)
        confma.click_Menu('服务熔断')
        result = re.search(r'服务熔断默认阈值', confma.get_source)
        log.info(result)
        assert result

        # 服务熔断开关
        confma.click_switch(0)
        result = re.search(r'aria-checked="true"', confma.get_source)
        log.info(result)
        assert result
        confma.click_switch(0)
        result = re.search(r'aria-checked="false"', confma.get_source)
        log.info(result)
        assert result

        # 服务默认阈值
        confma.click_DefaultEdit()
        confma.input_box('')
        confma.click_Tick()
        result = re.search(r'服务熔断默认阈值不能为空', confma.get_source)
        log.info(result)
        assert result
        confma.input_box('0')
        confma.click_Tick()
        result = re.search(r'值不能小于1', confma.get_source)
        log.info(result)
        assert result
        confma.input_box('101')
        confma.click_Tick()
        result = re.search(r'值不能大于100', confma.get_source)
        log.info(result)
        assert result
        confma.input_box('6')
        confma.click_fork()
        confma.click_DefaultEdit()
        confma.input_box('11')
        confma.click_Tick()
        result = re.search(r'操作成功', confma.get_source)
        log.info(result)
        assert result

        # 熔断阈值
        confma.click_list(0)
        confma.input_box('')
        confma.click_Tick()
        result = re.search(r'操作成功', confma.get_source)
        log.info(result)
        assert result
        confma.click_list(0)
        confma.input_box('0')
        confma.click_Tick()
        result = re.search(r'值不能小于1', confma.get_source)
        log.info(result)
        assert result
        confma.input_box('101')
        confma.click_Tick()
        result = re.search(r'值不能大于100', confma.get_source)
        log.info(result)
        assert result
        confma.click_fork()
        sleep()
        confma.click_list(0)
        confma.input_box('6')
        confma.click_fork()
        confma.click_list(0)
        confma.input_box('13')
        confma.click_Tick()
        result = re.search(r'<span>13</span>', confma.get_source)
        log.info(result)
        assert result

    @allure.story("流量控制")
    def test_004(self, drivers):
        """流量控制测试"""
        confma = ConfigManage(drivers)
        confma.click_Menu('流量控制')
        result = re.search(r'流量控制默认网速', confma.get_source)
        log.info(result)
        assert result

        # 流量控制开关
        confma.click_switch(0)
        result = re.search(r'aria-checked="true"', confma.get_source)
        log.info(result)
        assert result
        confma.click_switch(0)
        result = re.search(r'aria-checked="false"', confma.get_source)
        log.info(result)
        assert result

        # 流量控制默认网速
        confma.click_DefaultEdit()
        confma.input_box('-1')
        confma.click_Tick()
        result = re.search(r'值不能小于0', confma.get_source)
        log.info(result)
        assert result
        confma.input_box('101')
        confma.click_Tick()
        result = re.search(r'值不能大于100', confma.get_source)
        log.info(result)
        assert result
        confma.input_box('6')
        confma.click_fork()
        confma.click_DefaultEdit()
        confma.input_box('11')
        confma.click_Tick()
        result = re.search(r'操作成功', confma.get_source)
        log.info(result)
        assert result

        # 流量权重
        confma.click_list(0)
        confma.input_box('-1')
        confma.click_Tick()
        result = re.search(r'值不能小于0', confma.get_source)
        log.info(result)
        assert result
        confma.input_box('0.1')
        confma.click_Tick()
        result = re.search(r'只能输入整数', confma.get_source)
        log.info(result)
        assert result
        confma.input_box('101')
        confma.click_Tick()
        result = re.search(r'值不能大于100', confma.get_source)
        log.info(result)
        assert result
        confma.click_fork()
        sleep()
        confma.click_list(0)
        confma.input_box('6')
        confma.click_fork()
        confma.click_list(0)
        confma.input_box('13')
        confma.click_Tick()
        result = re.search(r'<span>13</span>', confma.get_source)
        log.info(result)
        assert result

    @allure.story("服务质量")
    def test_005(self, drivers):
        """服务质量测试"""
        confma = ConfigManage(drivers)
        confma.click_Menu('服务质量')
        result = re.search(r'保留值', confma.get_source)
        log.info(result)
        assert result

        # 服务质量开关
        confma.click_switch(0)
        result = re.search(r'aria-checked="true"', confma.get_source)
        log.info(result)
        assert result
        confma.click_switch(0)
        result = re.search(r'aria-checked="false"', confma.get_source)
        log.info(result)
        assert result

        # 服务质量操作保留值
        confma.click_list(0)
        confma.input_retain('-1')
        confma.click_Tick()
        result = re.search(r'值不能小于0', confma.get_source)
        log.info(result)
        assert result
        confma.input_retain('0.1')
        confma.click_Tick()
        result = re.search(r'只能输入整数', confma.get_source)
        log.info(result)
        assert result
        confma.input_retain('101')
        confma.click_Tick()
        result = re.search(r'值不能大于100', confma.get_source)
        log.info(result)
        assert result
        confma.input_retain('22')
        confma.click_Tick()
        result = re.search(r'<span>22</span>', confma.get_source)
        log.info(result)
        assert result

        # 服务质量操作保留值
        confma.click_list(0)
        confma.input_upper('-1')
        confma.click_Tick()
        result = re.search(r'值不能小于0', confma.get_source)
        log.info(result)
        assert result
        confma.input_upper('0.1')
        confma.click_Tick()
        result = re.search(r'只能输入整数', confma.get_source)
        log.info(result)
        assert result
        confma.input_upper('101')
        confma.click_Tick()
        result = re.search(r'值不能大于100', confma.get_source)
        log.info(result)
        assert result
        confma.input_upper('23')
        confma.click_Tick()
        result = re.search(r'<span>23</span>', confma.get_source)
        log.info(result)
        assert result

        # 服务质量操作权重
        confma.click_list(0)
        confma.input_weight('-1')
        confma.click_Tick()
        result = re.search(r'值不能小于0', confma.get_source)
        log.info(result)
        assert result
        confma.input_weight('0.1')
        confma.click_Tick()
        result = re.search(r'只能输入整数', confma.get_source)
        log.info(result)
        assert result
        confma.input_weight('101')
        confma.click_Tick()
        result = re.search(r'值不能大于100', confma.get_source)
        log.info(result)
        assert result
        confma.input_weight('24')
        confma.click_Tick()
        result = re.search(r'<span>24</span>', confma.get_source)
        log.info(result)
        assert result

        # 服务质量一起操作
        confma.click_list(0)
        confma.input_retain('')
        confma.input_upper('')
        confma.input_weight('')
        confma.click_Tick()
        result = re.search(r'操作成功', confma.get_source)
        log.info(result)
        assert result

        confma.click_list(0)
        confma.input_retain('66')
        confma.input_upper('77')
        confma.input_weight('88')
        confma.click_fork()
        confma.click_ButtoNo(0)
        sleep()
        confma.click_fork()
        sleep()
        confma.click_ButtonYes(0)
        result = re.search(r'<span>66</span>', confma.get_source)
        log.info(result)
        assert not result

        confma.click_list(0)
        confma.input_retain('66')
        confma.input_upper('77')
        confma.input_weight('88')
        confma.click_Tick()
        result = re.search(r'<span>66</span>', confma.get_source)
        log.info(result)
        assert result

    @allure.story("服务降级")
    def test_006(self, drivers):
        """服务质量测试"""
        confma = ConfigManage(drivers)
        confma.click_Menu('服务降级')
        result = re.search(r'服务降级默认阈值', confma.get_source)
        log.info(result)
        assert result

        # 服务质量开关
        confma.click_switch(0)
        result = re.search(r'aria-checked="true"', confma.get_source)
        log.info(result)
        assert result
        confma.click_switch(0)
        result = re.search(r'aria-checked="false"', confma.get_source)
        log.info(result)
        assert result

        # 服务降级默认阈值
        confma.click_DefaultEdit()
        confma.input_box('0')
        confma.click_Tick()
        result = re.search(r'值不能小于1', confma.get_source)
        log.info(result)
        assert result
        confma.input_box('101')
        confma.click_Tick()
        result = re.search(r'值不能大于100', confma.get_source)
        log.info(result)
        assert result
        confma.input_box('6')
        confma.click_fork()
        confma.click_DefaultEdit()
        confma.input_box('26')
        confma.click_Tick()
        result = re.search(r'操作成功', confma.get_source)
        log.info(result)
        assert result

        # 服务降级阈值
        confma.click_list(0)
        confma.input_box('0')
        confma.click_Tick()
        result = re.search(r'值不能小于1', confma.get_source)
        log.info(result)
        assert result
        confma.input_box('0.1')
        confma.click_Tick()
        result = re.search(r'只能输入整数', confma.get_source)
        log.info(result)
        assert result
        confma.input_box('101')
        confma.click_Tick()
        result = re.search(r'值不能大于100', confma.get_source)
        log.info(result)
        assert result
        confma.input_box('25')
        confma.click_fork()
        result = re.search(r'<span>25</span>', confma.get_source)
        log.info(result)
        assert not result
        confma.click_list(0)
        confma.input_box('26')
        confma.click_Tick()
        result = re.search(r'<span>26</span>', confma.get_source)
        log.info(result)
        assert result

        # 降级服务
        confma.click_DegradServList(0)
        result = re.search(r'ant-select ant-select-focused ant-select-single ant-select-show-arrow ant-select-open', confma.get_source)
        log.info(result)
        assert result
        confma.click_DegradServ(0)
        result = re.search(r'操作成功', confma.get_source)  # 如果之前就选中了第一个元素，这里不会出现操作成功按钮，会报错
        log.info(result)
        assert result
        # 最后选中空白元素，将环境还原
        confma.click_DegradServList(0)
        confma.click_DegradServEnd()
        result = re.search(r'操作成功', confma.get_source)
        log.info(result)
        assert result

@allure.feature("黑白名单")
class TestBlacklist:
    @pytest.fixture(scope='session', autouse=auto)
    def open_devops(self, drivers):
        """打开courier"""
        login = LoginPage(drivers)
        login.get_url(ini.url)
        login.input_username_login('admin')
        login.input_password_login('password')
        login.click_login()
        login.click_Menu("服务网关")
        login.click_Menu("黑白名单")

    @allure.story("点击黑白名单")
    def test_001(self, drivers):
        """点击黑白名单"""
        blackli = Blacklist(drivers)
        blackli.click_Menu('黑白名单')
        blackli.waite_element('白名单管理')
        result = re.search(r'IP地址', blackli.get_source)
        log.info(result)
        assert result

    @allure.story("白名单添加")
    def test_002(self, drivers):
        """白名单添加测试"""
        blackli = Blacklist(drivers)
        blackli.click_Menu('白名单管理')
        blackli.click_add(0)
        result = re.search(r'添加白名单', blackli.get_source)
        log.info(result)
        assert result
        blackli.click_Define()
        result = re.search(r'请输入正确的IP地址', blackli.get_source)
        log.info(result)
        assert result
        blackli.input_ip('1234')
        blackli.click_Define()
        result = re.search(r'请输入正确的IP地址', blackli.get_source)
        log.info(result)
        assert result
        blackli.input_ip('10.0.2.3')
        blackli.click_Canle()
        blackli.click_add(0)
        blackli.input_ip('10.0.2.3')
        blackli.click_close()
        blackli.click_add(0)
        blackli.input_ip('10.0.2.4')
        blackli.click_Define()
        result = re.search(r'10.0.2.4', blackli.get_source)
        log.info(result)
        assert result

    @allure.story("白名单刷新")
    def test_003(self, drivers):
        """白名单刷新测试"""
        blackli = Blacklist(drivers)
        blackli.click_refresh()
        result = re.search(r'anticon anticon-reload ant-tooltip-open', blackli.get_source)
        log.info(result)
        assert result

    @allure.story("白名单编辑")
    def test_004(self, drivers):
        """白名单编辑测试"""
        blackli = Blacklist(drivers)
        blackli.click_edit(0)
        blackli.input_ip('')
        blackli.click_Define()
        blackli.input_ip('4.3.2.1')
        blackli.click_Define()
        result = re.search(r'4.3.2.1', blackli.get_source)
        log.info(result)
        assert result

    @allure.story("白名单删除")
    def test_005(self, drivers):
        """白名单删除测试"""
        blackli = Blacklist(drivers)
        # blackli.click_gatedel(0)
        # blackli.click_ButtoNo(0)
        blackli.click_gatedel(0)
        blackli.click_ButtonYes(0)
        result = re.search(r'删除成功', blackli.get_source)
        log.info(result)
        assert result

    @allure.story("黑名单添加")
    def test_006(self, drivers):
        """黑名单添加测试"""
        blackli = Blacklist(drivers)
        blackli.click_Menu('黑名单管理')
        blackli.click_add(1)
        result = re.search(r'添加黑名单', blackli.get_source)
        log.info(result)
        assert result
        blackli.click_Define()
        result = re.search(r'请输入正确的IP地址', blackli.get_source)
        log.info(result)
        assert result
        blackli.input_ip('1234')
        blackli.click_Define()
        result = re.search(r'请输入正确的IP地址', blackli.get_source)
        log.info(result)
        assert result
        blackli.input_ip('10.0.2.4')
        blackli.click_Canle()
        blackli.click_add(1)
        blackli.input_ip('10.0.2.4')
        blackli.click_close()
        blackli.click_add(1)
        blackli.input_ip('10.0.2.5')
        blackli.click_Define()
        result = re.search(r'10.0.2.5', blackli.get_source)
        log.info(result)
        assert result

    @allure.story("黑名单编辑")
    def test_007(self, drivers):
        """黑名单编辑测试"""
        blackli = Blacklist(drivers)
        blackli.click_edit(0)
        blackli.input_ip('')
        blackli.click_Define()
        blackli.input_ip('4.3.2.1')
        blackli.click_Define()
        result = re.search(r'4.3.2.1', blackli.get_source)
        log.info(result)
        assert result

    @allure.story("黑名单删除")
    def test_008(self, drivers):
        """黑名单删除测试"""
        blackli = Blacklist(drivers)
        # blackli.click_gatedel(0)
        # blackli.click_ButtoNo(0)
        blackli.click_gatedel(0)
        blackli.click_ButtonYes(0)
        result = re.search(r'删除成功', blackli.get_source)
        log.info(result)
        assert result

@allure.feature("地理位置")
class TestLocation:
    @pytest.fixture(scope='session', autouse=auto)
    def open_devops(self, drivers):
        """打开courier"""
        login = LoginPage(drivers)
        login.get_url(ini.url)
        login.input_username_login('admin')
        login.input_password_login('password')
        login.click_login()
        login.click_Menu("服务网关")
        login.click_Menu("地理位置")

    @allure.story("点击地理位置")
    def test_001(self, drivers):
        """点击地理位置"""
        local = Location(drivers)
        local.click_Menu('地理位置')
        local.waite_element('开关按钮')
        result = re.search(r'区域经纬度', local.get_source)
        log.info(result)
        assert result

    @allure.story("地理位置启用开关")
    def test_002(self, drivers):
        """地理位置启用开关测试"""
        local = Location(drivers)
        local.click_switch(0)
        sleep()
        result = re.search(r'aria-checked="true"', local.get_source)
        log.info(result)
        assert result
        local.click_switch(0)
        result = re.search(r'aria-checked="false"', local.get_source)
        log.info(result)
        assert result

    @allure.story("地理位置添加")
    def test_003(self, drivers):
        """地理位置添加测试"""
        local = Location(drivers)
        local.click_add(0)
        result = re.search(r'添加地理位置', local.get_source)
        log.info(result)
        assert result

        local.click_Define()
        result = re.search(r'请输入区域半径', local.get_source)
        log.info(result)
        assert result
        # 新增框取消与关闭
        local.input_locationame("区域1")
        local.input_longtitude("12.3")
        local.input_latitude('31.5')
        local.input_radius('13.6')
        local.click_Canle()
        result = re.search(r'<span>[12.3, 31.5]', local.get_source)
        log.info(result)
        assert not result
        local.click_add(0)
        local.input_locationame("区域1")
        local.input_longtitude("12.3")
        local.input_latitude('31.6')
        local.input_radius('13.6')
        local.click_close()
        result = re.search(r'<span>[12.3, 31.6]', local.get_source)
        log.info(result)
        assert not result

        local.click_add(0)
        local.input_locationame("区域1")
        local.input_longtitude("22.3")
        local.input_latitude('33.5')
        local.input_radius('15')
        local.click_Define()
        result = re.search(r'<span>[22.3, 33.5]', local.get_source)
        log.info(result)
        assert not result

    @allure.story("地理位置刷新")
    def test_004(self, drivers):
        """地理位置刷新测试"""
        local = Location(drivers)
        local.click_refresh()
        result = re.search(r'anticon anticon-reload ant-tooltip-open', local.get_source)
        log.info(result)
        assert result

    @allure.story("地理位置展示数量下拉框")
    def test_005(self, drivers):
        """地理位置展示数量下拉框测试"""

        local = Location(drivers)
        local.click_Menu('下拉展示条')
        local.click_Menu('10条')
        result = re.search(r'<span.*?10 条/页', local.get_source)
        log.info(result)
        assert result
        local.click_Menu('下拉展示条')
        local.click_Menu('20条')
        result = re.search(r'<span.*?20 条/页', local.get_source)
        log.info(result)
        assert result
        local.click_Menu('下拉展示条')
        local.click_Menu('50条')
        result = re.search(r'<span.*?50 条/页', local.get_source)
        log.info(result)
        assert result
        local.click_Menu('下拉展示条')
        local.click_Menu('100条')
        result = re.search(r'<span.*?100 条/页', local.get_source)
        log.info(result)
        assert result

    @allure.story("地理位置开启强制刷新")
    def test_006(self, drivers):
        """地理位置刷新测试"""
        local = Location(drivers)
        local.click_switch(1)
        result = re.search(r'更改成功', local.get_source)
        log.info(result)
        assert result
        local.click_switch(1)
        result = re.search(r'更改成功', local.get_source)
        log.info(result)
        assert result

    @allure.story("地理位置编辑")
    def test_007(self, drivers):
        """地理位置编辑测试"""
        local = Location(drivers)
        local.click_edit(0)
        result = re.search(r'编辑地理位置', local.get_source)
        log.info(result)
        assert result
        try:
            local.input_locationame("区域2")
        except Exception as e:
            log.info(f"报错：{e}, \n编辑时，区域名无法点击")
        local.input_longtitude("3")
        local.input_latitude('4')
        local.input_radius('5')
        local.click_Define()
        result = re.search(r'编辑成功', local.get_source)
        log.info(result)
        assert result

    @allure.story("地理位置删除")
    def test_008(self, drivers):
        """地理位置删除测试"""
        local = Location(drivers)
        local.click_gatedel(0)
        # sleep()
        # local.click_ButtoNo(0)
        # local.click_gatedel(0)
        # sleep(2)
        local.click_ButtonYes(0)
        result = re.search(r'删除成功', local.get_source)
        log.info(result)
        assert result

@allure.feature("条件表达式")
class TestConditional:
    @pytest.fixture(scope='session', autouse=auto)
    def open_devops(self, drivers):
        """打开courier"""
        login = LoginPage(drivers)
        login.get_url(ini.url)
        login.input_username_login('admin')
        login.input_password_login('password')
        login.click_login()
        login.click_Menu("服务网关")
        login.click_Menu("条件表达式")

    @allure.story("点击条件表达式")
    def test_001(self, drivers):
        """点击地理位置"""
        condit = Location(drivers)
        condit.click_Menu('条件表达式')
        condit.waite_element('服务名输入')
        result = re.search(r'开启', condit.get_source)
        log.info(result)
        assert result

    @allure.story("添加条件表达式取消退出")
    def test_002(self, drivers):
        """添加条件表达式测试"""

        # 添加框取消退出
        condit = Conditional(drivers)
        condit.click_add(0)
        condit.click_Define()
        result = re.search(r'请输入服务名', condit.get_source)
        log.info(result)
        assert result
        condit.input_servicename(num=1, content='服务名1')
        condit.click_Menu('force')
        result = re.search(r'<button id="force.*?aria-checked="true"', condit.get_source)
        log.info(result)
        assert result
        condit.click_Menu('force')

        condit.click_Menu('enabled')
        result = re.search(r'<button id="enabled.*?aria-checked="true"', condit.get_source)
        log.info(result)
        assert result
        condit.click_Menu('enabled')
        condit.click_Canle()
        condit.click_add(0)
        condit.click_close()

    @allure.story("添加条件表达式")
    def test_003(self, drivers):
        """添加条件表达式测试"""

        # 添加框输入
        condit = Conditional(drivers)
        condit.click_add(0)
        condit.input_servicename(num=1, content='服务名1')
        condit.click_Menu('force')
        condit.click_Menu('enabled')

        # tag1
        condit.input_tagname1('标签名称1')
        condit.input_address1("10.0.1.1")
        condit.click_address(0)
        result = re.search(r'tags_0_address_1', condit.get_source)
        log.info(result)
        assert result
        condit.input_address2("10.0.1.2")
        result = re.search(r'10.0.1.2', condit.get_source)
        log.info(result)
        assert result

        # tag2
        condit.click_Menu('添加tag')
        condit.input_tagname2('标签名称2')
        condit.input_2address1("10.0.2.1")
        condit.click_address(1)
        result = re.search(r'tags_1_address_1', condit.get_source)
        log.info(result)
        assert result
        condit.input_2address2("10.0.2.2")
        result = re.search(r'10.0.2.2', condit.get_source)
        log.info(result)
        assert result
        condit.click_Define()
        result = re.search(r'服务名1', condit.get_source)
        log.info(result)
        assert result

    @allure.story("条件表达式搜索")
    def test_004(self, drivers):
        """条件表达式搜索测试"""

        # 新建两个服务
        condit = Conditional(drivers)
        condit.click_add(0)
        condit.input_servicename(num=1, content='服务名2')
        condit.input_tagname1('标签名称2')
        condit.input_address1("10.0.1.2")
        condit.click_Define()
        result = re.search(r'服务名2', condit.get_source)
        log.info(result)
        assert result

        condit.click_add(0)
        condit.input_servicename(num=1, content='服务名3')
        condit.input_tagname1('标签名称3')
        condit.input_address1("10.0.1.3")
        condit.click_Define()
        result = re.search(r'服务名3', condit.get_source)
        log.info(result)
        assert result

        # 搜索服务名2
        condit.input_servicename(num=0, content='服务名2')
        condit.click_search()
        result = re.search(r'服务名3', condit.get_source)
        log.info(result)
        assert not result
        condit.click_gatedel(0)
        condit.click_ButtonYes(0)
        condit.click_reset()
        result = re.search(r'服务名2', condit.get_source)
        log.info(result)
        assert not result

        # 搜索服务名3
        condit.input_servicename(num=0, content='服务名3')
        condit.click_search()
        result = re.search(r'服务名3', condit.get_source)
        log.info(result)
        assert result
        condit.click_gatedel(0)
        condit.click_ButtonYes(0)
        condit.click_reset()
        result = re.search(r'服务名3', condit.get_source)
        log.info(result)
        assert not result

    @allure.story("条件表达式刷新")
    def test_005(self, drivers):
        """条件表达式刷新测试"""

        condit = Conditional(drivers)
        condit.click_refresh()
        result = re.search(r'anticon anticon-reload ant-tooltip-open', condit.get_source)
        log.info(result)
        assert result

    @allure.story("条件表达式展示数量下拉框")
    def test_006(self, drivers):
        """条件表达式刷新测试"""

        condit = Conditional(drivers)
        condit.click_Menu('下拉展示条')
        condit.click_Menu('10条')
        result = re.search(r'<span.*?10 条/页', condit.get_source)
        log.info(result)
        assert result
        condit.click_Menu('下拉展示条')
        condit.click_Menu('20条')
        result = re.search(r'<span.*?20 条/页', condit.get_source)
        log.info(result)
        assert result
        condit.click_Menu('下拉展示条')
        condit.click_Menu('50条')
        result = re.search(r'<span.*?50 条/页', condit.get_source)
        log.info(result)
        assert result
        condit.click_Menu('下拉展示条')
        condit.click_Menu('100条')
        result = re.search(r'<span.*?100 条/页', condit.get_source)
        log.info(result)
        assert result

    @allure.story("条件表达式详情")
    def test_007(self, drivers):
        """条件表达式刷新测试"""

        condit = Conditional(drivers)
        condit.click_details(0)
        result = re.search(r'条件表达式详情', condit.get_source)
        log.info(result)
        assert result
        condit.click_close()
        condit.click_details(0)
        condit.click_Canle()
        result = re.search(r'条件表达式详情', condit.get_source)
        log.info(result)
        assert not result

    @allure.story("条件表达式编辑")
    def test_008(self, drivers):
        """条件表达式编辑测试"""

        condit = Conditional(drivers)
        condit.click_edit(0)
        result = re.search(r'编辑条件表达式', condit.get_source)
        log.info(result)
        assert result
        condit.input_tagname1("new标签")
        condit.input_address1("10.0.1.5")
        condit.click_Define()
        result = re.search(r'编辑成功', condit.get_source)
        log.info(result)
        assert result

    @allure.story("条件表达式开启关闭")
    def test_009(self, drivers):
        """条件表达式开启关闭测试"""

        condit = Conditional(drivers)

        # 关闭
        condit.click_shut(0)
        # sleep()
        # condit.click_ButtoNo(0)
        # condit.click_shut(0)
        # sleep(2)
        sleep()
        condit.click_ButtonYes(0)
        result = re.search(r'更改成功', condit.get_source)
        log.info(result)
        assert result

        #开启
        condit.click_opens(0)
        # sleep()
        # condit.click_ButtoNo(0)
        # condit.click_opens(0)
        # sleep(2)
        sleep()
        condit.click_ButtonYes(0)
        result = re.search(r'更改成功', condit.get_source)
        log.info(result)
        assert result

    @allure.story("条件表达式删除")
    def test_010(self, drivers):
        """条件表达式删除测试"""

        condit = Conditional(drivers)
        condit.click_gatedel(0)
        # 当全部执行时，上个用例操作后，页面元素中会多一个重复元素，这时改为1
        # condit.click_ButtoNo(1)
        # condit.click_gatedel(0)

        # 单独执行该用例时，参数为 0
        # condit.click_ButtoNo(0)
        # condit.click_gatedel(0)
        # condit.click_ButtonYes(0)

        condit.click_ButtonYes(1)
        result = re.search(r'删除成功', condit.get_source)
        log.info(result)
        assert result

@allure.feature("指标统计")
class TestStatistics:
    @pytest.fixture(scope='session', autouse=auto)
    def open_devops(self, drivers):
        """打开courier"""
        login = LoginPage(drivers)
        login.get_url(ini.url)
        login.input_username_login('admin')
        login.input_password_login('password')
        login.click_login()
        login.click_Menu("指标统计")

    @allure.story("点击指标统计")
    def test_001(self, drivers):
        """点击指标统计"""
        stati = Statistics(drivers)
        stati.click_Menu('指标统计')
        stati.waite_element('端口')
        result = re.search(r'成功次数', stati.get_source)
        log.info(result)
        assert result

    @allure.story("指标统计搜索")
    def test_002(self, drivers):
        """点击指标统计"""
        stati = Statistics(drivers)
        stati.click_search()
        result = re.search(r'请输入IP', stati.get_source)
        log.info(result)
        assert result

        # 搜索
        stati.input_ip('192.168.31.10')
        stati.click_search()
        result = re.search(r'请输入端口号', stati.get_source)
        log.info(result)
        assert result

        stati.input_port('1523')
        stati.click_search()
        result = re.search(r'请输入服务名', stati.get_source)
        log.info(result)
        assert result

        stati.input_serviceName('conditionservice')
        stati.click_search()
        result = re.search(r'请输入服务名', stati.get_source)
        log.info(result)
        assert not result

        #重置
        stati.click_reset()
        result = re.search(r'192.168.31.10', stati.get_source)
        log.info(result)
        assert not result

    @allure.story("指标统计刷新")
    def test_003(self, drivers):
        """指标统计刷新测试"""
        stati = Statistics(drivers)
        stati.click_refresh()
        result = re.search(r'anticon anticon-reload ant-tooltip-open', stati.get_source)
        log.info(result)
        assert result

if __name__ == '__main__':
    pytest.main(['TestCase/test_courier_login.py', '-sv'])

# if __name__ == '__main__':
# 下面的代码使用pycharm运行可能会没有生成报告，建议使用vscode执行
#     import os
#     pytest.main(['TestCase/test_search.py', '--alluredir', './allure'])
#     os.system('allure serve allure')
