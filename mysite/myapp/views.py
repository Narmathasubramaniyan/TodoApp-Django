from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def add_task(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')
        category = request.POST.get('category', '')
        estimate_time = request.POST.get('estimate_time', '')
        end_date = request.POST.get('end_date', '')

        task = Task(name=name, priority=priority, category=category, estimate_time=estimate_time, end_date=end_date)
        task.save()
        # After saving the task, redirect to the index page to display the task details
        return redirect('index')

    # If the request method is GET, render the add task form
    return render(request, 'myapp/index.html')

def index(request):
    task_list = Task.objects.all()
    return render(request, 'myapp/index.html', {'task_list': task_list})

def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('index')


