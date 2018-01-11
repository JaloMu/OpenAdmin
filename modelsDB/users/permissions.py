# -*- coding: utf-8 -*-
# @Time    : 2017/11/12 下午9:35
# @Author  : Jalo.Mu
# @Site    :
# @File    : permissions.py
# @Software: PyCharm
from app import db

class BasePer:
    Read = 0x01
    Mod = 0x02
    Write = 0x04
    Sup = 0x10


class Role(db.Model):
    __tablename__ = 'sma_role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    permissions = db.Column(db.Integer)
    users = db.relationship('Users', backref='role', lazy = 'dynamic')

    @staticmethod
    def insert_roles():
        roles = {
            "User": BasePer.Read |
                     BasePer.Mod,
            "Guest": BasePer.Read |
                      BasePer.Write,
            "Auth": BasePer.Read|
                     BasePer.Sup,
            "Admin": BasePer.Read |
                      BasePer.Sup |
                      BasePer.Write |
                      BasePer.Mod
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r]
            db.session.add(role)
        db.session.commit()

