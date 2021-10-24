# from rest_framework import routers
# from .views import WorkViewSet, CommentsViewSet
#
# router = routers.SimpleRouter()
# router.register('artworks', WorkViewSet, basename='artworks')  # register "Work viewSet" in router in url path
# router.register('comments', CommentsViewSet, basename='comments')  # register "Comments viewSet" in router in url path
#
# urlpatterns = []
# urlpatterns += router.urls  # Add registered "urls" to the main routing.

from django.urls import path, include
from .views import *

app_name = 'artworks'
urlpatterns = [
    path('main_app/artworks/', WorkCreateView.as_view()),  # route Work view class.
    path('main_app/comments/', CommentsCreateView.as_view()),  # route Comments view class
    path('all_artworks/', WorksListView.as_view()),  # Watch all works data view.
    path('all_comments/', CommentsListView.as_view()),  # Watch all comments data view.
    path('detail/<int:pk>/', WorksDetailView.as_view()),  # Change all works data.
]
