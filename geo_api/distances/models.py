from django.db import models

class GeoPoints(models.Model):
    origin_pts = models.FileField()
    dest_pts = models.FileField()
    roads_graph = models.FileField(blank=True, null=True)
    dest_type = models.CharField(max_length=255)
    country_name = models.CharField(max_length=255, null=True)
    # description = models.CharField(max_length=255)
    # uploaded_at = models.DateTimeField(auto_now_add=True)
