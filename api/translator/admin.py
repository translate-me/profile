from django.contrib import admin
from translator.models import (
    Language,
    Translator,
    Speak
)


admin.site.register(Language)
admin.site.register(Translator)
admin.site.register(Speak)
