from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='feed'
urlpatterns = [
        path('homepage/',views.homepage ,name='homepage'),
        path('sair/', views.sair , name='sair'),
        path('@<str:usuario_solicitado>/', views.perfil, name='perfil'),
        path('upload/', views.upload_post, name='upload_post'),
        path('upload_comentario/<int:post_id>/', views.upload_comentario, name='upload_comentario'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)