import json
from time import sleep
from celery import shared_task
from mycelery.celery import app
from datetime import timedelta
from celery.schedules import crontab,solar
from django_celery_beat.models import PeriodicTask, IntervalSchedule

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
# app.conf.beat_schedule = {
#     'clear_cache_every_10_seconds': {
#         'task': 'myapp.task.clear_cache',  # The task to run
#         'schedule': crontab(minute='*/1'),  # Run every 10 seconds
#         'args': (11,),  # Arguments to pass to the task
#     }
# }

# @app.on_after_configure.connect
# def setup_periodic_tasks(sender: Celery, **kwargs):
#     # Calls test('hello') every 10 seconds.
#     sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

#     # Calls test('hello') every 30 seconds.
#     # It uses the same signature of previous task, an explicit name is
#     # defined to avoid this task replacing the previous one defined.
#     sender.add_periodic_task(30.0, test.s('hello'), name='add every 30')

#     # Calls test('world') every 30 seconds
#     sender.add_periodic_task(30.0, test.s('world'), expires=10)

#     # Executes every Monday morning at 7:30 a.m.
#     sender.add_periodic_task(
#         crontab(hour=7, minute=30, day_of_week=1),
#         test.s('Happy Mondays!'),
#     )

# @app.task
# def test(arg):
#     print(arg)

# @app.task
# def add(x, y):
#     z = x + y
#     print(z)

app.conf.beat_schedule = {
    # Executes at sunset in Melbourne
    'add-at-melbourne-sunset': {
        'task': 'tasks.add',
        'schedule': solar('sunset', -37.81753, 144.96715),
        'args': (16, 16),
    },
}

def clear_redis_cache(key):
    """A task to clear the cache."""
    print("Redis Cache cleared!", {'key': key})
    return key

def clear_rabbitmq_cache(key):
    """A task to clear the cache."""
    print("Rabbitmq Cache cleared!", {'key': key})
    return key

schedude,created =IntervalSchedule.objects.get_or_create(
    every=10,
    period=IntervalSchedule.SECONDS,
)
PeriodicTask.objects.create(
    interval=schedude,
    name='clear_redis_cache',
    task='myapp.task.clear_redis_cache',
    args=json.dumps([1]),
)
