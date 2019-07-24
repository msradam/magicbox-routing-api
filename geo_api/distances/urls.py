from django.conf.urls import url
from .views import GeoPointsView

urlpatterns = [
    url(r'^upload/$', GeoPointsView.as_view(), name='distances'),
]
