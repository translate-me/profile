from django.db import models
# from django.contrib.auth.models import PermissionsMixin
# from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext as _


class Author(models.Model):
    username = models.CharField(_("username"), max_length=50, primary_key=True)
    name = models.CharField(_("name"), max_length=200)
    birthdate = models.DateField()

    class Meta:
        verbose_name = _("name")
        verbose_name_plural = _("names")

    def __str__(self):
        return self.username
    def get_name(self):
        return self.name.strip()

    def get_birthday(self):
        return self.birthdate.strip()
