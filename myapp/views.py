from django.shortcuts import render

# Home Page View
def home_view(request):
    return render(request, 'home.html')

# About Page View
def about_view(request):
    return render(request, 'about.html')

# Contact Page View
def contact_view(request):
    return render(request, 'contact.html')
