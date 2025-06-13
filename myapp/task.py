from time import sleep
from celery import shared_task


# Create a Celery instance
@shared_task
def sub(x, y):
    
    sleep(8)  # Simulate a long-running task
    
    return x - y
 