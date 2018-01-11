# -*- coding: utf-8 -*-
# @Time    : 2017/11/26 下午5:48
# @Author  : Jalo.Mu
# @Site    : 
# @File    : create.py
# @Software: PyCharm

from flask import request, jsonify
from flask_login import login_required, current_user
from app import db
from decorator.authority import permissons_required

from modelsDB.cmdb.schema import Schema
from modelsDB.cmdb.field import Field
from modelsDB.cmdb.entry import Entry
from modelsDB.cmdb.value import Value
from service.db.cmdb import schame
from service.db.cmdb import field
from .. import cmdb


@cmdb.route('/create/schema', methods=["POST"])
@login_required
@permissons_required('Admin')
def createSchema():
    parms = request.get_json()
    ret = schame.create(db,Schema, **parms)
    return jsonify({
        'code': 0,
        'mgs': {
            'confirm': True,
            'message': 'cmdb create {}'.format(ret)
        }
    })

@cmdb.route('/create/field', methods=["POST"])
@login_required
@permissons_required('Admin')
def createField():
    parms = request.get_json()
    args = request.args.to_dict()
    ret = field.create(db, Field, int(args["id"]),**parms)
    return jsonify({
        'code': 0,
        'mgs': {
            'confirm': True,
            'message': 'cmdb create {}'.format(ret)
        }
    })


@cmdb.route('/del', methods=["POST"])
@login_required
@permissons_required('Admin')
def delete():
    parms = request.get_json()
    operations = Operations(db,Schema)
    ret = operations.delete(**parms)
    return jsonify({
        'code': 0,
        'mgs': {
            'confirm': True,
            'message': 'cmdb create {}'.format(ret)
        }
    })

