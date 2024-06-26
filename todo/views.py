from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def home_todo(request):
    if request.method == "POST":
        task=request.POST['task']
        Todo.objects.create(title=task)

    all_works=Todo.objects.all()



    return render(request,'todo.html',context={'work_list':all_works})


def delete_todo(request,id):
    Todo.objects.get(id=id).delete()
    return redirect('todo_home')