from django.db import models


class Favour(models.Model):
    name = models.CharField(verbose_name='Название услуги', max_length=50)
    price = models.BigIntegerField(verbose_name='Цена', default=0)

    def __str__(self):
        return f'Услуга: {self.name}'

    class Meta:
        verbose_name_plural = 'Услуги'


class Aplications(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    email = models.EmailField(verbose_name='email', unique=True)
    date = models.DateTimeField(verbose_name='Дата заяки', auto_now_add=True)
    favour = models.ForeignKey(Favour, on_delete=models.PROTECT, verbose_name='Название услуги, цена')

    class Meta:
        verbose_name_plural = 'Заявки пользователей'
