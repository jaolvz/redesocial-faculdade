from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post
from django.http import HttpResponse



@login_required(login_url='usuarios:login')
def homepage(request):
    user = request.user
    posts = Post.objects.all()
    usuarios = User.objects.all()
    perfil = request.user.perfil
    imagem_perfil_url = perfil.imagem_perfil.url
    contexto = {'imagem_perfil_url': imagem_perfil_url,'user':user, 'usuarios':usuarios, 'posts':posts}
    return render(request, 'homepage.html', contexto)

def sair (request):
    request.session.flush()
    return redirect('home:home')

@login_required(login_url='usuarios:login')
def meuperfil(request):
    user = request.user
    perfil = request.user.perfil
    imagem_perfil_url = perfil.imagem_perfil.url
    contexto = {'imagem_perfil_url': imagem_perfil_url, 'user':user}
    return render(request,'meuperfil.html',contexto)

def upload_post(request):
    if request.method == 'POST':
        txt_post= request.POST.get('texto');
        autor_post = request.user
        post = Post.objects.create(autor=autor_post, conteudo=txt_post)
        return redirect('feed:homepage')
    else:
        # Caso a solicitação não seja POST, redirecione para alguma página de erro ou trate de outra forma
        return redirect('feed:meuperfil')
