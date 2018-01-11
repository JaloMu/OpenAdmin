# -*- coding: utf-8 -*-
# @Time    : 2017/11/12 下午9:35
# @Author  : Jalo.Mu
# @Site    : 
# @File    : value.py
# @Software: PyCharm

from app import db

class Value(db.Model):
    __tablename__ = 'sma_value'
    id = db.Column(db.Integer, index=True, unique=True, nullable=False, primary_key=True, autoincrement=True)
    value = db.Column(db.Text, nullable=False)
    meta = db.Column(db.Text)
    field_id = db.Column(db.Integer, db.ForeignKey('sma_field.id'), nullable=False)
    entry_id = db.Column(db.Integer, db.ForeignKey('sma_entry.id'), nullable=False)

__all__=["Value"]