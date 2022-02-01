import pdb 
from models.task import Task
from models.user import User
import repositories.task_repository as task_repository  
import repositories.user_repository as user_repository

task_repository.delete_all()
user_repository.delete_all()

user_1 = User("Jack", "Jarvis")
user_repository.save(user_1)
user_2 = User("Victor", "McDade")
user_repository.save(user_2)

users = user_repository.select_all()

task = Task("Talk Dog", user_1, 60)
task_repository.save(task)

tasks_of_user_1 = task_repository.tasks_for_user(user_1)

# task_1 = Task("Go for a run", 20)

# task_repository.save(task_1)

# task_1.mark_complete()
# #UPDATE HERE to reflect changes in the SQL side
# task_repository.update(task_1)

# result = task_repository.select_all()

# for task in result:
#     print(task.__dict__)

pdb.set_trace()