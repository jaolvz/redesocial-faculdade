from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='feed'
urlpatterns = [
        path('homepage/',views.homepage ,name='homepage'),
        path('sair/', views.sair , name='sair'),
        path('meuperfil/', views.meuperfil, name='meuperfil'),
        path('upload/', views.upload_post, name='upload_post'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)