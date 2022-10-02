from django.shortcuts import render
from rest_framework import viewsets
from Wallpapers.models import WallpapersDetail
from Wallpapers.serializers import WallpaperSerializer
from django_filters.rest_framework import filters
from rest_framework import generics
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class WallpapersListApiView(generics.ListAPIView):
    queryset=WallpapersDetail.objects.all()
    serializer_class=WallpaperSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields = ['title','categories__name']