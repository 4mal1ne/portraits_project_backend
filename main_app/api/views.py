from rest_framework import generics

from .serializers import (
    WorkSerializer,
    CommentsSerializer,
    WorkListSerializer,
    CommentsListSerializer
)
from ..models import Works, Comments


class WorkCreateView(generics.CreateAPIView):
    """
    Collecting the data stack and displaying it on the page.
    """
    serializer_class = WorkSerializer  # render all data from this serializer.


class CommentsCreateView(generics.CreateAPIView):
    """
    Collecting the data stack and displaying it on the page.
    """
    serializer_class = CommentsSerializer  # render all data from this serializer.


class WorksListView(generics.ListAPIView):
    serializer_class = WorkListSerializer  # The heir for this model is the model WorkListSerializer.
    queryset = Works.objects.all()  # Take the all data for model WorkListSerializer and save it.


class CommentsListView(generics.ListAPIView):
    serializer_class = CommentsListSerializer  # The heir for this model is the model CommentsListSerializer.
    queryset = Comments.objects.all()  # Take the all data for model CommentsListSerializer and save it.
