from time import sleep
from celery import shared_task
from mycelery.celery import app
from datetime import timedelta
from celery.schedules import crontab

# Create a Celery instance
@shared_task(bind=True, name='myapp.tasks.add')
def sub(self, x, y):
    return x - y

# @shared_task(name="myapp.task.clear_cache")
# def clear_cache(id):
#     """A task to clear the cache."""
#     print("Cache cleared!",{id})
#     return id

#   # A task to clear the cache method 2
# app.conf.beat_schedule = {
#     'clear_cache_every_10_seconds': {
#         'task': 'myapp.task.clear_cache',  # The task to run
#         'schedule': 10.0,  # Run every 10 seconds
#         'args': (1,),  # Arguments to pass to the task
#     }
# }

#  # A task to clear using timedelta

# app.conf.beat_schedule = {
#     'clear_cache_every_10_seconds': {
#         'task': 'myapp.task.clear_cache',  # The task to run
#         'schedule': timedelta(seconds=10),  # Run every 10 seconds
#         'args': (11,),  # Arguments to pass to the task
#     }
# }
app.conf.beat_schedule = {
    'clear_cache_every_10_seconds': {
        'task': 'myapp.task.clear_cache',  # The task to run
        'schedule': crontab(minute='*/1'),  # Run every 10 seconds
        'args': (11,),  # Arguments to pass to the task
    }
}