from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .serializers import AnimalSerializers
from rest_framework import viewsets, filters
from .models import *


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all().order_by('name')
    serializer_class = AnimalSerializers
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['id', 'name']
