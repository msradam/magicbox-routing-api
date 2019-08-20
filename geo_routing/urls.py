
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Magicbox Geospatial Routing API",
        default_version='v1',
        description="Utilities to compute distances between geospatial points and retrieve road networks for distance computations via routing.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="mrahmanadam@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^distances/', include('distances.urls')),
    url(r'^roads/', include('roads.urls')),
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # url(r'^swagger/$', schema_view.with_ui('swagger',
    #                                        cache_timeout=0), name='schema-swagger-ui'),
    url(r'^$', schema_view.with_ui('redoc',
                                   cache_timeout=0), name='schema-redoc'),
]
