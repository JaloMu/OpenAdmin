# -*- coding: utf-8 -*-
# @Time    : 2017/11/12 上午1:54
# @Author  : Jalo.Mu
# @Site    : 
# @File    : loginInfoTable.py
# @Software: PyCharm

from datetime import datetime
from flask import request
from utils.ipQuery import QQWry


def query(path):
    q = QQWry(path)
    c, a = q.query('104.238.222.193')
    return {'address':'{0}'.format(c), 'supplier':'{0}'.format(a)}

class Query():
    '''
        @db: 数据引擎
        @tables 所有的表列表
        @kwargs 添加的数据
    '''
    def __init__(self, db,user, table, ip, path):
        self.db = db
        self.table = table
        self.user = user
        self.ip = ip
        self.path = path
        (self.address, self.supplier) = self.query()
    def query(self):
        q = QQWry(self.path)
        c, a = q.query(self.ip)
        return ('{0}'.format(c),'{0}'.format(a))
    def add(self):
        try:
            tab0 = self.table()
            tab0.uid = self.user.id
            tab0.username = self.user.username
            tab0.login_date = datetime.now()
            if request.user_agent.browser is None:
                tab0.browser = request.user_agent.string
            else:
                tab0.browser = request.user_agent.browser
            tab0.login_ip = request.remote_addr
            tab0.os = request.user_agent.platform
            tab0.login_address = self.address
            tab0.supplier = self.supplier
            self.db.session.add(tab0)
            self.db.session.commit()
            return {
                'confirm': True,
                'message': ''
            }
        except Exception as e:
            self.db.session.rollback()
            return {
                'confirm': False,
                'message': e
            }