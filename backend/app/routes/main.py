from flask import Blueprint, jsonify

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return jsonify({
        'message': 'Welcome to the Task Management API',
        'version': '1.0',
        'endpoints': {
            'auth': {
                'register': '/api/auth/register',
                'login': '/api/auth/login',
                'logout': '/api/auth/logout',
                'me': '/api/auth/me'
            },
            'projects': {
                'list': '/api/projects',
                'create': '/api/projects',
                'get': '/api/projects/<id>',
                'update': '/api/projects/<id>',
                'delete': '/api/projects/<id>'
            },
            'tasks': {
                'create': '/api/tasks',
                'get': '/api/tasks/<id>',
                'update': '/api/tasks/<id>',
                'delete': '/api/tasks/<id>',
                'list_by_project': '/api/tasks/project/<id>'
            }
        }
    }) 