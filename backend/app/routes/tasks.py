from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from datetime import datetime
from ..models import Task, Project
from .. import db

bp = Blueprint('tasks', __name__, url_prefix='/api/tasks')

@bp.route('/', methods=['POST'])
@login_required
def create_task():
    data = request.get_json()
    
    if not data or not data.get('title') or not data.get('project_id'):
        return jsonify({'error': 'Title and project_id are required'}), 400
        
    # Verify project belongs to user
    project = Project.query.filter_by(id=data['project_id'], user_id=current_user.id).first()
    if not project:
        return jsonify({'error': 'Project not found'}), 404
        
    task = Task(
        title=data['title'],
        description=data.get('description', ''),
        status=data.get('status', 'not_started'),
        priority=data.get('priority', 'medium'),
        project_id=data['project_id']
    )
    
    if data.get('due_date'):
        try:
            task.due_date = datetime.fromisoformat(data['due_date'])
        except ValueError:
            return jsonify({'error': 'Invalid date format'}), 400
    
    db.session.add(task)
    db.session.commit()
    
    return jsonify(task.serialize), 201

@bp.route('/<int:task_id>', methods=['GET'])
@login_required
def get_task(task_id):
    task = Task.query.join(Project).filter(
        Task.id == task_id,
        Project.user_id == current_user.id
    ).first()
    
    if not task:
        return jsonify({'error': 'Task not found'}), 404
        
    return jsonify(task.serialize), 200

@bp.route('/<int:task_id>', methods=['PUT'])
@login_required
def update_task(task_id):
    task = Task.query.join(Project).filter(
        Task.id == task_id,
        Project.user_id == current_user.id
    ).first()
    
    if not task:
        return jsonify({'error': 'Task not found'}), 404
        
    data = request.get_json()
    
    if 'title' in data:
        task.title = data['title']
    if 'description' in data:
        task.description = data['description']
    if 'status' in data:
        task.status = data['status']
    if 'priority' in data:
        task.priority = data['priority']
    if 'due_date' in data:
        try:
            task.due_date = datetime.fromisoformat(data['due_date']) if data['due_date'] else None
        except ValueError:
            return jsonify({'error': 'Invalid date format'}), 400
            
    db.session.commit()
    
    return jsonify(task.serialize), 200

@bp.route('/<int:task_id>', methods=['DELETE'])
@login_required
def delete_task(task_id):
    task = Task.query.join(Project).filter(
        Task.id == task_id,
        Project.user_id == current_user.id
    ).first()
    
    if not task:
        return jsonify({'error': 'Task not found'}), 404
        
    db.session.delete(task)
    db.session.commit()
    
    return jsonify({'message': 'Task deleted successfully'}), 200

@bp.route('/project/<int:project_id>', methods=['GET'])
@login_required
def get_project_tasks(project_id):
    project = Project.query.filter_by(id=project_id, user_id=current_user.id).first()
    
    if not project:
        return jsonify({'error': 'Project not found'}), 404
        
    return jsonify([task.serialize for task in project.tasks]), 200 