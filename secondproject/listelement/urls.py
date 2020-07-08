from django.urls import path
from rest_framework import routers
from .viewsets import CategoryViewSet, TypeViewSet, ElementViewSet, CommentViewSet


route = routers.SimpleRouter()
route.register('category', CategoryViewSet)
route.register('type', TypeViewSet)
route.register('element', ElementViewSet)
route.register('comment', CommentViewSet)

urlpatterns = route.urls
