from rest_framework import serializers
from .models import EuroTravel
from io import BytesIO
from rest_framework.parsers import JSONParser

class EuroTravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EuroTravel
        fields = "__all__"
