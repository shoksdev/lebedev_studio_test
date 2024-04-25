from django.db import models


class Event(models.Model):
    institution = models.CharField(max_length=256, verbose_name='Учреждение')
    region = models.CharField(max_length=256, verbose_name='Регион')
    address = models.CharField(max_length=256, verbose_name='Адрес')
    year = models.IntegerField(default=0, verbose_name='Год')
    budget_amount = models.IntegerField(default=0, verbose_name='Размер иного межбюджетного трансферта')
