from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from project import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # DRF login url
    path('api-auth', include('rest_framework.urls')),

    # my apps
    path('api/accounts/', include('apps.authentication.urls')),
    path('accounts/', include('apps.authentication.myadmin.urls')),
]

# urls.py
if settings.DEBUG:
    import debug_toolbar

    # django debug toolbar
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns

    # media files
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
