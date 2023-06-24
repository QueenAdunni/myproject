from django.shortcuts import render
from.models import Post,Description
from rest_framework import viewsets
from.serializer import PostSerializer,DescriptionSerializer
# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset= Post.objects.all()
    serializer_class = PostSerializer

class DescriptionViewSet(viewsets.ModelViewSet):
    queryset= Description.objects.all()
    serializer_class = DescriptionSerializer