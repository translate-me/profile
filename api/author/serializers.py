from rest_framework import serializers
from author.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class AuthorSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["name", "birthdate"]
