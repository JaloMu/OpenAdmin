# -*- coding: UTF-8 -*-
from datetime import datetime

from flask import request, jsonify
from flask_login import login_required, current_user

from app import db
from decorator.authority import permissons_required
from modelsDB.users.user import Users
from service.db.userinfo.userTable import UserTab
from .. import user


def exist(key):
    if Users.query.filter_by(username=key).all():
        return True
    return False


@user.route('/add', methods=["POST"])
@login_required
@permissons_required('Admin')
def add():
    if exist(request.get_json()['username']):
        return jsonify({
            'code': 0,
            'mgs': {
                'confirm': True,
                'message': 'Users already exist'
            }
        })
    parms =request.get_json()
    tab = {
        'create_user':current_user.username.decode(),
        'updata_user': current_user.username.decode(),
        'uuid_hash':parms['username'],
        'create_date': datetime.now(),
        'updata_date': datetime.now(),
    }

    parms.update(tab)
    adduser = UserTab(db, Users,parms)
    res = adduser.addRecord()
    if res['confirm']:
        return jsonify({
            'code': 1,
            'page': request.get_json(),
            'mgs': res
        })
    return jsonify({
                'code': 0,
                'page': request.get_json(),
                'mgs': res
            })
