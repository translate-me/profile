from rest_framework import serializers
from translator.models import (
    Language,
    Translator,
    Speak
)


class LanguageCreateOrUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['name']


class LanguageViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"


class TranslatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translator
        fields = "__all__"


class SpeakSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speak
        fields = "__all__"
