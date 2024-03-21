# urls.py
from django.urls import include
from django.contrib.auth import views as auth_views
from .views import  update_task
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.task_list, name='task_list'),
    path('create/', views.create_task, name='create_task'),
    path('register/', views.register, name='register'),
    path('update/<int:task_id>/', update_task, name='update_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]