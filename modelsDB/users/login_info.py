# -*- coding: UTF-8 -*-
from app import db
from datetime import datetime

class LoginInfo(db.Model):
    __tablename__ = 'sma_loginInfo'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(64), nullable=False)
    login_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    login_ip = db.Column(db.String(15), nullable=False)
    browser = db.Column(db.String(20), nullable=False)
    os = db.Column(db.String(20), nullable=False)
    login_address = db.Column(db.String(256), nullable=False)
    supplier = db.Column(db.String(45), nullable=False)


    def __repr__(self):
        return '<LoginInfo>: %s %s %d' % self.username, self.login_address, self.counte

    def __str__(self):
        return self.__repr__()



__all__=['LoginInfo']