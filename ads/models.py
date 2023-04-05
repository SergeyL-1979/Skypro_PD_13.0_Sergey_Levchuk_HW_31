from django.db import models
from django.utils.translation import gettext as _

from category.models import Category
from users.models import User


# Create your models here.
class Announcement(models.Model):
    """Модель Announcements(Объявления)"""

    name = models.CharField(_("Наименование"), max_length=150)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, max_length=100, verbose_name="Автор"
    )
    price = models.FloatField(_("Цена"))
    description = models.TextField(_("Описание"))
    image = models.ImageField(_("Добавить фото"), upload_to="images", null=True)
    is_published = models.BooleanField(_("is_published"), null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория"
    )

    def image_(self):
        if self.image:
            from django.utils.safestring import mark_safe

            return mark_safe(
                u'<a href="{0}" target="_blank"><img src="{0}" width="150"/></a>'.format(
                    self.image.url
                )
            )
        else:
            return "(Нет изображения)"

    image_.short_description = "Фото"
    image_.allow_tags = True

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ["author__username"]

    def __str__(self):
        return '{}, NAME: {}'.format(self.author.username, self.name)


class Favorite(models.Model):
    """
    Модель позволяющая делать группу избранного и добавлять
    в нее выбранные объекты
    """
    name = models.CharField(max_length=15, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ads = models.ManyToManyField(Announcement, blank=True)

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранные"

    def __str__(self):
        return self.name

