# -*- coding: utf-8 -*-
# @Time    : 2017/11/12 下午9:35
# @Author  : Jalo.Mu
# @Site    : 
# @File    : field.py
# @Software: PyCharm
from app import db

class Field(db.Model):
    __tablename__ = 'sma_field'
    id = db.Column(db.Integer, index=True, unique=True, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    meta = db.Column(db.Text)
    schema_id = db.Column(db.Integer, db.ForeignKey('sma_schema.id'), nullable=False)
    value = db.relationship('Value', backref='field', lazy='dynamic')

    __table_args__ = (
        db.UniqueConstraint('name', 'schema_id', name='ux_schema_field'),
    )

__all__=["Field"]