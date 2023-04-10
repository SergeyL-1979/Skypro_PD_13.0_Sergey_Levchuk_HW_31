from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Category(models.Model):
    """Модель Category(КАТЕГОРИЯ)"""
    name = models.CharField(_("Наименование"), max_length=64, unique=True)
    slug = models.SlugField(_("Slug"), max_length=10, unique=True, validators=[MinLengthValidator(5)])

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return "{}".format(self.name)
