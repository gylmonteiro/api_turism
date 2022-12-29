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
        return TuristicPoint.objects.filter(approval = True)

    def list(self, request, *args, **kwargs):
        try:
            date = requests.get("https://cdn.apicep.com/file/apicep/59650-000.json")
            date_json = json.loads(date.content)
            print(date_json)
            return Response(date_json)
        except:
            return Response({"Ola": "Passei direto"})
            # super(TuristicPointView, self).list(request, *args, **kwargs)



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

    @action(methods=["post", "get"], detail=True)
    def test(self, request, pk=None):
        return Response({"teste": "Cheguei na action"})