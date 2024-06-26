from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home_todo, name='todo_home'),
    path('delete/<int:id>', views.delete_todo, name='delete')
]