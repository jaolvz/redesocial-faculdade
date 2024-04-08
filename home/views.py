from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
def home(request):
    return render(request, 'home.html')

