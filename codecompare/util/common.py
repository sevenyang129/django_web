# -*- coding: utf-8 -*-
# 作者  gongxc   
# 日期 2020/6/5  16:12 
# 文件  common
from django.db import DataError
from codecompare.models import User


def add_register_data(**kwargs):
    """
    用户注册信息逻辑判断及落地
    :param kwargs: dict
    :return: ok or tips
    """
    user_info = User.objects
    try:
        username = kwargs.pop('user')
        password = kwargs.pop('pw')
        station = kwargs.pop('station')

        if user_info.filter(username__exact=username).count() > 0:
            return '该用户名已被注册，请更换用户名'
        user_info.create(username=username, password=password, station=station)
        return 'ok'
    except DataError:
        return '字段长度超长，请重新编辑'