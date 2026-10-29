from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .models import Task

@require_POST
def addTask(request):
    task_text = request.POST.get('task', '').strip()
    if task_text:
        Task.objects.create(task=task_text)
    return redirect("home")

@require_POST
def mark_as_done(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed=True
    task.save()
    return redirect('home')

@require_POST
def undoTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save(update_fields=['is_completed', 'updated_at'])
    return redirect('home')

@require_POST
def editTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task_text = request.POST.get('task', '').strip()
    if task_text:
        task.task = task_text
        task.save(update_fields=['task', 'updated_at'])
    return redirect('home')

@require_POST
def deleteTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')