from .settings import (DEBUG, STATIC_ROOT, STATIC_URL, MEDIA_ROOT, MEDIA_URL)
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('appointment/', include('appointment.urls')),
] 

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT) 
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
