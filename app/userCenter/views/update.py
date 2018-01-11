# -*- coding: utf-8 -*-
# @Time    : 2017/11/12 上午1:39
# @Author  : Jalo.Mu
# @Site    : 
# @File    : update.py
# @Software: PyCharm

from datetime import datetime

from flask import request, jsonify
from flask_login import login_required, current_user

from app import db
from decorator.authority import permissons_required
from modelsDB.users.user import Users
from service.db.userinfo.userTable import UserTab
from .. import user


@user.route('/update', methods=["POST"])
@login_required
@permissons_required("User")
def update():
    usertab = Users.query.filter_by(username=request.get_json()['username']).first()
    usertab.updata_user = current_user.username
    usertab.updata_date = datetime.now()
    change = UserTab(db, usertab, request.get_json())
    res = change.updateRecord()
    return jsonify({
                'code': 1,
                'page': request.url,
                'mgs': res
            })