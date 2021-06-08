from django.db import models


class Favour(models.Model):
    name = models.CharField(verbose_name='Название услуги', max_length=50)
    price = models.BigIntegerField(verbose_name='Цена', default=0)

    def __str__(self):
        return f'Услуга: {self.name}'


class Message(models.Model):
    username = models.CharField('Имя', max_length=1000)
    favour = models.ForeignKey(Favour, on_delete=models.PROTECT)
    text = models.CharField('Сообщение', max_length=1000)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
