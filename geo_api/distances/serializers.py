from rest_framework import serializers
from .models import GeoPoints

class GeoPointsSerializer(serializers.ModelSerializer):

    class Meta():
        model = GeoPoints
        fields = ('origin_pts', 'dest_pts', 'roads_graph', 'dest_type',)