from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet


rout = DefaultRouter()
rout.register(r'posts/(?P<id>\d+)/comments',
              CommentViewSet, basename='comments')
rout.register('groups', GroupViewSet, basename='groups')
rout.register('posts', PostViewSet, basename='posts')
rout.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(rout.urls))
]
