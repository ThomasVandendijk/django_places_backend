from rest_framework import serializers
from google_places import models


class GooglePlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GooglePlace
        fields = '__all__'
