from rest_framework.serializers import ModelSerializer
from .models import TuristicPoint


class TuristicPointSerializer(ModelSerializer):
    class Meta:
        model = TuristicPoint
        fields = ('id', 'name', 'description', 'photo')
        
        # fields = "__all__" 
        '''
        Maneira de listar todos os campos
        '''