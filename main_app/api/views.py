from rest_framework import generics

from .serializers import (
    WorkSerializer,
    CommentsSerializer
)
# from ..models import Works, Comments


class WorkCreateView(generics.CreateAPIView):
    """
    Collecting the data stack and displaying it on the page.
    """
    serializer_class = WorkSerializer


class CommentsCreateView(generics.CreateAPIView):
    """
    Collecting the data stack and displaying it on the page.
    """
    serializer_class = CommentsSerializer
