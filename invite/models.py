from django.db import models
from django.utils.translation import gettext_lazy as _

class Photo(models.Model):
    title = models.CharField(
        _('Название Фото'), max_length=64, help_text=_('Введите название фото'), unique=True
    )
    image = models.ImageField(
        _("Фото"),
        upload_to="images/",
        blank=True,
        null=True,
        help_text=_("Загрузите фото"),
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = _('Фотографии')
        verbose_name_plural = _('Фотографии')


class Music(models.Model):
    title = models.CharField(
        _('Музыка'), max_length=64, help_text=_('Введите название музыки'), unique=True
    )

    image = models.FileField(
        _("Музыка"),
        upload_to="music/",
        blank=True,
        null=True,
        help_text=_("Загрузите музыку"),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Музыка')
        verbose_name_plural = _('Музыка')

class Time(models.Model):
    day = models.IntegerField(
        _('День'),
        default=0,
        help_text=_('Введите количество дней')
    )
    hours = models.IntegerField(
        _('Час'),
        default=0,
        help_text=_('Введите количество часов')
    )

    def __str__(self):
        return f' {self.day} : {self.hours}'
    class Meta:
        verbose_name = _('Время')
        verbose_name_plural = _('Время')


class Guest(models.Model):

    fullname = models.CharField(
        _('Имя первого гостя'), max_length=64, help_text=_('Введите имя'), unique=True
    )
    fullname2 = models.CharField(
        _('Имя второго гостя'),blank=True,null=True,max_length=64, help_text=_('Введите имя'), unique=True
    )
    fullname3 = models.CharField(
        _('Имя третьего гостя'),blank=True,null=True, max_length=64, help_text=_('Введите имя'), unique=True
    )
    is_confirm_yes = models.BooleanField("Приду", default=False)
    is_confirm_no = models.BooleanField("Не приду", default=False)
    is_confirm_together = models.BooleanField("Приду не один", default=False)



    date = models.DateTimeField(
        _("Дата создания"),
        auto_now_add=True,
        help_text=_("Дата и время создания записи"),
    )

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = _('Гости')
        verbose_name_plural = _('Гости')


