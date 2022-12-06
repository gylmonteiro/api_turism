from rest_framework.viewsets import ModelViewSet
from .serializers import LocalizationSerializer
from .models import Localization
# Create your views here.

class LocalizationView(ModelViewSet):
    queryset = Localization.objects.all()
    serializer_class = LocalizationSerializer

    