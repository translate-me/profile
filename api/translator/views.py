from translator.models import (
    Speak,
    Translator,
    Language
)
from translator.serializers import (
    LanguageCreateOrUpdateSerializer,
    LanguageViewSerializer,
    TranslatorSerializer,
    SpeakSerializer
)
from rest_framework import generics
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAdminUser
)
from drf_yasg.utils import swagger_auto_schema
import unidecode

"""
Language
"""


class AddNewLanguage(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Language.objects.all()
    serializer_class = LanguageCreateOrUpdateSerializer

    @swagger_auto_schema(request_body=LanguageCreateOrUpdateSerializer,
                         response={200: LanguageViewSerializer},
                         operation_description="Add new language")
    def perform_create(self, serializer):
        instance = serializer.save()
        name = unidecode.unidecode(instance.name)
        name = name.lower()
        serializer.save(name=name)


class ListLanguages(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Language.objects.all()
    serializer_class = LanguageViewSerializer


"""
Translator
"""


class AddNewTranslator(generics.CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Translator.objects.all()
    serializer_class = TranslatorSerializer

    @swagger_auto_schema(request_body=TranslatorSerializer,
                         response={200: TranslatorSerializer},
                         operation_description="Add new translator")
    def perform_create(self, serializer):
        serializer.save()


class ListTranslators(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = Translator.objects.all()
    serializer_class = TranslatorSerializer


"""
Speak
"""


class AddNewSpeak(generics.CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Speak.objects.all()
    serializer_class = SpeakSerializer

    @swagger_auto_schema(request_body=SpeakSerializer,
                         response={200: SpeakSerializer},
                         operation_description="Add new speak relation.")
    def perform_create(self, serializer):
        serializer.save()


class ListSpeaks(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = Speak.objects.all()
    serializer_class = SpeakSerializer
