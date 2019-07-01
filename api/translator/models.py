from django.db import models
from author.models import Author
from django.core.validators import FileExtensionValidator

LEVELS = (
    ("High", "3"),
    ("Average", "2"),
    ("Low", "1")
)


class Language(models.Model):
    lang_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return str(self.lang_id) + " | " + self.name


class Translator(models.Model):
    username = models.OneToOneField(Author, on_delete=models.CASCADE,
                                    primary_key=True)
    cpf = models.CharField(max_length=14, null=False, blank=False)
    wallet = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.username)


class Speak(models.Model):
    class Meta:
        unique_together = ('language', 'username')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)
    certification = models.FileField(upload_to="certifications/",
                                     validators=[FileExtensionValidator(
                                         allowed_extensions=['pdf'])],
                                     max_length=300, null=True, blank=True)
    certification_is_valid = models.BooleanField(default=False)
    level = models.CharField(max_length=8, choices=LEVELS)
    username = models.ForeignKey(Translator, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.certification is None or not self.certification_is_valid:
            self.level = "Low"
        super(Speak, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.username) + " | " + str(self.language)
