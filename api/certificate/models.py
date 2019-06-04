from django.db import models

# Create your models here.

class Certificate(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    document = models.FileField(upload_to='document', blank=True, null=True)
