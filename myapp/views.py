from django.shortcuts import render
from mycelery.celery import add
from myapp.task import sub 
from celery.result import AsyncResult
from django.shortcuts import redirect
from django_celery_results.models import TaskResult


#     #enque task using delay

# def home_view(request):
#     # Example of using a Celery task
#     result = add.delay(4, 6)  # Asynchronously add 4 and 6
#     print('result 1:',result)  # Log the task ID for debugging
#     # You can store the result in the session or database if needed
#     return render(request, 'home.html')


    # Enqueue task using apply_async
# def home_view(request):
#     # Example of using a Celery task
#     result = add.apply_async(args =[4, 6])
#     print('result 1:',result) 
#     # You can store the result in the session or database if needed
#     return render(request, 'home.html')

#    #display the result of the task
def home_view(request):
    result = add.delay(44, 6)
    return redirect('check_result', task_id=result.id)
    
def check_result(request, task_id):
    try:
        task_result = TaskResult.objects.get(task_id=task_id)
        context = {
            'task_id': task_result.task_id,
            'task_name': task_result.task_name,
            'status': task_result.status,
            'result': task_result.result,
            'traceback': task_result.traceback,
            'worker': task_result.worker,
            'created_at': task_result.date_created,
            'started_at': task_result.date_started,
            'completed_at': task_result.date_done,
        }
    except TaskResult.DoesNotExist:
        context = {
            'task_id': task_id,
            'status': 'Pending',
            'result': 'Task is still processing or not found.',
        }

    return render(request, 'result.html', {'result': context})

# About Page View
def about_view(request):
    result = sub.delay(33, 6) 
    print('result 1:',result)
    return render(request, 'about.html')

# Contact Page View
def contact_view(request):
    return render(request, 'contact.html')
