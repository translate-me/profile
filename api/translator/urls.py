from django.conf.urls import url
from translator.views import (
    AddNewLanguage,
    ListLanguages,
    AddNewTranslator,
    ListTranslators,
    AddNewSpeak,
    ListSpeaks,
)
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Translator API",
      default_version='v0',
      description="Test description",
   ),
   public=True,
   permission_classes=(AllowAny,),
)

urlpatterns = [
    # language
    url(r"^api/v0/create/language/$", AddNewLanguage.as_view(),
        name="create_language"),
    url(r"^api/v0/list/language/$", ListLanguages.as_view(),
        name="list_languages"),
    # translator
    url(r"^api/v0/create/translator/$", AddNewTranslator.as_view(),
        name="create_translator"),
    url(r"^api/v0/list/translator/$", ListTranslators.as_view(),
        name="list_translators"),

    # speak
    url(r"^api/v0/create/speak/$", AddNewSpeak.as_view(), name="create_speak"),
    url(r"^api/v0/list/speak/$", ListSpeaks.as_view(), name="list_speak"),
]
