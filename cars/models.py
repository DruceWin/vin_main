from django.db import models

from django.contrib.postgres.fields import ArrayField


class Car(models.Model):
    year = models.CharField('Год выпуска', max_length=255)
    brand = models.CharField('Марка', max_length=255)
    model = models.CharField('Модель', max_length=255)
    vin = models.CharField('VIN', max_length=255, unique=True)
    odometer = models.CharField('Пробег (миль)', max_length=255)
    engine = models.CharField('Объем двигателя', max_length=255)
    gearbox = models.CharField('КПП', max_length=255)
    drive_train = models.CharField('Привод', max_length=255)
    auction_date = models.CharField('Дата аукциона', max_length=255)
    sale_type = models.CharField('Тип продажи', max_length=255)
    damage = models.CharField('Повреждения', max_length=255)
    photo = ArrayField(models.CharField('Фото', max_length=255))
    is_hidden = models.BooleanField('Скрыть для API v1', default=False)
    is_hidden_v2 = models.BooleanField('Скрыть для API v2', default=False)

    def __str__(self):
        return f'{self.brand} {self.model} {self.engine} {self.engine}'

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
        ordering = '-id'
