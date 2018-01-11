# -*- coding: utf-8 -*-
# @Time    : 2017/11/6 下午5:42
# @Author  : Jalo.Mu
# @Site    : 
# @File    : config.py
# @Software: PyCharm

import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or 'hard to guess string'
    FLASKY_POSTS_PER_PAGE = 20
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        'mysql+pymysql://sma:123456@192.16.1.100:3306/sma?charset=utf8'

    HOST = '0.0.0.0'
    PORT = '8000'
    EXPIRATION = 8 * 3600
    QQPATH =basedir + '/modelsDB/ipdb/qqwry.dat'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        'mysql+pymysql://sma:123456@192.16.1.100:3306/sma?charset=utf8'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_RECORD_QUERIES = True
    HOST = '0.0.0.0'
    PORT = '8000'
    EXPIRATION = 8 * 3600


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        'mysql+pymysql://sma:123456@127.0.0.1:3306/sma?charset=utf8'
    HOST = '0.0.0.0'
    PORT = '8000'
    EXPIRATION = 8 * 3600

config = {
    'development': DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}