from unicodedata import name
from django.urls import path
from .views import create_task,delete_task,home,mark_task

urlpatterns = [
    path('',home,name = 'home'),
    path('create',create_task,name='create'),
    path('mark/<int:pk>',mark_task,name = 'mark'),
    path('delete/<int:pk>',delete_task,name = 'delete')
]