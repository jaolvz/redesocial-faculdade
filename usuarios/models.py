from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE)
    imagem_perfil= models.ImageField(upload_to='imagens_perfil/',blank=True,null=True)

    def __str__(self):
        return self.user.username