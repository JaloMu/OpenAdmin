# -*- coding: utf-8 -*-
# @Time    : 2017/11/6 下午8:52
# @Author  : Jalo.Mu
# @Site    : 
# @File    : 404.py
# @Software: PyCharm

from flask import jsonify, request
from . import error

@error.app_errorhandler(404)
def page_not_found(e):
    return jsonify({'code': 400, 'page': request.url})

