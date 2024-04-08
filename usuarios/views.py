from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django




def cadastro(request):
    if request.method=="GET":
        return render(request, 'cadastro.html')
    else:
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = User.objects.filter(username=usuario).first()
        if user:
            return HttpResponse("Já existe um usuário com esse usuário.")
        
        user = User.objects.create_user(username=usuario, email=email, password=senha)
        user.save()
        
        return HttpResponse ("Usuário cadastrado com sucesso!")



def login(request):
    if request.method=="GET":
        return render(request, 'login.html')
    else:
        usario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = authenticate(username=usario,password=senha)

        if user:
            login_django (request,user)
            return redirect('feed:home') 
        else:
            return HttpResponse("Usuario ou senha inválido")

        
'''
@login_required(login_url='/auth/login  ')
def plataforma(request):
    return HttpResponse("Logado!")


'''