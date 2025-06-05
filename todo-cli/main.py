import utils.http_session
import utils.transport
import utils.session
import click
import os
import json

TODO_FILE = 'todo.json'

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=4)

@click.group()
def cli():
    pass

@cli.command()
@click.argument('task')
def add(task):
    """Add a new todo task."""
    tasks = load_todos()
    tasks.append({"task": task, "done": False})
    save_todos(tasks)
    click.echo(f"Task added successfully: {task}")

@cli.command(name="list")
def list_tasks():
    """List all todo tasks."""
    tasks = load_todos()
    if not tasks:
        click.echo("No tasks found.")
        return
    for i, task in enumerate(tasks, start=1):
        status = '✔' if task['done'] else '✖'
        click.echo(f"{i}. {task['task']} [{status}]")




@cli.command()
@click.argument('task_id', type=int)
def complete(task_id):
    """Mark a todo task as completed."""
    tasks = load_todos()
    if 0 < task_id <= len(tasks):
        tasks[task_id - 1]['done'] = True
        save_todos(tasks)
        click.echo(f"Task {task_id} marked as completed.")
    else:
        click.echo("Invalid task ID.")

@cli.command()
@click.argument('task_id', type=int)

def delete(task_id):
    """Delete a todo task."""
    tasks = load_todos()
    if 0 < task_id <= len(tasks):
        removed_task = tasks.pop(task_id - 1)
        save_todos(tasks)
        click.echo(f"Task deleted successfully: {removed_task['task']}")
    else:
        click.echo("Invalid task ID.")

if __name__ == '__main__':
    cli()
