# -*- coding: utf-8 -*-
# @Time    : 2017/11/15 下午8:48
# @Author  : Jalo.Mu
# @Site    : 
# @File    : list.py
# @Software: PyCharm

from flask import request, jsonify
from flask_login import login_required

from app import db
from decorator.authority import permissons_required
from modelsDB.users.user import Users
from service.db.userinfo.userTable import UserTab
from .. import user


@user.route('/list', methods=["GET"])
@login_required
@permissons_required("Admin")
def list():
    if request.args.to_dict():
        parms = request.args.to_dict()
    else:
        parms = {'num': 10, 'page': 0}
    u =  UserTab(db, Users, parms)
    res = u.list()
    return jsonify({
        'code': 1,
        'mgs': {
            'confirm': True,
            'message': res
        }
    })