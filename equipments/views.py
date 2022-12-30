from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Equipment
from .serializers import EquipmentSerializer
# Create your views here.
class EquipmentView(ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    filterset_fields = ["name", "approval"]