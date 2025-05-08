from django.contrib import admin
from django.urls import path, include

# For serving media during development
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ✅ Custom error handlers
handler404 = 'main.views.error_views.handler404'
handler500 = 'main.views.error_views.handler500'
handler403 = 'main.views.error_views.handler403'
