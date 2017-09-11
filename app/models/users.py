from .. import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_login import UserMixin
from datetime import datetime
from flask import current_app

class Users(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False, index=True)
    uuid = db.Column(db.String(64), unique=True, nullable=False, index=True)
    email = db.Column(db.String(64), unique=True, nullable=False, index=True)
    phone = db.Column(db.String(11), unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    position = db.Column(db.String(64))
    ssh_key_pwd = db.Column(db.String(128))
    last_login = db.Column(db.DateTime, nullable=False, default=datetime.now())
    is_active = db.Column(db.Boolean, default=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), default=1, nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('usergroups.id'))
    section_id = db.Column(db.Integer, db.ForeignKey('sections.id'), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    create_user = db.Column(db.String(64), nullable=False, server_default="sma")
    updata_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    updata_user = db.Column(db.String(64), nullable=False, server_default="sma")

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def reset_password(self, new_password):
        self.password = new_password
        db.session.add(self)
        db.session.commit()
        return True

	def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    def __repr__(self):
        return '<User %r>' % self.username

    def __str__(self):
        return self.__repr__()


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))
