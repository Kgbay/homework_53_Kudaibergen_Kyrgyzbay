# Generated by Django 4.1.6 on 2023-02-17 05:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='Заголовок не задан', max_length=200, verbose_name='Заголовок')),
                ('full_desc', models.TextField(max_length=3000, null=True, verbose_name='Полное описание')),
                ('status', models.CharField(choices=[('ACTIVE', 'Активна'), ('NOT_ACTIVE', 'Неактивна')], default='ACTIVE', max_length=20, verbose_name='Статус')),
                ('author', models.CharField(max_length=200, verbose_name='Автор')),
                ('date', models.DateField(default=datetime.datetime(2023, 2, 17, 5, 9, 24, 859871, tzinfo=datetime.timezone.utc), verbose_name='date')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')),
            ],
        ),
    ]
