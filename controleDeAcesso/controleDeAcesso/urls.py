
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from controleDeAcesso.core import urls as coreUrls
from controleDeAcesso.contas import urls as accountsUrls
from controleDeAcesso.usuarios import urls as usuariosUrls

urlpatterns = [
    path('', include(coreUrls)),
    path('conta/', include(accountsUrls)),
    path('usuarios/', include(usuariosUrls)),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    