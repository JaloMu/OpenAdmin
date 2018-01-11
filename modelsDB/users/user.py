# -*- coding: UTF-8 -*-
from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_login import UserMixin
from flask import current_app
from datetime import datetime
from uuid import uuid3, NAMESPACE_DNS

class Users(UserMixin, db.Model):
    __tablename__ = 'sma_users'
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(64), unique=True, nullable=False, index=True)
    username = db.Column(db.String(64), unique=True, nullable=False, index=True)
    email = db.Column(db.String(64), unique=True, nullable=False, index=True)
    phone = db.Column(db.String(11), unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    is_active = db.Column(db.Boolean, default=False)
    create_date = db.Column(db.DateTime, nullable=False)
    create_user = db.Column(db.String(64), nullable=False)
    updata_user = db.Column(db.String(64), nullable=False)
    updata_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    role_id = db.Column(db.Integer, db.ForeignKey('sma_role.id'), nullable=False)

    def can(self, persmissions):
        return self.role is not None and \
               self.role.name == persmissions

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


    @property
    def uuid_hash(self):
        return self.uuid

    @uuid_hash.setter
    def uuid_hash(self, username):
        self.uuid = str(uuid3(NAMESPACE_DNS, username.encode('utf-8'))).decode('utf-8')

    def reset_password(self, new_password):
        self.password = new_password
        db.session.add(self)
        db.session.commit()
        return True

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.uuid})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.uuid:
            return False
        return True

    def to_json(self):
        json_user= {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'phone': self.phone,
            'permission': self.role.name,
            'active': self.is_active,
            'create_data': self.create_date,
            'create_user': self.create_user,
            'update_user': self.updata_user,
            'update_date': self.updata_date
        }
        return json_user

    def __repr__(self):
        return '<User %r>' % self.username

    def __str__(self):
        return self.__repr__()


@login_manager.user_loader
def load_user(user_id):
    if Users.query.get(int(user_id)) is not None:
        return Users.query.get(int(user_id))

__all__=['Users']