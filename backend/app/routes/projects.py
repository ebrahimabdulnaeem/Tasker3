from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from ..models import Project
from .. import db

bp = Blueprint('projects', __name__, url_prefix='/api/projects')

@bp.route('/', methods=['GET'])
@login_required
def get_projects():
    projects = Project.query.filter_by(user_id=current_user.id).all()
    return jsonify([{
        'id': p.id,
        'title': p.title,
        'description': p.description,
        'created_at': p.created_at.isoformat()
    } for p in projects]), 200

@bp.route('/', methods=['POST'])
@login_required
def create_project():
    data = request.get_json()
    
    if not data or not data.get('title'):
        return jsonify({'error': 'Title is required'}), 400
        
    project = Project(
        title=data['title'],
        description=data.get('description', ''),
        user_id=current_user.id
    )
    
    db.session.add(project)
    db.session.commit()
    
    return jsonify({
        'id': project.id,
        'title': project.title,
        'description': project.description,
        'created_at': project.created_at.isoformat()
    }), 201

@bp.route('/<int:project_id>', methods=['GET'])
@login_required
def get_project(project_id):
    project = Project.query.filter_by(id=project_id, user_id=current_user.id).first()
    
    if not project:
        return jsonify({'error': 'Project not found'}), 404
        
    return jsonify({
        'id': project.id,
        'title': project.title,
        'description': project.description,
        'created_at': project.created_at.isoformat(),
        'tasks': [task.serialize for task in project.tasks]
    }), 200

@bp.route('/<int:project_id>', methods=['PUT'])
@login_required
def update_project(project_id):
    project = Project.query.filter_by(id=project_id, user_id=current_user.id).first()
    
    if not project:
        return jsonify({'error': 'Project not found'}), 404
        
    data = request.get_json()
    
    if 'title' in data:
        project.title = data['title']
    if 'description' in data:
        project.description = data['description']
        
    db.session.commit()
    
    return jsonify({
        'id': project.id,
        'title': project.title,
        'description': project.description,
        'created_at': project.created_at.isoformat()
    }), 200

@bp.route('/<int:project_id>', methods=['DELETE'])
@login_required
def delete_project(project_id):
    project = Project.query.filter_by(id=project_id, user_id=current_user.id).first()
    
    if not project:
        return jsonify({'error': 'Project not found'}), 404
        
    db.session.delete(project)
    db.session.commit()
    
    return jsonify({'message': 'Project deleted successfully'}), 200 