from rest_framework import viewsets

from .serializers import (
    WorkSerializer,
    CommentsSerializer
)
from ..models import Works, Comments


class WorkViewSet(viewsets.ModelViewSet):
    """
    Collecting the data stack and displaying it on the page.
    """
    queryset = Works.objects.all()
    serializer_class = WorkSerializer


class CommentsViewSet(viewsets.ModelViewSet):
    """
    Collecting the data stack and displaying it on the page.
    """
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


