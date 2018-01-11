# -*- coding: UTF-8 -*-
from flask import request, jsonify
from flask_login import login_required

from app import db
from modelsDB.users.user import Users
from service.db.userinfo.userTable import UserTab
from .. import user


@user.route('/detail', methods = ["GET"])
@login_required
def detail():
    parms = request.args.to_dict()
    u = UserTab(db, Users, parms)
    res = u.detail()
    return jsonify({
            'code': 1,
            'mgs': res
        })
