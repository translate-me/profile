from django.db import models
from author.models import Author
# from django.contrib.postgres.fields import ArrayField

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


class Certification(models.Model):
    archive = models.FileField(upload_to="certifications/", max_length=300)

    def __str__(self):
        return str(self.id)


class Translator(models.Model):
    username = models.OneToOneField(Author, on_delete=models.CASCADE,
                                    primary_key=True)
    cpf = models.CharField(max_length=14, null=False, blank=False)

    def __str__(self):
        return str(self.username)


class Level(models.Model):
    class Meta:
        unique_together = ('level_id', 'username')
    level_id = models.PositiveIntegerField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)
    certification = models.ForeignKey(Certification, on_delete=models.CASCADE)
    level = models.CharField(max_length=8, choices=LEVELS)
    username = models.OneToOneField(Translator, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.username) + " | " + str(self.level_id)
