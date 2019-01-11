#coding=utf-8
import os
import time
import unittest

import wda




bundle_id = 'com.xxjr.cfsApp'

c = wda.Client('http://localhost:8100')

# USERNAME = os.getenv('4080')
# PASSWORD = os.getenv('12345678')
USERNAME = '4080'
PASSWORD = '12345678'



def setup_function():
    # 每次测试之前，保证帐号是登录的
    global d
    d = create_session()
    account_login(d)


def teardown_function():
    account_logout(d)
    d.close() # 一次测试结束，关闭应用
    # s = create_session()
    # account_logout(s)
    # s.close()

def alert_callback(session):
    btns = set([u'不再提醒', 'OK', u'知道了', 'Allow', u'允许']).intersection(session.alert.buttons())
    if len(btns) == 0:
        raise RuntimeError("Alert can not handled, buttons: " + ', '.join(session.alert.buttons()))
    session.alert.click(list(btns)[0])

def create_session():
    d = c.session(bundle_id)
    d.set_alert_callback(alert_callback)
    return d


def account_login(d):
    # 输入帐号密码，验证是否登录成功
    d(type="TextField").clear_text()
    d(type="TextField").set_text(USERNAME)
    d(label=u"return").tap()
    d(type="SecureTextField").tap()
    d(type="SecureTextField").set_text(PASSWORD)
    d(label=u"Done").tap()
    d(label=u"登录", className='Button').tap()
    assert d(label=u"首页").wait() # 等待8s
    print("登录成功")


def account_logout(d):
    d(label=u"user head", type='Button').tap() # not support \s, wired
    # d(label=u"退出登录").scroll().tap()
    d(label=u"退出登录").tap()
    d.alert.click(u'确定')
    # d(label=u"确定").tap()
    assert d(label=u"登录").wait()
    print("已退出登陆")


def test_new_loan():
    """
    测试 新建报单
    """
    assert d(label=u"首页").wait()  # 等待8s
    print("开始新建报单>>>")
    print("点击快速报单>>>")
    assert d(label=u"快速报单").wait()
    d(name=u"home_icon_augment").tap()  # 默认会寻找10s，所以不用担心点不到
    print("点击快速报单成功>>>")
    # assert d(label=u"报单信息").wait(timeout=120)
    d(label=u"新增用户").tap()
    # assert d(label=u"新增客户").wait()
    print("开始新建客户>>>")



    """
    error：输入框这里没有唯一的元素值，无法定位。  只能开发添加元素值才能定位
    """
    d(type="TextField", instance=1).set_text("测试名")
    d(type="TextField", instance=3).set_text("18012341185")
    d(type="TextField", instance=7).set_text("360782198911215514")



    d(label=u"保存").tap()
    print("新建客户完成>>>")
    d(type="TextField", instance=11).set_text("测试数据")
    d(type="TextView", instance=1).set_text("测试数据")
    d(label=u"保存").tap()
    print("新建报单完成>>>")




