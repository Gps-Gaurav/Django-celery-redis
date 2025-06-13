from time import sleep
from celery import shared_task


# Create a Celery instance
@shared_task(bind=True, name='myapp.tasks.add')
def sub(self, x, y):
    return x - y

@shared_task(name="myapp.task.clear_cache")
def clear_cache(id):
    """A task to clear the cache."""
    print("Cache cleared!",{id})
    return id