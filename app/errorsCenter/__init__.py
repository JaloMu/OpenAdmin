# -*- coding: utf-8 -*-
# @Time    : 2017/11/6 下午8:52
# @Author  : Jalo.Mu
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Blueprint

error = Blueprint("error", __name__)

from . import err400, err403,err404, err405, err500, err503