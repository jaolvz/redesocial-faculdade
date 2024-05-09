from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='usuarios'

urlpatterns = [
        path('login/', views.login, name='login'),
        path('cadastro/',views.cadastro, name='cadastro'),
    ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)