# -*- coding: utf-8 -*-
# @Time    : 2017/11/6 下午8:52
# @Author  : Jalo.Mu
# @Site    : 
# @File    : 500.py
# @Software: PyCharm

from flask import jsonify, request
from . import error

@error.app_errorhandler(500)
def internal_server_error(e):
    return jsonify({'code': 500, 'page': request.url})