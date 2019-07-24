from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import GeoPointsSerializer
import pandas as pd
from django.conf import settings
import csv
import io
import os
import pickle
import igraph as ig


from .dist_utils import csv_utils, straight_line_dist, site_routing


class GeoPointsView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):

        def csv_to_df(key):
            csv_file = request.data[key]
            csv_file.seek(0)
            data = [row for row in csv.DictReader(
                io.StringIO(csv_file.read().decode('utf-8')))]
            return pd.DataFrame(data)

        file_serializer = GeoPointsSerializer(data=request.data)

        if "dest_type" not in request.data.keys():
            return Response("Please specify a destination type",
                            status=status.HTTP_400_BAD_REQUEST)

        else:
            if file_serializer.is_valid():
                origin_df = csv_to_df('origin_pts')
                dest_df = csv_to_df('dest_pts')

                origin_pts = csv_utils.getTaggedPoints(origin_df)
                dest_pts = csv_utils.getTaggedPoints(dest_df)

                dest_type = request.data['dest_type']
                sl_dist_data = straight_line_dist.straight_line_distance(
                    origin_pts, dest_pts)

                if "roads_graph" not in request.data.keys():

                    if "country_name" in request.data.keys():
                        country_query = request.data['country_name'].lower().replace(
                            " ", "_")
                        for graph_fname in os.listdir(settings.GRAPHS_ROOT):
                            if country_query in graph_fname:
                                country_roadsG = pickle.load(
                                    open(settings.GRAPHS_ROOT + '/' + graph_fname, 'rb'))

                        routed_dist_data = site_routing.routed_distance(
                            origin_pts, dest_pts, country_roadsG)
                        col_names = ['Straight line distance to nearest ' + dest_type + ' (meters)',
                                     'Routed distance to nearest ' +
                                     dest_type + ' (meters)',
                                     'id']
                        updated_csv = csv_utils.makeUpdatedCsv(
                            routed_dist_data, col_names, origin_df)
                        return Response(updated_csv, status=status.HTTP_200_OK)
                    else:

                        col_names = ['Straight line distance to nearest ' + dest_type + ' (meters)',
                                     'id']
                        updated_csv = csv_utils.makeUpdatedCsv(
                            sl_dist_data, col_names, origin_df)

                        return Response(updated_csv, status=status.HTTP_200_OK)

                # else:
                #     print(request.data)
                #     col_names = ['Straight line distance to nearest ' + dest_type + ' (meters)',
                #                  'Routed distance to nearest ' + dest_type + ' (meters)',
                #                  'id']

                #     updated_csv = csv_utils.makeUpdatedCsv(sl_dist_data, col_names, origin_df)

                #     return Response(updated_csv, status=status.HTTP_200_OK)

            else:
                return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
