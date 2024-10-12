from django.contrib import admin
from django.urls import path, include

from QuotyProject import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('QuotyProjectApp.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

