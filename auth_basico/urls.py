
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contas/',include('usuarios.urls')),
    path('',include('home.urls')),
    path('feed/',include('feed.urls'))
]
