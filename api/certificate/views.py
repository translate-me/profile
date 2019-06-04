from django.shortcuts import render
from certificate.models import Certificate
from certificate.serializers import CertificateSerializer
from rest_framework import generics
from rest_framework.permissions import (
    IsAdminUser
)

# Create your views here.

class AddCertificateView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

class ListCertificateView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer