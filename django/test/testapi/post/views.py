from django.shortcuts import render
from rest_framework import viewsets, permissions

from . import models
from . import serializers
# Create your views here.


class PostsViewset(viewsets.ModelViewSet):
    queryset = models.Posts.objects.all()
    serializer_class = serializers.ClubSerializer
