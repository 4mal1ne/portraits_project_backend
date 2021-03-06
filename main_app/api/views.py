# DRF imports.
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

#  serializers imports.
from .serializers import (
    WorkSerializer,
    CommentsSerializer,
    WorkListSerializer,
    CommentsListSerializer
)
# Others imports.
from ..models import Works, Comments
from main_app.api.permissions import IsOwnerOrReadOnly


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
    """
    Display the entire json stack of data about the artist's work.
    """
    serializer_class = WorkListSerializer  # The heir for this model is the model WorkListSerializer.
    queryset = Works.objects.all()  # Take the all data for model WorkListSerializer and save it.
    permission_classes = (IsAdminUser,)  # The data set can only be viewed by a registered users.


class CommentsListView(generics.ListAPIView):
    """
    Display the entire json stack of data about the artist's works comments.
    """
    serializer_class = CommentsListSerializer  # The heir for this model is the model CommentsListSerializer.
    queryset = Comments.objects.all()  # Take the all data for model CommentsListSerializer and save it.


class WorksDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Change, or delete the json data stack.
    """
    serializer_class = WorkSerializer  # Selecting all fields from the "WorkSerializer" serializer.
    queryset = Works.objects.all()  # Take the all data for model 'Works' and save it.
    permission_classes = (
        IsOwnerOrReadOnly,
        IsAdminUser,
    )  # Only the admin or the user who created this entry can change the data in it.
