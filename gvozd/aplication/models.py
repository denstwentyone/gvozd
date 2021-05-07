from django.db import models


class Aplications(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    favour = models.CharField('Услуга', max_length=50, default='Разбить окно')
    email = models.EmailField('email', unique=True)
    date = models.DateTimeField('Дата', auto_now_add=True)