from rest_framework.viewsets import ModelViewSet
from .models import Assessment
from .serializers import AssessmentSeriliazer


class AssessmentView(ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSeriliazer
# Create your views here.
