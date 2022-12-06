from rest_framework.serializers import ModelSerializer
from .models import Localization

class LocalizationSerializer(ModelSerializer):
    class Meta:
        model = Localization
        fields = ("public_place", "state", "country", "coordenates_latitude", "coordenates_longitude")
        