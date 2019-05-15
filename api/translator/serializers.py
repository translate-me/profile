from rest_framework import serializers
from translator.models import (
    Language,
    Translator,
    Speak
)


class LaguageCreateOrUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fiedls = ['name']


class LaguageViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fiedls = "__all__"


class TranslatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translator
        fields = "__all__"


class SpeakSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speak
        fields = "__all__"
