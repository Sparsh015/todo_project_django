from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
# Create your views here.

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks' : tasks})
from .models import Task

def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority=request.POST.get('priority')
        due_date=request.POST.get('due_date')
        Task.objects.create(
            title=title,
            description=description,
            priority=priority,
            due_date=due_date
        )

        return redirect('task_list')

    return render(request, 'tasks/add_task.html')

def toggle_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')