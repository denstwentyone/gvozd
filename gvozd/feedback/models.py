from django.db import models



class Message(models.Model):
    username = models.CharField('Имя', max_length=1000)
    text = models.CharField('Сообщение', max_length=1000)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.username.name
