from rest_framework.serializers import ModelSerializer
from .models import TuristicPoint
from equipments.serializers import EquipmentSerializer


class TuristicPointSerializer(ModelSerializer):
    equipments = EquipmentSerializer(many=True)
    class Meta:
        model = TuristicPoint
        fields = ('id', 'name', 'description', 'photo', 'equipments')
        
        # fields = "__all__" 
        '''
        Maneira de listar todos os campos
        '''