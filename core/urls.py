
from django.contrib import admin
from django.urls import path, include

#avisa o projeto principal (core) para incluir essas URLs

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),          # Permite cadastro de usuário (/users/)
    path('api/v1/', include('djoser.urls.authtoken')), # Permite login (/token/login/)
    path('api/v1/', include('product.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
