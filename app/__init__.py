from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'openadmin.auth.login'


def create_app(config_name):
    # 创建一个Flask实例
    app = Flask(__name__)

    # 配置文件初始化
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # 数据库初始化
    db.init_app(app)
    # 登录授权初始化
    login_manager.init_app(app)

    # 创建auth蓝图
    from .auth import auth as auth_buleprint
    app.register_blueprint(auth_buleprint, url_prefix='/auth')

