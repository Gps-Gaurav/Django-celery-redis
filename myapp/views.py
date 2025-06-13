from django.shortcuts import render
from mycelery.celery import add
from myapp.task import sub 


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
    print('result 1:', result) 
    return render(request, 'home.html', {'result': result})

def check_result(request, task_id):
    from celery.result import AsyncResult
    result = AsyncResult(task_id)
    
    if result.ready():
        return render(request, 'result.html', {'result': result.result})
    else:
        return render(request, 'result.html', {'result': 'Task is still processing.'})
    
    

# About Page View
def about_view(request):
    result = sub.delay(33, 6) 
    print('result 1:',result)
    return render(request, 'about.html')

# Contact Page View
def contact_view(request):
    return render(request, 'contact.html')
