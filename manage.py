# -*- coding: utf-8 -*-
# @Time    : 2017/11/6 下午5:44
# @Author  : Jalo.Mu
# @Site    : 
# @File    : manage.py
# @Software: PyCharm

import os
from app import create_app, db
from modelsDB.users.user import Users
from modelsDB.users.permissions import Role
from modelsDB.cmdb.schema import Schema
from modelsDB.cmdb.entry import Entry
from modelsDB.cmdb.field import Field
from modelsDB.cmdb.value import Value
from modelsDB.users.login_info import LoginInfo

from flask_script import Manager, Shell, Server

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

def make_shell_context():
    return dict(app=app, db=db, Users=Users, LoginInfo=LoginInfo, Role=Role, Schema=Schema, Field=Field, Entry=Entry, Value=Value )

manager.add_command("runserver", Server(host=app.config['HOST'], port=app.config['PORT']))
manager.add_command("shell", Shell(make_context=make_shell_context,use_ipython=True))



if __name__ == '__main__':
    manager.run()