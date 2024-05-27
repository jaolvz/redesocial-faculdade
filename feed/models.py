from django.db import models
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):

    #atribuindo um post a um usuario e on_delete cascade= usario deletado, posts deletados. 
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    conteudo = models.TextField()
    titulo = models.CharField(max_length=50,default='Título Padrão')
    postado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Postado por {self.autor.username}"
    
    @classmethod
    def obter_posts_do_usuario(cls,username):
        user = User.objects.get(username=username)
        posts_do_usuario = Post.objects.filter(autor=user)
        return posts_do_usuario
        
    def get_dataformatada(self):
        now = timezone.now()
        time_difference = now - self.postado

        if time_difference < timedelta(minutes=1):
            return "Postado há poucos segundos."
        elif time_difference < timedelta(hours=1):
            minutes = int(time_difference.total_seconds() // 60)
            return f"Postado há {minutes} minuto{'s' if minutes > 1 else ''}."
         #verificação inline
        elif time_difference < timedelta(days=1):
            hours = int(time_difference.total_seconds() // 3600)
            return f"Postado há {hours} hora{'s' if hours > 1 else ''}."
        else:
            days = time_difference.days
            return f"Postado há {days} dia{'s' if days > 1 else ''}."

class Comentario(models.Model):
    post = models.ForeignKey(Post, related_name='comentarios', on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()
    postado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário por {self.autor.username} em {self.post.titulo}"

    def get_dataformatada(self):
        now = timezone.now()
        tempo_diferança = now - self.postado

        if tempo_diferança  < timedelta(minutes=1):
            return f"{tempo_diferança } s."
            
        elif tempo_diferança  < timedelta(hours=1):
            minutos = int(tempo_diferança .total_seconds() // 60)
            return f" {minutos} min."
        elif tempo_diferança  < timedelta(days=1):
            horas = int(tempo_diferança .total_seconds() // 3600)
            return f" {horas} h"
        else:
            dias = tempo_diferança.days
            return f"Comentado há {dias} dia   "

