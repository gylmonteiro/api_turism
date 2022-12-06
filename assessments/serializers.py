from rest_framework.serializers import ModelSerializer
from .models import Assessment


class AssessmentSeriliazer(ModelSerializer):
    class Meta:
        model = Assessment
        fields = ("user", "description", "point", "date")
