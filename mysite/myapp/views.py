from django.shortcuts import render,redirect
from .models import Task

# Create your views here.
def add(request):
    if request.method=='POST':
        name = request.POST.get('name','')
        priority = request.POST.get('priority','')
        category = request.POST.get('category','')
        estimate_time = request.POST.get('estimate_time','')
        end_date = request.POST.get('end_date','')

        task=Task(name=name,priority=priority,category=category,estimate_time=estimate_time,end_date=end_date)
        task.save()
        return redirect('/')


    return render(request,'myapp/add.html')

def index(request):
    task_list = Task.objects.all()
    return render(request,'myapp/index.html',{'task_list':task_list})
