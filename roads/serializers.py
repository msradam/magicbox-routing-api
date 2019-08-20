from rest_framework import serializers
from .models import GraphRetrieval

class GraphRetrievalSerializer(serializers.ModelSerializer):

    class Meta():
        model = GraphRetrieval
        fields = ('country_name', 'network_type', 'filepath',)