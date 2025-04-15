from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import HrAccount
from .serializers import HrAccountSerializer

class HrAccountViewSet(viewsets.ModelViewSet):
    queryset = HrAccount.objects.all()
    serializer_class = HrAccountSerializer