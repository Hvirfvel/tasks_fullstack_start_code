from db.run_sql import run_sql

from models.task import Task
import repositories.user_repository as user_repository
  
def select_all():  
    tasks = [] 

    sql = "SELECT * FROM tasks"
    results = run_sql(sql)

    for row in results:
        user = user_repository.select(row['user_id'])
        task = Task(
            row['description'],
            user, 
            row['duration'], 
            row['completed'], 
            row['id'] )
        tasks.append(task)
    return tasks 

# CRUD
# CREATE

def save(task):
    # formatted string: f"" or f""" """
    sql = f"""
    INSERT INTO tasks 
    (description, user_id, duration, completed) 
    VALUES 
    (%s, %s, %s, %s)
    RETURNING id
    """
    values = [task.description, task.user.id, task.duration, task.completed]
    result = run_sql(sql, values)
    task.id = result[0]['id']

# READ -> SHOW
def select(id):
    task = None
    sql = "SELECT * FROM tasks WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        user = user_repository.select(result['user_id'])
        task = Task(
            result['description'], 
            user,
            result['duration'], 
            result['completed'], 
            result['id']
            )
    return task

# only for development - DELETE ALL
def delete_all():
    sql = "DELETE FROM tasks"
    run_sql(sql)

# DELETE ONE
def delete_one(id):
    sql = "DELETE FROM tasks WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# UPDATE
# task should be already updated on the Python side!
def update(task):
    sql = f"""
    UPDATE tasks
    SET (description, user_id, duration, completed)
    = (%s, %s, %s, %s)
    WHERE id = %s
    """
    values = [
        task.description, 
        task.user.id,
        task.duration, 
        task.completed, 
        task.id]
    run_sql(sql, values)

def tasks_for_user(user):
    tasks = []

    sql = "SELECT * FROM tasks WHERE id = %s"
    values = [user.id]
    results = run_sql(sql, values)

    for row in results:
        task = Task(row['description'], user, row['duration'], row['completed'], row['id'])
        tasks.append(task)
    return tasks