from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
# Create your views here.

@login_required
def task_list(request):
    tasks = Task.objects.filter(user = request.user)
    return render(request, 'tasks/task_list.html', {'tasks' : tasks})
from .models import Task

def add_task(request):
    
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority=request.POST.get('priority')
        due_date=request.POST.get('due_date')
        Task.objects.create(
            user = request.user,
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

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
        
    return redirect('task_list')


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        
        task.title = request.POST.get("title")
        task.description = request.POST.get("description")
        task.priority = request.POST.get("priority")
        task.due_date = request.POST.get("due_date")

        task.save() 

        return redirect('task_list')

    return render(request, 'tasks/add_task.html', {'task': task})

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('task_list')
    return render(request, 'tasks/signup.html')

def logout_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('task_list')
    return redirect(request, 'tasks/login.html')


