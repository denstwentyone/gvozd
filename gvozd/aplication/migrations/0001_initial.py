# Generated by Django 3.2.1 on 2021-05-07 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('favour', models.CharField(default='Разбить окно', max_length=50, verbose_name='Услуга')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
            ],
        ),
    ]