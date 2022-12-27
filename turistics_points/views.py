from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import TuristicPoint
from .serializers import TuristicPointSerializer
from rest_framework.decorators import action

class TuristicPointView(ModelViewSet):
    # queryset = TuristicPoint.objects.all()
    serializer_class = TuristicPointSerializer
    def get_queryset(self):
        return TuristicPoint.objects.filter(approval = True)

    def list(self, request, *args, **kwargs):
        return Response({"teste": "deu certo"})

    def create(self, request, *args, **kwargs):
        print (request.data)
        return Response({"teste": "criei recurso"})

    def destroy(self, request, *args, **kwargs):
        return Response({"Ok": "Delete"})
    
    def retrieve(self, request, *args, **kwargs):
        return Response({"teste": "ok"})
    
    def update(self, request, *args, **kwargs):
        return Response({"teste": "ok"})

    def partial_update(self, request, *args, **kwargs):
        return Response({"teste": "ok"})

    @action(methods=["get"], detail=False)
    def denunciar(self, request, pk=None):
        return Response({"teste": "Cheguei na action"})

    @action(methods=["post", "get"], detail=True)
    def test(self, request, pk=None):
        return Response({"teste": "Cheguei na action"})