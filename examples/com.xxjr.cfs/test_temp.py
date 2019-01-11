#coding=utf-8

import pytest


# 功能函数
def multiply(a,b):
    return a * b

# =====fixtures========
def setup_module(module):
    print ("\n")
    print ("setup_module================>")

def teardown_module(module):
    print ("teardown_module=============>")

def setup_function(function):
    print ("setup_function------>")

def teardown_function(function):
    print ("teardown_function--->")

# setup_module/teardown_module        在所有测试用例执行之后和之后执行。
# setup_function/teardown_function    在每个测试用例之后和之后执行。




# =====测试用例========
def test_numbers_3_4():
    # print 'test_numbers_3_4'
    assert multiply(3,4) == 12


def test_strings_a_3():
    # print 'test_strings_a_3'
    assert multiply('a',3) == 'aaa'

if __name__ == '__main__':
    pytest.main("-s test_fixtures.py")


def test_new_loan(self,account_login):
    """
    测试 快速报单->新建报单
    """
    s(label=u"快速报单", className='StaticText').tap()

    # assert s(name=u'听歌识曲', visible=True).wait()
    # s(name=u'私人FM').tap()
    # assert s(name=u'不再播放').exists
    # assert s(name=u'添加到我喜欢的音乐').exists
    # assert s(name=u'00:00', className='StaticText').exists
    # s(nameMatches=u'(暂停|播放)').tap()
    # assert s(name=u'00:00', className='StaticText').wait_gone(10.0)
    # s(name=u'跑步FM').tap()
    # s(name=u'知道了').click_exists(2.0)

