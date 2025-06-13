
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('check_result/<str:task_id>/', views.check_result, name='check_result'),
]
