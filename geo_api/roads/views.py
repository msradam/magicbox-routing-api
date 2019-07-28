from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import GraphRetrievalSerializer
import pandas as pd
from django.conf import settings

from .osmnx_utils import retrieve_roads

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class GraphRetrievalView(APIView):
    @swagger_auto_schema(
        request_body=GraphRetrievalSerializer,
        operation_id="Retrieve Roads",
        operation_description="Retrieve and store graph road network of specified country."
    )
    def post(self, request, *args, **kwargs):

        serializer = GraphRetrievalSerializer(data=request.data)

        if serializer.is_valid():
            if "network_type" not in request.data.keys():
                network_type = 'all'
            else:
                network_type = request.data['network_type']

            country_name = request.data['country_name']
            filepath = settings.GRAPHS_ROOT + '/' + \
                country_name.lower().replace(' ', '_') + ".p"
            retrieval_response = retrieve_roads.make_igraph(
                country_name, network_type, filepath)

            return Response(retrieval_response, status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
