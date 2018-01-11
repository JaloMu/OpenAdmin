# -*- coding: UTF-8 -*-
from flask import jsonify, request, current_app
from flask_login import login_user, logout_user, login_required

from app import db
from modelsDB.users.login_info import LoginInfo
from modelsDB.users.user import Users
from service.db.userinfo.loginInfoTable import Query
from .. import auth


@auth.route("/login", methods=["POST"])
def login():
    user = Users.query.filter_by(username=request.get_json().get('username')).first()
    if user is not None:
        if not user.is_active:
            return jsonify({
                'code':0,
                'page': 'login',
                'isactive': user.is_active,
                'msg': {
                    'info': '联系管理与激活用户'
            }
            })
        if user.verify_password(request.get_json().get("password")):
            q = Query(db, user, LoginInfo,request.remote_addr, current_app.config['QQPATH'])
            try:
                res = q.add()
                if (not res['confirm']):
                    print "================", res
                    raise {'code': 0, 'msg': 'ip not login'}
                login_user(user)
                return jsonify({
                    'code': 1,
                    'page': 'login',
                    'userInfo': {
                        'username': user.username,
                        'token': user.generate_confirmation_token(current_app.config["EXPIRATION"]),
                        'role': user.role.name
                    }
                })
            except Exception as e:
                print("=========e", e)
                return jsonify({"code": 0})
    return jsonify({
        'code':0,
        'page':'login',
        'msg': {
            'info': '用户不存在'
        }
    })



@auth.route('/logout', methods=["GET"])
@login_required
def logout():
    logout_user()
    return jsonify({
        'code':0,
        'page':'logout'
    })