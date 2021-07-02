
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from app.models import Todo
from .forms import TodoForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http.response import HttpResponse
from django.contrib import messages


# Create your views here.

def login(request):
    return render(request, 'login.html')

def home(request):
    username = request.GET['username']
    todo_items = Todo.objects.all()
    return render(request, 'index.html',
    {
        "todo_items": todo_items,
        'username': username
    },)


def add_todo(request):
    if request.method == 'POST':
        current_date = timezone.now()
        content = request.POST['content']
        Todo.objects.create(added_date=current_date, todo=content)
        return redirect('home')
    else:
        return render(request, '404.html')


# def delete_todo(request, id):
#     Todo.objects.get(id=id).delete()
#     return redirect('/')


# def add_todo(request):
#     current_date = 'something'
#     content = request.POST['content']
#     # created_obj = Todo.objects.create(added_date=current_date, todo=content)
#     messages.info(request, content)
#     # created_obj.save()
#     Todo.objects.create(added_date=current_date, todo=content)
#     # form= TodoForm(request.POST or None)
#     # if form.is_valid():
#     #     form.save()
#     # todo_items = Todo.objects.all()
#     todo_items = Todo.objects.all()
    
#     context= {"todo_items": todo_items}
#     return redirect('/')
    # return HttpResponseRedirect('/')