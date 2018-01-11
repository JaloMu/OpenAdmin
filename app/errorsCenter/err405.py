# -*- coding: utf-8 -*-
# @Time    : 2017/11/6 下午8:53
# @Author  : Jalo.Mu
# @Site    : 
# @File    : 405.py
# @Software: PyCharm

from flask import jsonify, request
from . import error

@error.app_errorhandler(405)
def method_error(e):
    return jsonify({'code': 405, 'page': request.url})

