from django.db import models

# Create your models here.
class Task(models.Model):
    desc = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Описание")
    status = models.TextField(max_length=200, null=False, blank=False, verbose_name="Статус")
    author = models.CharField(max_length=200, null=False, blank=False, verbose_name="Автор")
    date = models.TextField(max_length=200, null=False, blank=False, verbose_name="Дедлайн")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время обновления")

    def __str__(self):
        return f"{self.author} - {self.desc}"
