from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import TuristicPoint
from .serializers import TuristicPointSerializer
# Create your views here.

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