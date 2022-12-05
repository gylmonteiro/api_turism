from rest_framework.serializers import ModelSerializer
from .models import Equipment

class EquipmentSerializer(ModelSerializer):
    class Meta:
        model = Equipment
        fields = ("name", "description", "approval", "opening_hours", "approval", "minimun_age")

