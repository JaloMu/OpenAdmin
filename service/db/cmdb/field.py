# -*- coding: utf-8 -*-
# @Time    : 2017/11/26 下午4:22
# @Author  : Jalo.Mu
# @Site    : 
# @File    : field.py.py
# @Software: PyCharm

def create(db, tab, id, **kwargs):
    table = tab.query.filter_by(schema_id=id).first()
    if table is not None:
        return table.id
    for f in kwargs["name"]:
        table = tab()
        if isinstance(f, dict):
            table(**f)
        else:
            table.name = f
        table.schema_id = id
        db.session.add(table)
    db.session.commit()
    return True

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
