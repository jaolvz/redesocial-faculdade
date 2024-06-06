from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from .models import Perfil
from django.core.files.storage import default_storage
from django.utils.text import slugify


def cadastro(request):
    if request.method=="GET":
        return render(request, 'cadastro.html')
    else:
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        nome =  request.POST.get('nome')
        imagem_perfil = request.FILES.get('imagem_perfil')

        user = User.objects.filter(username=usuario).first()
        if user:
            return HttpResponse("Já existe um usuário com esse usuário.")
        
        user = User.objects.create_user(username=usuario, email=email, password=senha, first_name=nome)

        if imagem_perfil:
            nome_imagem = slugify(user.username) + '.jpg'
            caminho_imagem = default_storage.save('imagens_perfil/' + nome_imagem, imagem_perfil)
            perfil, criado = Perfil.objects.get_or_create(usuario=user)
            perfil.imagem_perfil = caminho_imagem
            perfil.save() 

        return redirect ('usuarios:login')

def login(request):
    if request.method=="GET":
        return render(request, 'login.html')
    else:
        usario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = authenticate(username=usario,password=senha)

        if user:
            login_django (request,user)
            return redirect('feed:homepage') 
        else:
            return HttpResponse("Usuario ou senha inválido")

        