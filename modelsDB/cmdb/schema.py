# -*- coding: utf-8 -*-
# @Time    : 2017/11/12 下午9:35
# @Author  : Jalo.Mu
# @Site    : 
# @File    : schema.py
# @Software: PyCharm

from app import db

class Schema(db.Model):
    __tablename__ = 'sma_schema'
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True,autoincrement=True )
    name = db.Column(db.String(64), unique=True, nullable=False)
    desc = db.Column(db.Text)

    field = db.relationship('Field', backref='field', lazy='dynamic')
    entry = db.relationship("Entry", backref='entry', lazy='dynamic')

__all__=['Schema']