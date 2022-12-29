from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import TuristicPoint
from .serializers import TuristicPointSerializer
from rest_framework.decorators import action
import requests
import json

class TuristicPointView(ModelViewSet):
    # queryset = TuristicPoint.objects.all()
    serializer_class = TuristicPointSerializer
    def get_queryset(self):
        
        try:
            queryset = TuristicPoint.objects.all()
            id = self.request.query_params.get("id", None)
            name_params = self.request.query_params.get("name", None)
        
            if id:
                queryset = TuristicPoint.objects.filter(pk=id)
            if name_params:
                queryset = TuristicPoint.objects.filter(name__iexact = name_params)
            return queryset 

        except:
            return TuristicPoint.objects.filter(approval = True) 


    def list(self, request, *args, **kwargs):
        try:
            return super(TuristicPointView, self).list(request, *args, **kwargs) 
        except:
            date = requests.get("https://cdn.apicep.com/file/apicep/59650-000.json")
            date_json = json.loads(date.content)
            
            return Response(date_json)
            



    def create(self, request, *args, **kwargs):
        # print (request.data)
        return super(TuristicPointView, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(TuristicPointView, self).destroy(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        return super(TuristicPointView, self).retrieve(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return super(TuristicPointView, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(TuristicPointView, self).partial_update(request, *args, **kwargs)

    @action(methods=["get"], detail=False)
    def denunciar(self, request, pk=None):
        return Response({"teste": "Cheguei na action"})

    @action(methods=["get"], detail=True)
    def test(self, request, pk=None):
        return Response({"teste": "Cheguei na action"})