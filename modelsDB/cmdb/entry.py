# -*- coding: utf-8 -*-
# @Time    : 2017/11/12 下午9:35
# @Author  : Jalo.Mu
# @Site    : 
# @File    : enetry.py
# @Software: PyCharm

from app import db

class Entry(db.Model):
    __tablename__ = 'sma_entry'
    id = db.Column(db.Integer, index=True, unique=True, nullable=False, primary_key=True, autoincrement=True)
    key = db.Column(db.String(64), unique=True, nullable=False)
    schema_id = db.Column(db.Integer, db.ForeignKey('sma_schema.id'), nullable=False)

    value = db.relationship('Value', backref='entry', lazy='dynamic')

    __table_args__ = (
        db.UniqueConstraint('key', 'schema_id', name='ux_schema_entry'),
    )

__all__=['Entry']