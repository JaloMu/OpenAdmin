# -*- coding: utf-8 -*-
# @Time    : 2017/11/6 下午8:53
# @Author  : Jalo.Mu
# @Site    : 
# @File    : 403.py
# @Software: PyCharm

from flask import jsonify, request
from . import error


@error.app_errorhandler(403)
def forbidden(e):
    return jsonify({'code': 403, 'page': request.url})

