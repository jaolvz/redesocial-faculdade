from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    conteudo = models.TextField()
    postado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Postado por {self.autor.username}"