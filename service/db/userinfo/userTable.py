# -*- coding: utf-8 -*-
# @Time    : 2017/11/12 上午1:54
# @Author  : Jalo.Mu
# @Site    : 
# @File    : usertable.py
# @Software: PyCharm
from modelsDB.users.permissions import Role
class UserTab():
    '''
        @db: 数据引擎
        @tables 所有的表列表
        @kwargs 添加的数据
    '''
    def __init__(self, db, tab, kwargs):
        self.db = db
        self.tab = tab
        self.kwargs = kwargs

    def detail(self):
        record = {}
        try:
            if self.kwargs.has_key('id'):
                userli = self.tab.query.filter_by(id = self.kwargs['id']).first()
                record = userli.to_json()
                return {
                    'confirm': True,
                    'message': record
                }
            elif self.kwargs.has_key('username'):
                    userli = self.tab.query.filter_by(username=self.kwargs['username']).first()
                    record = userli.to_json()
                    return {
                        'confirm': True,
                        'message': record
                    }
            else:
                return {
                    'confirm': False,
                    'message': 'User is not exist!!!'
                }
        except Exception as e:
            return {
                'confirm': False,
                'message': e
            }

    def list(self):
        record = {}
        try:
            userli = self.tab.query.limit(self.kwargs['num']).offset(self.kwargs['page']).all()
            if userli is not None:
                for res in userli:
                    record[res.id] = res.to_json()
            return {
                'confirm': True,
                'message': record
            }
        except Exception as e:
            return {
                'confirm': False,
                'message': e
            }

    def updateRecord(self):
        try:
            for k, v in self.kwargs.items():
                if k == 'role':
                    role = Role.query.filter_by(name=k).first()
                    self.kwargs.pop('role')
                    self.kwargs['role_id'] = role.id
                setattr(self.tab, k, v)
            self.db.session.add(self.tab)
            self.db.session.commit()
            return {
                'confirm': True,
                'message': True
            }
        except Exception as e:
            self.db.session.rollback()
            return {
                'confirm': False,
                'message': False
            }

    def addRecord(self):
        try:
            role = Role.query.filter_by(name=self.kwargs['role']).first()
            self.kwargs.pop('role')
            self.kwargs['role_id'] = role.id
            tRecord = self.tab(**self.kwargs)
            self.db.session.add(tRecord)
            self.db.session.commit()
            return {
                'confirm': True,
                'message': 'User added success',
                'user_info': {
                    'create_date': tRecord.create_date,
                    'uuid': tRecord.uuid,
                }
            }
        except Exception as e:
            self.db.session.rollback()
            return {
                'confirm': False,
                'message': False
            }

    def delRecord(self):
        try:
            record = self.tab.query.filter_by(**self.kwargs).first()
            self.db.session.delete(record)
            self.db.session.commit()
            return {
                'message': {
                    'info': 'delete suc'
                }
            }
        except Exception as e:
            self.db.session.rollback()
            return {
                'message': {
                    'info': 'delete fail'
                }
            }