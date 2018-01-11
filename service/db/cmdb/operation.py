# -*- coding: utf-8 -*-
# @Time    : 2017/11/26 下午5:22
# @Author  : Jalo.Mu
# @Site    : 
# @File    : operation.py
# @Software: PyCharm

class Operations:
    def __init__(self, db, tab):
        self.db = db
        self.tab = tab
    def create(self, name, desc=None):
        table = self.tab.query.filter_by(name = name).first()
        if table is not None:
            return table.id
        table = self.tab()
        table.name = name
        table.desc = desc
        self.db.session.add(table)
        self.db.session.commit()
        return table.id

    def delete(self, name):
        table = self.tab.query.filter_by(name=name).first()
        if table is None:
            return False
        return table
        # if table is None:
        #     return -1
        # self.db.session.delete(table)
        # self.db.session.commit()
        # return table.id

    def rename(self,name):
        table = self.tab.query.filter_by(name=name).first()
        if table is None:
            return -1
        self.db.session.add(table)
        self.db.session.commit()
        return table.id

    def select(self, **kwargs):
        table = self.tab.query.filter_by(**kwargs).first()
        return table