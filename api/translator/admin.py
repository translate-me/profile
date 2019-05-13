from django.contrib import admin
from translator.models import (
    Language,
    Certification,
    Translator,
    Level
)


admin.site.register(Language)
admin.site.register(Certification)
admin.site.register(Translator)
admin.site.register(Level)
