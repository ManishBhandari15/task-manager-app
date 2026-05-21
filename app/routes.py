from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Task

main = Blueprint('main', __name__)


# Read - Show all tasks
@main.route('/')
def index():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template('index.html', tasks=tasks)


# Create - Add new task
@main.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    priority = request.form.get('priority')

    new_task = Task(
        title=title,
        description=description,
        priority=priority
    )

    db.session.add(new_task)
    db.session.commit()

    return redirect(url_for('main.index'))


# Update - Mark task complete or incomplete
@main.route('/complete/<int:task_id>')
def complete_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.complete = not task.complete
    db.session.commit()
    return redirect(url_for('main.index'))


# Update - Edit task
@main.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)

    if request.method == 'POST':
        task.title = request.form.get('title')
        task.description = request.form.get('description')
        task.priority = request.form.get('priority')
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('edit.html', task=task)


# Delete - Remove task
@main.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('main.index'))