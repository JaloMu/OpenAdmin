from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'sma.auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    login_manager.init_app(app)

    # create auth views
    from .authCenter import auth as auth_blueprint

    app.register_blueprint(auth_blueprint, url_prefix='/sma/auth')

    # create userCenter views
    from .userCenter import user as user_blueprint

    app.register_blueprint(user_blueprint, url_prefix='/sma/user')

    # create userCenter views
    from .cmdbCenter import cmdb as cmdb_blueprint

    app.register_blueprint(cmdb_blueprint, url_prefix='/sma/cmdb')

    # create userCenter views
    from .errorsCenter import error as error_blueprint

    app.register_blueprint(error_blueprint, url_prefix='/sma/error')

    return app