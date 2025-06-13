from time import sleep
from celery import shared_task


# Create a Celery instance@shared_task(bind=True, name='myapp.tasks.add')
def sub(self, x, y):
    return x - y