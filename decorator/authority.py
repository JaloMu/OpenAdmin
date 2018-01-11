# -*- coding: utf-8 -*-
# @Time    : 2017/11/12 下午8:00
# @Author  : Jalo.Mu
# @Site    : 
# @File    : authority.py
# @Software: PyCharm
from functools import wraps
from flask_login import current_user
from flask import abort

def permissons_required(permission):
    def decorator(fn):
        @wraps(fn)
        def wrap(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return fn(*args, **kwargs)
        return wrap
    return decorator
