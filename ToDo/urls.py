from django.urls import path
from . import views

urlpatterns = [
    path('addtask/', views.addTask, name='addTask'),
]