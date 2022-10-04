from django.db import models


class Employees(models.Model):
    id_base = models.AutoField(primary_key=True)
    certificate = models.DecimalField(unique=True, decimal_places=0, max_digits=7, max_length=7,
                                      verbose_name='Номер удостоверения', help_text='Введите не более 7 цифр')
    full_name = models.CharField(max_length=35, verbose_name='Ф.И.О.')
    title = models.CharField(max_length=20, verbose_name='Звание')
    address = models.CharField(max_length=30, verbose_name='Адрес')
    family_composition = models.CharField(max_length=20, verbose_name='Состав семьи')

    def __str__(self):
        return f'{self.full_name}'

    class Meta:
        verbose_name = 'Сотрудникa'
        verbose_name_plural = 'Сотрудники'
        ordering = ('certificate',)


class IncidentDB(models.Model):
    id_base = models.AutoField(primary_key=True)
    certificate = models.DecimalField(unique=True, decimal_places=0, max_digits=7, max_length=7,
                                      verbose_name='Номер удостоверения', help_text='Введите не более 7 цифр')
    full_name = models.CharField(max_length=35, verbose_name='Ф.И.О.')
    title = models.CharField(max_length=20, verbose_name='Звание')
    address = models.CharField(max_length=30, verbose_name='Адрес')
    family_composition = models.CharField(max_length=20, verbose_name='Состав семьи')

    def __str__(self):
        return f'{self.full_name}'

    class Meta:
        verbose_name = 'Сотрудникa'
        verbose_name_plural = 'Сотрудники'
        ordering = ('certificate',)
