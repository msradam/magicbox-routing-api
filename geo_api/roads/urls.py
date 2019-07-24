from django.conf.urls import url
from .views import GraphRetrievalView

urlpatterns = [
    url(r'^retrieve/$', GraphRetrievalView.as_view(), name='graph-retrieval'),
]
