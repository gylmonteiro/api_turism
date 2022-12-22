from rest_framework.viewsets import ModelViewSet
from .models import TuristicPoint
from .serializers import TuristicPointSerializer
# Create your views here.

class TuristicPointView(ModelViewSet):
    # queryset = TuristicPoint.objects.all()
    serializer_class = TuristicPointSerializer
    def get_queryset(self):
        return TuristicPoint.objects.filter(approval = True)