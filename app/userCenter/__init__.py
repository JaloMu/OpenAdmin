# -*- coding: UTF-8 -*-
from flask import Blueprint


user = Blueprint("user", __name__)

from . import errors, views