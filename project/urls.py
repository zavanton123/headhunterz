from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from project import settings

# drf-yasg
schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Django admin url
    path('admin/', admin.site.urls),

    # DRF login url
    path('api-auth', include('rest_framework.urls')),

    # drf-yasg urls
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # my apps
    path('', include('apps.core.urls')),
    path('api/', include('apps.taxonomies.urls')),
    path('api/', include('apps.profiles.urls')),
    path('api/', include('apps.authentication.urls')),
    path('api/', include('apps.jobs.urls')),
]

# urls.py
if settings.DEBUG:
    import debug_toolbar

    # django debug toolbar
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns

    # media files
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
