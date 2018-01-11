# -*- coding: utf-8 -*-
# @Time    : 2017/11/26 下午4:21
# @Author  : Jalo.Mu
# @Site    : 
# @File    : schame.py
# @Software: PyCharm

def create(db, tab, name, desc=None):
    table = tab.query.filter_by(name = name).first()
    if table is not None:
        return table.id
    table = tab()
    table.name = name
    table.desc = desc
    db.session.add(table)
    db.session.commit()
    return table.id

# def delete(db, tab, name):
#     table = tab.query.filter_by(name=name).first()
#     if table is None:
#         return False
#     return table
#     # if table is None:
#     #     return -1
#     # self.db.session.delete(table)
#     # self.db.session.commit()
#     # return table.id
#
# def rename(self,name):
#     table = self.tab.query.filter_by(name=name).first()
#     if table is None:
#         return -1
#     self.db.session.add(table)
#     self.db.session.commit()
#     return table.id
#
# def select(self, **kwargs):
#     table = self.tab.query.filter_by(**kwargs).first()
#     return table


