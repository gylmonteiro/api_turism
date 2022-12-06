from rest_framework.viewsets import ModelViewSet
from .models import Comment
from .serializers import CommentSerializer
# Create your views here.

class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
