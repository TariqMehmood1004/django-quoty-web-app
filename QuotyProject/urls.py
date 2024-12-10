from django.contrib import admin
from django.urls import path, include
from QuotyProject import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('QuotyProjectApp.urls')),
]

# Serve media files during development (when DEBUG=True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)