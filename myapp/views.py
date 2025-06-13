from django.shortcuts import render
from mycelery.celery import add
from myapp.task import sub 

# Home Page View
def home_view(request):
    # Example of using a Celery task
    result = add.delay(4, 6)  # Asynchronously add 4 and 6
    print('result 1:',result)  # Log the task ID for debugging
    # You can store the result in the session or database if needed
    return render(request, 'home.html')

# About Page View
def about_view(request):
    result = sub.delay(4, 6)  # Asynchronously add 4 and 6
    print('result 1:',result)
    return render(request, 'about.html')

# Contact Page View
def contact_view(request):
    return render(request, 'contact.html')
