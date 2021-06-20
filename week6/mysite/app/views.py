from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def  username(request):
    username = request.GET['username']
    return render(request, 'username.html', {'username': username})