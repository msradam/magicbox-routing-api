from django.db import models

class GraphRetrieval(models.Model):
    country_name = models.CharField(max_length=255)
    network_type = models.CharField(max_length=255, null=True)
    filepath = models.CharField(max_length=255, null=True)