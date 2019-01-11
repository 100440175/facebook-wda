#coding=utf-8
import os
import time
import unittest

import wda
from test_login import test_new_loan, create_session, account_login


def test_new_loan():
    """
    测试 新建报单
    """
    assert d(label=u"首页").wait()  # 等待8s
    print("开始新建报单>>>")
    print("点击快速报单>>>")
    time.sleep(10)
    d(label=u"快速报单", name=u"快速报单", type="StaticText").wait()
    d(label=u"快速报单", name=u"快速报单", type="StaticText").tap()
    # d(label=u"快速报单", name=u"快速报单", type="StaticText").click()  # 默认会寻找10s，所以不用担心点不到
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





if __name__ == '__main__':
    d = create_session()
    account_login(d)
    test_new_loan()