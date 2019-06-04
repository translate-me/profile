from rest_framework import serializers
from certificate.models import Certificate

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['image', 'document',]