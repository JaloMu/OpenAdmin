# -*- coding: utf-8 -*-
# @Time    : 2017/11/12 下午7:43
# @Author  : Jalo.Mu
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm

class BasePermission:
    ADMIN = 0x00
    READ = 0x01
    MOD = 0x02
    CREATE = 0x04
    AUDIT = 0x08