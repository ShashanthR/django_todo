from django.urls import path
from . import views

urlpatterns = [
    path('addtask/', views.addTask, name='addTask'),
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    path('undo/<int:pk>/', views.undoTask, name='undoTask'),
    path('edit/<int:pk>/', views.editTask, name='editTask'),
    path('delete/<int:pk>/', views.deleteTask, name='deleteTask'),
]