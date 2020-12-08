from django.conf import settings
from django.urls import path, include


urlpatterns = [
    path('records/', include('apps.records.urls')),
    path('reports/', include('apps.reports.urls')),
]


if settings.DEBUG:
    from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

    urlpatterns += [
        path('docs/', SpectacularAPIView.as_view(), name='schema'),
        path('docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
        path('docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    ]
