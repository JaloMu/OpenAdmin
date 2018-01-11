from . import user
from flask import jsonify

@user.app_errorhandler(401)
def unauthorized(e):
    return jsonify({'code': 401})

@user.app_errorhandler(403)
def forbidden(e):
    return jsonify({'code': 403})

@user.app_errorhandler(404)
def page_not_found(e):
    return jsonify({'code': 400})

@user.app_errorhandler(405)
def method_error(e):
    return jsonify({'code': 405})

@user.app_errorhandler(500)
def internal_server_error(e):
    return jsonify({'code': 500})