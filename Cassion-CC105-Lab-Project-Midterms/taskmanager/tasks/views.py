from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    search_query = request.GET.get('search', '')  # Get the search query from GET parameter
    tasks = Task.objects.all()

    if search_query:
        tasks = tasks.filter(title__icontains=search_query)  # Filter tasks by title (case-insensitive)

    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'search_query': search_query})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

def task_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.status = 'complete'  # Mark task as complete
    task.save()
    return redirect('task_list')
