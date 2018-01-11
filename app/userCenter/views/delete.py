# -*- coding: utf-8 -*-
# @Time    : 2017/11/8 下午11:27
# @Author  : Jalo.Mu
# @Site    : 
# @File    : delete.py
# @Software: PyCharm
from flask import request, jsonify
from flask_login import current_user, login_required

from app import db
from decorator.authority import permissons_required
from modelsDB.users.user import Users
from service.db.userinfo.userTable import UserTab
from .. import user


def checkUser(params):
    if (params['username'] == current_user.username):
        return {
            "code": 0,
            "msg": {
                "info": "自己不能删除自己"
            }
        }

    if (params['username'] == 'Admin'):
        return {
            "code": 0,
            "msg": {
                "info": "超级管理员用户不能删除"
            }
        }
    return {
            "code": 1,
            "msg": {
                "info": "suc"
            }
        }

@user.route('/del', methods=["GET"])
@login_required
@permissons_required('Admin')
def delete():
    params = request.args.to_dict()
    if not checkUser(params)['code']:
        return jsonify({
        "code": 1,
        "page": request.url,
        "msg": checkUser(params)['msg']
    })
    deluser = UserTab(db, Users, params)
    msg = deluser.delRecord()
    return jsonify({
        "code": 1,
        "page": request.url,
        "msg": msg
    })

# @user.route('/dels', methods=["GET"])
# def deletes():
#     params = request.args.to_dict()
#     for k, v in params.items():
#         pass
#     deluser = UserTab(db, Users, params)
#     msg = deluser.delRecord()
#     return jsonify({
#         "code": 1,
#         "page": request.url,
#         "msg": msg
#     })