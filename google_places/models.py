from django.db import models
"""
class Location(models.Model):
    longitude = models.FloatField()
    lattitude = models.FloatField()


class Geometry(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE())
"""


class GooglePlace(models.Model):
    name = models.CharField(max_length=100)
    formatted_address = models.CharField(max_length=200)
    # geometry = models.ForeignKey(Geometry, on_delete=models.CASCADE())




