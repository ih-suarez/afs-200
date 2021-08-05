from django.shortcuts import render, redirect
from django.utils import timezone
from app.models import Todo
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .form import NewUserForm
# Create your views here.

def home(request):
    todo_items = Todo.objects.all()
    return render(request, 'main/landing.html', {'todo_items': todo_items})

def register(request):
    if request.method=="POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'New Account Created: {username}')
            login(request, user)
            messages.info(request, f'You are logged in as {username}')
            return redirect('home')
        else:
            for msg in form.error_messages:
                messages.error(request, f'{msg}: {form.error_messages[msg]}')
    form = NewUserForm
    return render(request, 'main/register.html', context={'form': form})

def logout_request(request):
    logout(request)
    messages.info(request, 'Log Out Successful')
    return redirect('home')

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are logged in as {username}')
                return redirect('home')
            else: 
                messages.error(request, 'Invalid username and/or password')
    else:
        messages.error(request, 'Invalid username and/or password')
        
    form = AuthenticationForm()
    return render(request, 'main/login.html', context={'form': form})


def add_todo(request):
    if request.method == 'POST':
        current_date = timezone.now()
        content = request.POST['content']
        Todo.objects.create( added_date=current_date, todo=content)
        return redirect('home')
    else:
        return render(request, '404.html')

def delete_todo(request, id):
    if request.method == 'POST':
        Todo.objects.get(id=id).delete()
        return redirect('home')

