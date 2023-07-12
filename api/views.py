from django.shortcuts import render
from webCaos.models import Mercaderia
from .serializers import mercaderiaSerializer
from rest_framework import generics

# Create your views here.

class MercaderiaViewSet(generics.ListAPIView):
    queryset = Mercaderia.objects.all()
    serializer_class = mercaderiaSerializer