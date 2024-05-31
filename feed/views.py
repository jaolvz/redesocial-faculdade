from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post, Comentario
from django.http import HttpResponse



@login_required(login_url='usuarios:login')
def homepage(request):
    user = request.user
    posts = Post.objects.order_by('-postado') #ordenandos os posts dos mais novos,pro mais velhos   
    usuarios = User.objects.all()
    perfil = request.user.perfil
    imagem_perfil_url = perfil.imagem_perfil.url
    contexto = {'imagem_perfil_url': imagem_perfil_url,'user':user, 'usuarios':usuarios, 'posts':posts}
    return render(request, 'homepage.html', contexto)

def sair (request):
    request.session.flush()
    return redirect('home:home')

@login_required(login_url='usuarios:login')
def perfil(request,usuario_solicitado):
    usuario_perfil = User.objects.get(username=usuario_solicitado)
    posts_usuario = Post.obter_posts_do_usuario(usuario_solicitado)
    contexto = {'usuario_perfil':usuario_perfil   ,'posts_do_usuario': posts_usuario }
    return render(request,'perfil.html',contexto)

@login_required(login_url='usuarios:login')
def upload_post(request):
    if request.method == 'POST':
        txt_post= request.POST.get('texto_conteudo')
        autor_post = request.user
        post = Post.objects.create(autor=autor_post, conteudo=txt_post)
        return redirect('feed:homepage')
    else:

        return redirect('feed:meuperfil')


@login_required(login_url='usuarios:login')
def upload_comentario(request,post_id):
    if request.method== 'POST':
        conteudo_comentario = request.POST.get('conteudo_comentario')
        autor_comentario = request.user 
        post_comentado =  get_object_or_404(Post, id=post_id)
        comentario = Comentario.objects.create(autor=autor_comentario, conteudo=conteudo_comentario, post=post_comentado)
        return redirect('feed:homepage')
    else:
        return HttpResponse("Vtmnccc")